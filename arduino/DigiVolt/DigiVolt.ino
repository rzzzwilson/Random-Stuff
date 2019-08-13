////////////////////////////////////////////////////////
// Test code for the DigiVolt.
//
// Use the internal 2.56 volts reference and use the digital
// potentiometer to get a "full-scale" reading and calculate
// the voltage from the reading * 2.56 * potentiometer ratio.
////////////////////////////////////////////////////////

#include <SPI.h>

// Voltage measurement program name & version
const char *ProgramName = "DigiVolt";
const char *Version = "0.2";

// internal LED pin
int ledPin = 12;                // D6 on the Iota

// set pin 17 as the slave select for the digital pot
// other SPI pins are as assumed on the Iota
const int slaveSelectPin = 17;  // B0 on the Iota

// value of internal reference
const float ARef = 2.56;

// command bytes for the digital pot
byte writePot0 = B00010001; // write to pot 0
byte writePot1 = B00010010; // write to pot 1

// pin numbers for each voltage channel
const int NumChannels = 2;
int ChannelPin[NumChannels] = {23, 22};
//                             F0  F1 pins

// offset values (current) for each channel
int ChanOffset[NumChannels] = {0, 0};

// values for max and min offset
const int MinOffset = 0;
const int MaxOffset = 255;

// buffer, etc, to gather external command strings
#define MAX_COMMAND_LEN   16
#define COMMAND_END_CHAR    ';'
char CommandBuffer[MAX_COMMAND_LEN+1];
int CommandIndex = 0;

const char *ErrorMsg = "ERROR";


/////////////////////////////////////////////////////////////
// Convert a string to uppercase in situ.
/////////////////////////////////////////////////////////////

void str2upper(char *str)
{
  while (*str)
  {
    *str = toupper(*str);
    ++str;
  }
}

/////////////////////////////////////////////////////////////
// Set 'channel' pot to the given 'offset'.
/////////////////////////////////////////////////////////////

void digitalPotWrite(int channel, int offset)
{
  // handle multiple channels
  byte cmd = writePot0;
  if (channel != 0)
  {
    // if it's not channel 0, assume channel 1
    cmd = writePot1;
  }

  // send value to the appropriate channel
  SPI.beginTransaction(SPISettings(10000000, MSBFIRST, SPI_MODE0));
  digitalWrite(slaveSelectPin, LOW);
  SPI.transfer(cmd);
  SPI.transfer(offset);
  digitalWrite(slaveSelectPin, HIGH);
  SPI.endTransaction();
}


/////////////////////////////////////////////////////////////
// Read the voltage on 'channel' pot.
/////////////////////////////////////////////////////////////

float voltageRead(int channel)
{
  // the working variables
  int dig_value = 0;
  int pin = ChannelPin[channel];
  int pot_step = 16;
  int last_offset = 0;

  // first, set wiper to 0 offset (protect the pot chip)
  digitalPotWrite(channel, 0);

  // step up until we get the largest reading <= 1023 for the voltage
  for (int offset = 1; offset < 256; offset += pot_step)
  {
    digitalPotWrite(channel, offset);
    int read_value = analogRead(pin);
    
    if (read_value >= 1023)
        break;
    dig_value = read_value;
    last_offset = offset;
  }

  // set wiper to 0 offset again (protect the pot chip)
  digitalPotWrite(channel, 0);

  // we have enough, use last_offset and dig_value to calculate voltage
  return (ARef * dig_value / 1023) * 255 / last_offset;
}


//##############################################################################
// External command routines.
//
// External commands are:
//     H;           send help text to console
//     ID;          get device identifier string
//     NG;          get number of channels
//     V?G;         get voltage on channel '?'
//##############################################################################

//----------------------------------------
// Get help:
//     H;
//----------------------------------------

const char * xcmd_help(char *answer, char *cmd)
{
  // to turn off warning about "unused parameter"
  cmd[0] = '\0';
  
  strcpy(answer, (char *) "-----------Interactive Commands-----------------\n");
  strcat(answer, (char *) "H;         send help text to console\n");
  strcat(answer, (char *) "ID;        get device identifier string\n");
  strcat(answer, (char *) "NG;        get number of channels\n");
  strcat(answer, (char *) "V?G;       get voltage for channel '?'\n");
  strcat(answer, (char *) "------------------------------------------------");
  return answer;
}

//----------------------------------------
// Get the identifier string:
//     ID;
//----------------------------------------

const char * xcmd_id(char *answer, char *cmd)
{
  // if not legal, complain
  if (strcmp(cmd, "ID;"))
    return ErrorMsg;

  // generate ID string and return
  strcpy(answer, ProgramName);
  strcat(answer, " ");
  strcat(answer, Version);
  return answer;
}

//----------------------------------------
// Get the number of channels:
//     NG;
//----------------------------------------

const char * xcmd_nc(char *answer, char *cmd)
{
  // if not legal, complain
  if (strcmp(cmd, "NG;"))
    return ErrorMsg;

  // generate answer string and return
  sprintf(answer, "%d\n", NumChannels);
  return answer;
}

//----------------------------------------
// Get voltage for a channel:
//     V?G;
//----------------------------------------

const char * xcmd_vx(char *answer, char *cmd)
{
  float voltage = 0;

  // if not legal, complain
  if (strlen(cmd) < 4)
    return ErrorMsg;

  // get channel number, check legal
  int channel = cmd[1] - '0';
  if ((channel < 0) or (channel >= NumChannels))
    return ErrorMsg;

  // do a GET
  if (cmd[2] == 'G')
  {
    if (cmd[3] != ';')
      return ErrorMsg;
    voltage = voltageRead(channel);
    dtostrf(voltage, 1, 2, answer);
    return answer;
  }
    
  return ErrorMsg;
}

//----------------------------------------
// Process an external command.
//     answer  address of place to store answer string
//     cmd     address of command string buffer
//     index   index of last char in string buffer
// 'cmd' is '\0' terminated.
// Returns the command response string.
//----------------------------------------
const char * do_external_cmd(char *answer, char *cmd, int index)
{
  char end_char = cmd[index];

  // ensure everything is uppercase
  str2upper(cmd);

  // if command too long it's illegal
  if (end_char != COMMAND_END_CHAR)
  {
    return (char *) "TOO LONG";
  }

  // process the command
  switch (cmd[0])
  {
    case 'H':
      return xcmd_help(answer, cmd);
    case 'I':
      return xcmd_id(answer, cmd);
    case 'N':
      return xcmd_nc(answer, cmd);
    case 'V':
      return xcmd_vx(answer, cmd);
  }

  return xcmd_help(answer, cmd);
}

void do_external_commands(void)
{
  // gather any commands from the external controller
  while (Serial.available()) 
  {
    char ch = Serial.read();

    // ignore newlines
    if (ch == '\n')
      continue;
    
    if (CommandIndex < MAX_COMMAND_LEN)
    { 
      // only add if command not over-length
      CommandBuffer[CommandIndex++] = ch;
    }
    
    if (ch == COMMAND_END_CHAR)   // if end of command, execute it
    {
      char answer[512];           // place to construct answer strings
      
      CommandBuffer[CommandIndex] = '\0';
      
      digitalWrite(ledPin, HIGH);

      Serial.println("");
      Serial.print("Command='");
      Serial.print(CommandBuffer);
      Serial.println("'");
      
      sprintf(answer, "%s\n", do_external_cmd(answer, CommandBuffer, CommandIndex-1));
      
      Serial.print(answer);
      digitalWrite(ledPin, LOW);
      
      CommandIndex = 0;
    }
  }
}

void setup()
{
  Serial.begin(19200);
  analogReference(INTERNAL);   // 2.56 volt reference
  
  pinMode(slaveSelectPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  for (int chan = 0; chan < NumChannels; chan += 1)
  {
    digitalPotWrite(chan, 0);
  }
  digitalWrite(slaveSelectPin, LOW);
  digitalWrite(ledPin, LOW);
  
  SPI.begin();

  delay(3000);
  Serial.print(ProgramName);
  Serial.print(" ");
  Serial.print(Version);
  Serial.println(" ready.");
  Serial.println("Enter 'H;' and <enter> to get help.");
}

void loop()
{
  // do any external commands
  do_external_commands();
//  delay(100);   // not too fast
}
