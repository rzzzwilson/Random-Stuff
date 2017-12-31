#include <SPI.h>
#include "Adafruit_SH1106.h"

/*
 * Drive the 128x32 OLED display using SH1106 controller
 * Uses hardware SPI.
 */
 
// the connecting pins
#define OLED_MOSI     11
#define OLED_CLK      13
#define OLED_DC       9
#define OLED_CS       8
#define OLED_RESET    10

// invert after this number of frames
#define INVERT_COUNT  200

// define text attributes
#define TEXT_TOP      18
#define TEXT_LEFT     5
#define TEXT_HEIGHT   8

// use hardware SPI
Adafruit_SH1106 display(OLED_DC, OLED_RESET, OLED_CS);

void setup(void)
{                
  Serial.begin(115200);
  Serial.print("Adafruit library using hardware SPI\n");
  display.begin(SH1106_SWITCHCAPVCC);
  display.display();
  delay(2000);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
}

void loop(void)
{
  static unsigned long delta = 0;
  static bool inverted = false;
  static long invert_count = 0;
  static long screen_count = 0;
  unsigned long start = micros();

  if (++screen_count > 1000000)
    screen_count = 0;
    
  display.clearDisplay();

  if (--invert_count <= 0)
  {
    display.invertDisplay(inverted);
    inverted = !inverted;
    invert_count = INVERT_COUNT;
    if (delta > 0)
    {
      Serial.print(delta);
      Serial.print(" microseconds\n");
    }
  }

  display.setCursor(0, 0);
  display.printf("%5dus", delta);
  display.setCursor(86, 0);
  display.printf("%07d", screen_count);
  
//  display.print("us    Adafruit HW");
//  display.print("123456789012345678901\n\n");
  display.setCursor(TEXT_LEFT, TEXT_TOP);
  display.print("The time has come,");
  display.setCursor(TEXT_LEFT, TEXT_TOP+TEXT_HEIGHT);
  display.print("the Walrus said, to");
  display.setCursor(TEXT_LEFT, TEXT_TOP+TEXT_HEIGHT*2);
  display.print("talk of many things.");
  display.setCursor(TEXT_LEFT, TEXT_TOP+TEXT_HEIGHT*4);
  display.print("       Lewis Carroll");

  display.drawFastHLine(TEXT_LEFT/2-1, TEXT_TOP-TEXT_HEIGHT/2, SH1106_LCDWIDTH-2, 1);
  display.drawFastHLine(TEXT_LEFT/2-1, SH1106_LCDHEIGHT-2, SH1106_LCDWIDTH-2, 1);
  display.drawFastVLine(TEXT_LEFT/2-1, TEXT_TOP-4, 48, 1);
  display.drawFastVLine(SH1106_LCDWIDTH-TEXT_LEFT/2, TEXT_TOP-4, 48, 1);
  
  display.display();

  delta = micros() - start;
}
