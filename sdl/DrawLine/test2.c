#include "SDL.h"

#define MAX_X   512
#define MAX_Y   512

SDL_Window* window = NULL;
SDL_Renderer* renderer = NULL;

void draw(void)
{
    static int offset = 0;

    if (++offset >= 8)
    {
        offset = 0;
    }

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);

    for (int x = offset; x < MAX_X; x += 8)
        SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, x, 0);
    for (int y = offset; y < MAX_Y; y += 8)
        SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, MAX_X, y);
    for (int x = MAX_X-offset; x > 0; x -= 8)
        SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, x, MAX_Y);
    for (int y = MAX_Y-offset; y > 0; y -= 8)
        SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, 0, y);

    SDL_RenderPresent(renderer);
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

                // put vimlac here
                SDL_Delay(50);

                draw();

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
