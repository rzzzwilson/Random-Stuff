/*
 * SH1106 - Drive a SH1106 controlled OLED 128x64 display
 */

#include <stdlib.h>
#include <avr/io.h>

#include <avr/pgmspace.h>

#include "sh1106.h"
#include "font6x8.h"

#include "num2str.h"

// Convenience definitions for PORTB
#define DIGITAL_WRITE_HIGH(PORT) PORTB |= (1 << PORT)
#define DIGITAL_WRITE_LOW(PORT) PORTB &= ~(1 << PORT)

const uint8_t sh1106_init_sequence [] PROGMEM = {	// Initialization Sequence
	0xAE,			    // Display OFF (sleep mode)
	0x20, 0b00,		// Set Memory Addressing Mode
					      // 00=Horizontal Addressing Mode; 01=Vertical Addressing Mode;
					      // 10=Page Addressing Mode (RESET); 11=Invalid
	0xB0,			    // Set Page Start Address for Page Addressing Mode, 0-7
	0xC8,			    // Set COM Output Scan Direction
	0x00,			    // ---set low column address
	0x10,			    // ---set high column address
	0x40,			    // --set start line address
	0x81, 0x3F,		// Set contrast control register
	0xA1,			    // Set Segment Re-map. A0=address mapped; A1=address 127 mapped. 
	0xA6,			    // Set display mode. A6=Normal; A7=Inverse
	0xA8, 0x3F,		// Set multiplex ratio(1 to 64)
	0xA4,			    // Output RAM to Display
					      // 0xA4=Output follows RAM content; 0xA5,Output ignores RAM content
	0xD3, 0x00,		// Set display offset. 00 = no offset
	0xD5,	        // --set display clock divide ratio/oscillator frequency
	0xF0,			    // --set divide ratio
	0xD9, 0x22,		// Set pre-charge period
	0xDA, 0x12,		// Set com pins hardware configuration		
	0xDB,			    // --set vcomh
	0x20,			    // 0x20,0.77xVcc
	0x8D, 0x14,		// Set DC-DC enable
	0xAF			    // Display ON in normal mode
	
};

// These function should become separate library for handling I2C simplified output.

void sh1106_xfer_start(void)
{
	DIGITAL_WRITE_HIGH(SH1106_SCL);	  // Set to HIGH
	DIGITAL_WRITE_HIGH(SH1106_SDA);	  // Set to HIGH
	DIGITAL_WRITE_LOW(SH1106_SDA);		// Set to LOW
	DIGITAL_WRITE_LOW(SH1106_SCL);		// Set to LOW
}

void sh1106_xfer_stop(void)
{
	DIGITAL_WRITE_LOW(SH1106_SCL);		// Set to LOW
	DIGITAL_WRITE_LOW(SH1106_SDA);		// Set to LOW
	DIGITAL_WRITE_HIGH(SH1106_SCL);	  // Set to HIGH
	DIGITAL_WRITE_HIGH(SH1106_SDA);	  // Set to HIGH
}

void sh1106_send_byte(uint8_t byte)
{
	uint8_t i;
	for (i = 0; i < 8; i++)
	{
		if ((byte << i) & 0x80)
			DIGITAL_WRITE_HIGH(SH1106_SDA);
		else
			DIGITAL_WRITE_LOW(SH1106_SDA);
		
		DIGITAL_WRITE_HIGH(SH1106_SCL);
		DIGITAL_WRITE_LOW(SH1106_SCL);
	}
	DIGITAL_WRITE_HIGH(SH1106_SDA);
	DIGITAL_WRITE_HIGH(SH1106_SCL);
	DIGITAL_WRITE_LOW(SH1106_SCL);
}

void sh1106_send_command_start(void)
{
	sh1106_xfer_start();
	sh1106_send_byte(SH1106_SA);  // Slave address, SA0=0
	sh1106_send_byte(0x00);	      // write command
}

void sh1106_send_command_stop(void)
{
	sh1106_xfer_stop();
}

void sh1106_send_command(uint8_t command)
{
	sh1106_send_command_start();
	sh1106_send_byte(command);
	sh1106_send_command_stop();
}

void sh1106_send_data_start(void)
{
	sh1106_xfer_start();
	sh1106_send_byte(SH1106_SA);
	sh1106_send_byte(0x40);	//write data
}

void sh1106_send_data_stop(void)
{
	sh1106_xfer_stop();
}

void sh1106_init(void)
{
	DDRB |= (1 << SH1106_SDA);	// Set port as output
	DDRB |= (1 << SH1106_SCL);	// Set port as output
	
	for (uint8_t i = 0; i < sizeof (sh1106_init_sequence); i++)
	{
		sh1106_send_command(pgm_read_byte(&sh1106_init_sequence[i]));
	}
}

void sh1106_setpos(uint8_t x, uint8_t y)
{
	sh1106_send_command_start();
	sh1106_send_byte(0xb0 + y);
	sh1106_send_byte(((x & 0xf0) >> 4) | 0x10); // | 0x10
  sh1106_send_byte((x & 0x0f));               // | 0x01
	sh1106_send_command_stop();
}

void sh1106_fillp(uint8_t p1, uint8_t p2)
{
	sh1106_setpos(0, 0);
	sh1106_send_data_start();
	for (uint16_t i = 0; i < 128 * 8 / 2; i++)
	{
		sh1106_send_byte(p1);
		sh1106_send_byte(p2);
	}
	sh1106_send_data_stop();
}

void sh1106_fill(uint8_t p)
{
	sh1106_fillp(p, p);
}

void sh1106_fillscreen(uint8_t fill)
{
	for (uint8_t m = 0; m < 8; m++)
	{
		sh1106_send_command(0xb0 + m);	// page0 - page1
		sh1106_send_command(0x00);		  // low column start address
		sh1106_send_command(0x10);		  // high column start address
		sh1106_send_data_start();
		for (uint8_t n = 0; n < 128; n++)
		{
			sh1106_send_byte(fill);
		}
		sh1106_send_data_stop();
	}
}

void sh1106_draw_char(char ch)
{
	uint8_t c = ch - 32;
	sh1106_send_data_start();
	for (uint8_t i = 0; i < 6; i++)
	{
		sh1106_send_byte(pgm_read_byte(&sh1106xled_font6x8[c * 6 + i]));
	}
	sh1106_send_data_stop();
}

void sh1106_draw_string(char *s)
{
	while (*s)
	{
		sh1106_draw_char(*s++);
	}
}

char sh1106_numdec_buffer[USINT2DECASCII_MAX_DIGITS + 1];

void sh1106_numdec_font6x8(uint16_t num)
{
	sh1106_numdec_buffer[USINT2DECASCII_MAX_DIGITS] = '\0';   // Terminate the string.
	uint8_t digits = usint2decascii(num, sh1106_numdec_buffer);
	sh1106_draw_string(sh1106_numdec_buffer + digits);
}

void sh1106_numdecp_font6x8(uint16_t num)
{
	sh1106_numdec_buffer[USINT2DECASCII_MAX_DIGITS] = '\0';   // Terminate the string.
	usint2decascii(num, sh1106_numdec_buffer);
	sh1106_draw_string(sh1106_numdec_buffer);
}

void sh1106_draw_bmp(uint8_t x0, uint8_t y0, uint8_t x1, uint8_t y1, const uint8_t bitmap[])
{
	uint16_t j = 0;
	uint8_t y;
  
	if (y1 % 8 == 0)
	  y = y1 / 8;
	else
	  y = y1 / 8 + 1;
   
	for (y = y0; y < y1; y++)
	{
		sh1106_setpos(x0, y);
		sh1106_send_data_start();
		for (uint8_t x = x0; x < x1; x++)
		{
			sh1106_send_byte(pgm_read_byte(&bitmap[j++]));
		}
		sh1106_send_data_stop();
	}
}

