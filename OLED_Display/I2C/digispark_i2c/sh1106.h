/*
 * SH1106xLED - Drivers for SH1106 controlled dot matrix OLED/PLED 128x64 displays
 *
 * @created: 2014-08-12
 * @author: Neven Boyanov
 *
 * Copyright (c) 2015 Neven Boyanov, Tinusaur Team. All Rights Reserved.
 * Distributed as open source software under MIT License, see LICENSE.txt file.
 * Please, as a favour, retain the link http://tinusaur.org to The Tinusaur Project.
 *
 * Source code available at: https://bitbucket.org/tinusaur/sh1106xled
 *
 */

#ifndef SH1106_H
#define SH1106_H

// ----------------------------------------------------------------------------

// -----(+)--------------->	// Vcc,	Pin 1 on SH1106 Board
// -----(-)--------------->	// GND,	Pin 2 on SH1106 Board
#ifndef SH1106_SCL
#define SH1106_SCL		PB2	// SCL,	Pin 3 on SH1106 Board
#endif
#ifndef SH1106_SDA
#define SH1106_SDA		PB0	// SDA,	Pin 4 on SH1106 Board
#endif
#ifndef SH1106_SA
#define SH1106_SA		0x78	// Slave address
#endif

// ----------------------------------------------------------------------------

// These functions are used only internally by the library
void sh1106_xfer_start(void);
void sh1106_xfer_stop(void);
void sh1106_send_byte(uint8_t byte);
void sh1106_send_command(uint8_t command);
void sh1106_send_data_start(void);
void sh1106_send_data_stop(void);

// ----------------------------------------------------------------------------

#define sh1106_char(c) sh1106_draw_char(c)
#define sh1106_string(s) sh1106_draw_string(s)
#define sh1106_numdec(n) sh1106_numdec_font6x8(n)
#define sh1106_numdecp(n) sh1106_numdecp_font6x8(n)

// ----------------------------------------------------------------------------

void sh1106_init(void);
void sh1106_setpos(uint8_t x, uint8_t y);
void sh1106_fillp(uint8_t p1, uint8_t p2);
void sh1106_fill(uint8_t p);
void sh1106_fillscreen(uint8_t fill);
void sh1106_draw_char(char ch);
void sh1106_draw_string(char *s);
void sh1106_numdec_font6x8(uint16_t num);
void sh1106_numdecp_font6x8(uint16_t num);
void sh1106_draw_bmp(uint8_t x0, uint8_t y0, uint8_t x1, uint8_t y1, const uint8_t bitmap[]);

// ----------------------------------------------------------------------------

#endif
