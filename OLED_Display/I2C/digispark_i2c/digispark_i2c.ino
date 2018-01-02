#include <stdlib.h> //Code library can be downloaded below
#include "font6x8.h" //Code library can be downloaded below
#include "font8x16.h" // Code library can be downloaded below
#include "ssd1306xled.h" //Code library can be downloaded below
#include "ssd1306xled8x16.h" //Code library can be downloaded below

char buffH[10];
char buffT[10];
 
void setup()
{
  delay(40);
  ssd1306_init();
}
 
void texto(char* s)
{
  ssd1306_string_font6x8(s);
}

void textoG(int pos_x, int pos_y, char* sG)
{
  ssd1306_char_f8x16(pos_x, pos_y, sG);
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
  ssd1306_fillscreen(0x00);
  pos(0, 0);
  dtostrf(draw_time, 2, 0, buffH);
  textoG(0, 0, buffH);
  dtostrf(redraw_count, 5, 0, buffT);
  textoG(0, 2, buffT);
  textoG(0, 4, "The time has come, the Walrus said");
#if 0
  pos(0, 5);
  textoG(0, 2, " Temperature(C)");
  pos(0, 7);
  texto(" www.14core.com");
  textoG(0,0," Weather Station");
  textoG(87,2,buffH);
  textoG(87,4,buffT);
  //delay(3000);
#endif
  draw_time = micros() - start;
}
