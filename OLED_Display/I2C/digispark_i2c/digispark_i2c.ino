#include <stdlib.h>
#include "font6x8.h"
#include "sh1106.h"

// Setting to '0' forces a full screen redraw each time in loop().
// A '1' value draws the screen once with partial updates - faster!
// But note the corruption with value set to '1'.
#define REDRAW_SCREEN   0

#define PIN_LED         1   // pin 1 has the LED
#define PIN_AUDIO       5   // use pin 5 for audio sensor

char buffer[32];

void setup()
{
  Serial.begin(115200);
  Serial.write("setup() finished\n");
  delay(40);
  sh1106_init();
#if !REDRAW_SCREEN
  sh1106_fillscreen(0x00);
  textxy(1, 0, "                      ");
  textxy(1, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  textxy(1, 2, "The time has come,    ");
  textxy(1, 3, "the Walrus said, to   ");
  textxy(1, 4, "talk of many things.  ");
  textxy(1, 5, "                      ");
  textxy(1, 6, "        Lewis Carroll ");
  textxy(1, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif

  pinMode(PIN_AUDIO, INPUT);
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
  Serial.write("setup() finished\n");
}

void textxy(int pos_x, int pos_y, char* s)
{
  sh1106_setpos(pos_x, pos_y);
  sh1106_draw_string(s);
}

void loop()
{
  static unsigned int draw_time = 0;
  static unsigned int redraw_count = 0;

  redraw_count += 1;
  
  // redraw the screen
  unsigned long start = micros();
#if REDRAW_SCREEN
  sh1106_fillscreen(0x00);
  textxy(1, 0, "                      ");
  textxy(1, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  textxy(1, 2, "The time has come,    ");
  textxy(1, 3, "the Walrus said, to   ");
  textxy(1, 4, "talk of many things.  ");
  textxy(1, 5, "                      ");
  textxy(1, 6, "        Lewis Carroll ");
  textxy(1, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif
  sprintf(buffer, "%uus", draw_time);
  sh1106_setpos(0, 0);
  sh1106_draw_string(buffer);
  sprintf(buffer, "%06d", redraw_count);
  sh1106_setpos(90, 0);
  sh1106_draw_string(buffer);
  draw_time = (unsigned) micros() - start;

  delay(1000);

  int aud_value = digitalRead(PIN_AUDIO);
  if (aud_value > 100)
  {
    Serial.write("Sound!\n");
    digitalWrite(PIN_LED, HIGH);
    delay(1000);
    digitalWrite(PIN_LED, LOW);
  }
}
