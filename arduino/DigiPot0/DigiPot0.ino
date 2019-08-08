////////////////////////////////////////////////////////
// Test code for the MCP42100 chip.
//
// Just wipe channel 0 from 0 to 5 volts and then from
// 5 to 0 volts (configurable steps and pauses).  Repeat.
//
// With a 'step' of 1 and a 'pause' of 0 we can get a
// triangular wave of >160Hz.  Fast enough!  There is
// some "ringing" noise on changes.
////////////////////////////////////////////////////////

#include <SPI.h>
#include <MCP41xxx.h>

// internal LED pin
int ledPin = 12;                // D6 on the Iota

// set pin 17 as the slave select for the digital pot
// other SPI pins are as assumed on the Iota
const int slaveSelectPin = 17;  // B0 on the Iota

// command bytes for the digital pot
byte writePot0 = B00010001; // write to pot 0
byte writePot1 = B00010010; // write to pot 1

// values to define how fast we do things
// use a #define for 'pause' so we can compile away the call to delay(0)
#define pause 0               // millisecond pause after each change
const unsigned int step = 1;  // size of the change for the pot


void setup()
{
  pinMode(slaveSelectPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(slaveSelectPin, LOW);
  digitalWrite(ledPin, LOW);
  
  SPI.begin();
}

void loop()
{
  int channel = 0;
  
  // change the resistance on this channel from min to max
  digitalWrite(ledPin, HIGH);
  for (int level = 0; level < 256; level+=step)
  {
    digitalPotWrite(channel, level);
#if pause > 0
    delay(pause);
#endif
  }
  
  // change the resistance on this channel from max to min
  digitalWrite(ledPin, LOW);
  for (int level = 255; level >= 0; level-=step)
  {
    digitalPotWrite(channel, level);
#if pause > 0
    delay(pause);
#endif
  }
}

void digitalPotWrite(int address, int value)
{
  // handle multiple channels
  byte cmd = writePot0;
  if (address != 0)
  {
    cmd = writePot1;
  }

  // send value to the appropriate channel
  SPI.beginTransaction(SPISettings(10000000, MSBFIRST, SPI_MODE0));
  digitalWrite(slaveSelectPin, LOW);
  SPI.transfer(cmd);
  SPI.transfer(value);
  digitalWrite(slaveSelectPin, HIGH);
  SPI.endTransaction();
}
