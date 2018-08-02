#include <SDL.h>

#define MAX_X       512
#define MAX_Y       512

#define MAX_LINES   2048

typedef struct DrawLine
{
   int x1;
   int y1;
   int x2;
   int y2;
} DrawLine;

static SDL_Window* window = NULL;
static SDL_Renderer* renderer = NULL;

static DrawLine lines[MAX_LINES];
static int num_lines = 0;


void draw(int x1, int y1, int x2, int y2)
{
    DrawLine *p = &lines[num_lines++];

    p->x1 = x1;
    p->y1 = y1;
    p->x2 = x2;
    p->y2 = y2;
}

void draw_displaylist(void)
{
    DrawLine *p = lines;

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);

    for (int i = 0; i < num_lines; ++i)
    {
        SDL_RenderDrawLine(renderer, p->x1, p->y1, p->x2, p->y2);
        ++p;
    }

    SDL_RenderPresent(renderer);
}


void clear_displaylist(void)
{
    num_lines = 0;
}


static void make_test_displaylist(void)
{
    static int offset = 0;
    int i = 0;

    if (++offset >= 8)
    {
        offset = 0;
    }

    clear_displaylist();

    for (int x = offset; x < MAX_X; x += 8)
        draw(MAX_X/2, MAX_Y/2, x, 0);
    for (int y = offset; y < MAX_Y; y += 8)
        draw(MAX_X/2, MAX_Y/2, MAX_X, y);
    for (int x = MAX_X-offset; x > 0; x -= 8)
        draw(MAX_X/2, MAX_Y/2, x, MAX_Y);
    for (int y = MAX_Y-offset; y > 0; y -= 8)
        draw(MAX_X/2, MAX_Y/2, 0, y);
}


int main(int argc, char* argv[])
{
    if (SDL_Init(SDL_INIT_VIDEO) == 0)
    {
        if (SDL_CreateWindowAndRenderer(MAX_X, MAX_Y, 0, &window, &renderer) == 0)
        {
            SDL_bool done = SDL_FALSE;

            while (!done)
            {
                SDL_Event event;

                // run vimlac code here
                SDL_Delay(20);

                make_test_displaylist();
                draw_displaylist();

                while (SDL_PollEvent(&event))
                {
                    if (event.type == SDL_QUIT)
                    {
                        done = SDL_TRUE;
                    }
                }
            }
        }

        if (renderer)
        {
            SDL_DestroyRenderer(renderer);
        }
        if (window)
        {
            SDL_DestroyWindow(window);
        }
    }

    SDL_Quit();

    return 0;
}
