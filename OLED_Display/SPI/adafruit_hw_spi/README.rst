Testing a small (128x64 pixel) monochrome OLED display with the 
Teensy 3.x microcontroller.  The code here uses hardware SPI
to control the display.

The demo code writes a mix of graphics and text to the screen and
measures how long it takes to redraw the entire screen.  Currently
taking about 4500 microseconds.

It would be faster to use other libraries rather than Adafruit, but
then we would lose the nice graphics.
