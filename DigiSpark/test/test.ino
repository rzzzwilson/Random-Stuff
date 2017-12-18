/**************************************************************
 * DigiSpark demo - send Morse code through the builtin LED,
 *                  also sound morse if buzzer connected.
 **************************************************************/

#include <string.h>

// DigiSpark model A, builtin LED is pin 1
#define LED_BUILTIN 1

// connect piezo buzzer to this pin
#define PIEZO_PIN   0

// time for one 'dot' in milliseconds
#define DOT_TIME    100   // slightly faster than 10wpm

// halfcycle time for morse buzzer
#define HALF_CYCLE  1     // length of one halfcycle, milliseconds

// struct to map single char to morse dot/dash string
typedef struct CHAR_DATA {
                           char ch;
                           char *dot_dash;
                         } MorseData;

/*
 * Routine to sound morse buzzer for given period
 */

void buzzer(int msec)
{
  unsigned long end_millis = millis() + msec;

  while (millis() < end_millis)
  {
    // do one cycle
    digitalWrite(PIEZO_PIN, HIGH);
    delay(HALF_CYCLE);
    digitalWrite(PIEZO_PIN, LOW);
    delay(HALF_CYCLE);
  }
}

/*
 * Routines to send a dot/dash/spacer
 */
 
void dot(void)
{
  digitalWrite(LED_BUILTIN, HIGH);
  buzzer(DOT_TIME); // a dot is one dot time
  digitalWrite(LED_BUILTIN, LOW);
}

void dash(void)
{
  digitalWrite(LED_BUILTIN, HIGH);
  buzzer(3*DOT_TIME); // a dash is three dot times
  digitalWrite(LED_BUILTIN, LOW);
}

void dot_space(void)
{
  digitalWrite(LED_BUILTIN, LOW); // just in case
  delay(DOT_TIME);
}

/*
 * Routine to send one morse character.
 */

// table to map a character to its morse code equivalent
MorseData morse_table[] = {
                           {' ', " "},
                           {'a', ".-"},   {'b', "-..."}, {'c', "-.-."}, {'d', "-.."},
                           {'e', "."},    {'f', "..-."}, {'g', "--."},  {'h', "...."},
                           {'i', ".."},   {'j', ".---"}, {'k', "-.-"},  {'l', ".-.."},
                           {'m', "--"},   {'n', "-."},   {'o', "---"},  {'p', ".--."},
                           {'q', "--.-"}, {'r', ".-."},  {'s', "..."},  {'t', "-"},
                           {'u', "..-"},  {'v', "...-"}, {'w', ".--"},  {'x', "-..-"},
                           {'y', "-.--"}, {'z', "--.."},
                          };

// number of entries in MorseData
#define NumMorseChars   (sizeof(morse_table) / sizeof(morse_table[0]))

void send_morse_char(char *dot_dash)
{
  for (char *p = dot_dash; *p; ++p)
  {
    switch (*p)
    {
      case ' ':
        dot_space();  // 7 spaces between words, already waited 3
        dot_space();
        dot_space();
        dot_space();
        break;
      case '.':
        dot();
        dot_space();
        break;
      case '-':
        dash();
        dot_space();
        break;
    }
  }
  
  dot_space();   // 3 spaces after complete letter, already waited 1
  dot_space();
}

void send_morse(char ch)
{
  for (int i = 0; i < NumMorseChars; ++i)
  {
    if (morse_table[i].ch == ch)
    {
      send_morse_char(morse_table[i].dot_dash);
      return;
    }
  }
}

// called once to initialize the system
void setup()
{                
  // initialize the LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop routine is called continuously
void loop()
{
  char *msg = "morse code";  // display message
//  char *msg = "paris";      // used for speed tests

  for (char *p = msg; *p; ++p)
  {
    send_morse(*p);
  }
  
  dot_space();  // 7 dot spaces after the string
  dot_space();
  dot_space();
  dot_space();
  dot_space();
  dot_space();
  dot_space();
}

