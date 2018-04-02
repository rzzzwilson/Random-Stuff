#include "sh1106.h"

// Setting to '0' forces a full screen redraw each time in loop().
// A '1' value draws the screen once with partial updates - faster!
// But note the corruption with value set to '1'.
#define REDRAW_SCREEN   1

char buffer[32];

void setup()
{
  delay(40);
  sh1106_init();
  sh1106_fillscreen(0x00);
}

//const uint8_t bmp[] PROGMEM = {0xff, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0xff};
const uint8_t bmp[] PROGMEM = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};


void loop()
{
  static unsigned int draw_time = 0;
  static unsigned int redraw_count = 0;

  redraw_count += 1;
  
  // redraw the screen
  unsigned long start = micros();
  sprintf(buffer, "%uus", draw_time);
  sh1106_setpos(2, 0);
  sh1106_draw_string(buffer);
  sprintf(buffer, "%06d", redraw_count);
  sh1106_setpos(90, 0);
  sh1106_draw_string(buffer);
  draw_time = (unsigned) micros() - start;

  sh1106_setpos(2, 6);
  sh1106_draw_bmp(24, 24, 32, 32, bmp);
  
  sh1106_setpos(2, 4);
  sh1106_draw_string("{{{{");
//  sh1106_draw_string("\\\\\\\\");
  
  delay(1000);
}


