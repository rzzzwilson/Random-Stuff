#include <stdlib.h>
#include "font6x8.h"
#include "sh1106.h"

#define REDRAW_SCREEN   0

char buffer[32];

void setup()
{
  delay(40);
  sh1106_init();
#if !REDRAW_SCREEN
  sh1106_fillscreen(0x00);
  textxy(0, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  textxy(0, 2, "The time has come,");
  textxy(0, 3, "the Walrus said, to");
  textxy(0, 4, "talk of many things.");
  textxy(0, 6, "        Lewis Carroll");
  textxy(0, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif
}

//void textxy(char* s)
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
#endif
  sprintf(buffer, "%uus", draw_time);
  sh1106_setpos(0, 0);
  sh1106_draw_string(buffer);
  sprintf(buffer, "%06d", redraw_count);
  sh1106_setpos(90, 0);
  sh1106_draw_string(buffer);
#if REDRAW_SCREEN
  textxy(0, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  textxy(0, 2, "The time has come,");
  textxy(0, 3, "the Walrus said, to");
  textxy(0, 4, "talk of many things.");
  textxy(0, 6, "        Lewis Carroll");
  textxy(0, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif
  draw_time = (unsigned) micros() - start;
}
