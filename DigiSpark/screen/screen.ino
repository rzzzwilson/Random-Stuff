/****************************************************
 * See if the Digispark can drive a 320x240 TFT display via SPI.
 ****************************************************/

//#include <SPI.h>
#include <Adafruit_ILI9341.h>
#include <Adafruit_GFX.h>
//#include <FreeSansBold24pt7b.h>

#define SCREEN_WIDTH    320
#define SCREEN_HEIGHT   240

// The display also uses hardware SPI, plus #4 & #5
#define TFT_RST     3
#define TFT_DC      4
#define TFT_CS      5
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_RST);  

// display constants - offsets, colours, etc
//#define FONT_FREQ           (&FreeSansBold24pt7b) // font for frequency display

// various colours
#define ILI9341_LIGHTGREY   0xC618      /* 192, 192, 192 */
#define ILI9341_DARKGREY    0x7BEF      /* 128, 128, 128 */

  // write message to the TFT screen
//  tft.setFont(FONT_ABORT);
//  tft.fillRect(0, 0, tft.width(), tft.height(), ABORT_BG);
//  tft.setTextColor(ABORT_FG);
//  tft.setCursor(5, offset_y);

//-----------------------------------------------
// Setup the whole shebang.
//-----------------------------------------------

void setup(void)
{
  Serial.begin(115200);
  Serial.println("DigiSpark test");

  // start handling devices
  //SPI.begin();
  
  //tft.begin();
  //tft.setRotation(1);
}

//-----------------------------------------------
// Arduino main loop function.
//-----------------------------------------------
void loop()
{
}
