/*
 * Using an OLED display, 128x64 (or is it 132x64, 130x64, ...)
 * Set SDA to P0, SCL to P2
 */

#include <DigisparkOLED.h>

// set IMAGE to
//   0   example image
//   1   the Digistump logo
#define IMAGE   1

#if IMAGE == 0
  #include "img0_128x64c1.h"
#endif
#if IMAGE == 1
  #include "digistump_128x64c1.h"
#endif


void setup()
{
  oled.begin();
}

void loop()
{
  oled.fill(0xFF); //fill screen with color
  delay(1000);
  oled.clear(); //all black
  delay(1000);
  
  //usage: oled.setCursor(X IN PIXELS, Y IN ROWS OF 8 PIXELS STARTING WITH 0);
  oled.setCursor(0, 0); //top left
  oled.setFont(FONT8X16);
  oled.print(F("DIGISTUMP")); //wrap strings in F() to save RAM!
  oled.setFont(FONT6X8);
  oled.print(F(" OLED!"));
  oled.setCursor(0, 2); //two rows down because the 8x16 font takes two rows of 8
  oled.println(F("test")); //println will move the cursor 8 or 16 pixels down (based on the font) and back to X=0
  oled.print(F("test test test test test")); //lines auto wrap
  
  delay(3000);
  
#if IMAGE == 0
  //usage oled.bitmap(START X IN PIXELS, START Y IN ROWS OF 8 PIXELS, END X IN PIXELS, END Y IN ROWS OF 8 PIXELS, IMAGE ARRAY);
  oled.bitmap(0, 0, 128, 8, img0_128x64c1);
  delay(3000);
#endif
#if IMAGE == 1
  oled.bitmap(0, 0, 128, 8, digistumplogo);
  delay(3000);
#endif
}
