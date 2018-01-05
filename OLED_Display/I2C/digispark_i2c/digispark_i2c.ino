#include <stdlib.h>
#include "font6x8.h"
#include "ssd1306xled.h"

char buffH[10];
char buffT[10];

//#define TRY

void setup()
{
  delay(40);
  ssd1306_init();
#ifndef TRY
  ssd1306_fillscreen(0x00);
  texto(0, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  texto(0, 2, "The time has come");
  texto(0, 3, "the Walrus said, to");
  texto(0, 4, "talk of many things.");
  texto(0, 6, "        Lewis Carroll");
  texto(0, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif
}

void int2str(int i, char *buff)
{
  sprintf(buff, "%d", i);
}

//void texto(char* s)
void texto(int pos_x, int pos_y, char* s)
{
  ssd1306_setpos(pos_x, pos_y);
  ssd1306_string_font6x8(s);
}

void pos(uint8_t x, uint8_t y)
{
  ssd1306_setpos(x, y);
}

void DisMan()
{
  ssd1306_fillscreen(0x00);
//  delay(100);
}
 
void loop()
{
  static unsigned int draw_time = 0;
  static unsigned int redraw_count = 0;

  redraw_count += 1;
  
  // redraw the screen
  unsigned long start = micros();
#ifdef TRY
  ssd1306_fillscreen(0x00);
#endif
  sprintf(buffH, "%uus", draw_time);
  texto(0, 0, buffH);
  dtostrf(redraw_count, 5, 0, buffT);
  sprintf(buffT, "%06d", redraw_count);
  texto(90, 0, buffT);
#ifdef TRY
  texto(0, 1, "{{{{{{{{{{{{{{{{{{{{{{");
  texto(0, 2, "The time has come,");
  texto(0, 3, "the Walrus said, to");
  texto(0, 4, "talk of many things.");
  texto(0, 6, "        Lewis Carroll");
  texto(0, 7, "{{{{{{{{{{{{{{{{{{{{{{");
#endif
  draw_time = (unsigned) micros() - start;
}
