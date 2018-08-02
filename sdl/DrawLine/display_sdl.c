/*
 * The vimlac display code using SDL.
 */


#include <SDL.h>
#include "display.h"


#define MAX_X       512
#define MAX_Y       512
#define MAX_LINES   2048

// struct to hold info for one line drawn from (x1,y1) to (x2,y2)
typedef struct DrawLine
{
   int x1;
   int y1;
   int x2;
   int y2;
} DrawLine;

// display state variables
static SDL_Window* window = NULL;       // 
static SDL_Renderer* renderer = NULL;   // 

static DrawLine DisplayList[MAX_LINES]; // 
static int NumLines = 0;                // 
static bool DisplayDirty = false;       // 


void display_draw(int x1, int y1, int x2, int y2)
{
    DrawLine *p = &DisplayList[NumLines++];

    p->x1 = x1;
    p->y1 = y1;
    p->x2 = x2;
    p->y2 = y2;

    DisplayDirty = true;
}


void display_write(void)
{
    DrawLine *p = DisplayList;    // get pointer to first struct in DisplayList

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);

    for (int i = 0; i < NumLines; ++i)
    {
        SDL_RenderDrawLine(renderer, p->x1, p->y1, p->x2, p->y2);
        ++p;
    }

    SDL_RenderPresent(renderer);

    DisplayDirty = false;
}


void display_reset(void)
{
    NumLines = 0;
    DisplayDirty = true;
}


bool display_init()
{
    if (SDL_Init(SDL_INIT_VIDEO) != 0)
        return false;

    if (SDL_CreateWindowAndRenderer(MAX_X, MAX_Y, 0, &window, &renderer) != 0)
    {
        if (renderer)
            SDL_DestroyRenderer(renderer);
        if (window)
            SDL_DestroyWindow(window);
        return false;
    }

    display_reset();

    return true;
}


bool display_dirty(void)
{
    return DisplayDirty;
}


void display_close(void)
{
    if (renderer)
        SDL_DestroyRenderer(renderer);
    if (window)
        SDL_DestroyWindow(window);

    SDL_Quit();
}
