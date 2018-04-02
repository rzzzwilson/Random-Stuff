#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_SH1106.h"

Adafruit_SH1106 display(4);

void setup()
{                
  Serial.begin(115200);
  delay(40);
  Serial.println("setup");

  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SH1106_SWITCHCAPVCC, 0x3C);

  // setup the display
  display.clearDisplay();  
  display.drawRect(0, 0, SH1106_LCDWIDTH, SH1106_LCDHEIGHT, WHITE);
}

void loop()
{
  static int loop_count = 0;
  
  Serial.println("loop");

  display.invertDisplay(loop_count);
  display.display();
  if (++loop_count > 1)
  {
    loop_count = 0;
  }
  
  for (int x = 1; x < 127; x++)
  {
    int y = 32 - (int) (15.0 * sin(x/5.0));
    
    display.drawPixel(x, y, WHITE);
  }

  // refresh only after drawing sine wave - shows slowness of display.display().
  // this is because the Adafruit_SH1106 library has a built-in buffer and
  // display.display() refreshes the display from the buffer.
  display.display();

  for (int x = 127 - 1; x >= 1; x--)
  {
    int y = 32 - (int) (15.0 * sin(x/5.0));
    
    display.drawPixel(x, y, BLACK);
    display.drawLine(0, 0, SH1106_LCDWIDTH-1, SH1106_LCDHEIGHT-1, WHITE);
    display.drawLine(0, SH1106_LCDHEIGHT-1, SH1106_LCDWIDTH-1, 0, WHITE);
    display.display();
  }
}

void loopX()
{
  Serial.println("loop");
  
  static unsigned int draw_time = 0;
  static unsigned int redraw_count = 0;
  static char buffer[32];

  redraw_count += 1;
  
  // redraw the screen
  unsigned long start = micros();
  sprintf(buffer, "%uus", draw_time);
  printf("buffer: %s\n", buffer);

  display.setCursor(2, 0);
  display.printf("%s", buffer);
  display.display();

  sprintf(buffer, "%06d", redraw_count);
  display.setCursor(90, 0);
  display.print(buffer);
  draw_time = (unsigned) micros() - start;
  
  display.setCursor(2, 4);
  display.print("{{{{");
  display.display();

  delay(1000);
}

