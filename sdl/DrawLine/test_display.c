/*
 * Code to test the display_*.c code.
 */

#include <SDL.h>
#include "vimlac.h"
#include "display.h"


#define MAX_X   512
#define MAX_Y   512


static void make_test_displaylist(void)
{
    static int offset = 0;
    int i = 0;

    if (++offset >= 8)
    {
        offset = 0;
    }

    display_reset();

    for (int x = offset; x < MAX_X; x += 8)
        display_draw(MAX_X/2, MAX_Y/2, x, 0);
    for (int y = offset; y < MAX_Y; y += 8)
        display_draw(MAX_X/2, MAX_Y/2, MAX_X, y);
    for (int x = MAX_X-offset; x > 0; x -= 8)
        display_draw(MAX_X/2, MAX_Y/2, x, MAX_Y);
    for (int y = MAX_Y-offset; y > 0; y -= 8)
        display_draw(MAX_X/2, MAX_Y/2, 0, y);
}


int main(void)
{
    if (display_init())
    {
        static int offset = 0;
        int i = 0;
        bool done = false;
        SDL_Event event;

        while (!done)
        {    
            if (++offset >= 8)
            {
                offset = 0;
            }
        
            display_reset();
        
            for (int x = offset; x < MAX_X; x += 8)
                display_draw(MAX_X/2, MAX_Y/2, x, 0);
            for (int y = offset; y < MAX_Y; y += 8)
                display_draw(MAX_X/2, MAX_Y/2, MAX_X, y);
            for (int x = MAX_X-offset; x > 0; x -= 8)
                display_draw(MAX_X/2, MAX_Y/2, x, MAX_Y);
            for (int y = MAX_Y-offset; y > 0; y -= 8)
                display_draw(MAX_X/2, MAX_Y/2, 0, y);
    
            display_write();
    
            while (SDL_PollEvent(&event))
            {
                if (event.type == SDL_QUIT)
                {
                    done = true;
                }
            }
        }

        display_close();
    }
}
