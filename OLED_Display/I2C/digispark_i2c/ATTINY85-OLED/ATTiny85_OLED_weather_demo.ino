#include "font6x8.h" //Code library can be downloaded below
#include "font8x16.h" // Code library can be downloaded below
//#include <num2str.h>
#include "ssd1306xled.h" //Code library can be downloaded below
#include "ssd1306xled8x16.h" //Code library can be downloaded below
#include <stdlib.h> //Code library can be downloaded below

float h=0;
float t=0;
char buffH[6];
char buffT[6];

void setup()
{
DelayMs(40);
SSD1306.ssd1306_init();
}

void texto(char* s) {SSD1306.ssd1306_string_font6x8(s);}
void textoG(int pos_x, int pos_y, char* sG) {SSD1306.ssd1306_char_f8x16(pos_x, pos_y, sG);}
void pos(uint8_t x, uint8_t y){SSD1306.ssd1306_setpos(x, y);}
void DisMan(){uint8_t p = 0xff; for (uint8_t i = 0; i < 4; i++){p = (p >> i); SSD1306.ssd1306_fillscreen(~p); DelayMs(100);}SSD1306.ssd1306_fillscreen(0x00);}

void loop() {

h=23;
t=23;
dtostrf(h, 4, 2, buffH);
dtostrf(t, 4, 2, buffT);

DisMan();
pos(0, 3);
texto("Humidity(%)");
pos(0, 5);
texto("Temperature(C)");
pos(0, 7);
texto(" www.14core.com");
textoG(0,0,"Weather Station");
textoG(87,2,buffH);
textoG(87,4,buffT);
DelayMs(3000);
}
