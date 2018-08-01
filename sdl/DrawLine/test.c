#include "SDL.h"

#define MAX_X   512
#define MAX_Y   512

int main(int argc, char* argv[])
{
    if (SDL_Init(SDL_INIT_VIDEO) == 0)
    {
        SDL_Window* window = NULL;
        SDL_Renderer* renderer = NULL;

        if (SDL_CreateWindowAndRenderer(MAX_X, MAX_Y, 0, &window, &renderer) == 0)
        {
            SDL_bool done = SDL_FALSE;
            int offset = 0;

            while (!done)
            {
                SDL_Event event;

                SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
                SDL_RenderClear(renderer);
                SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);

                for (int x = offset; x < MAX_X; x += 8)
                    SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, x, 0);
                for (int y = offset; y < MAX_Y; y += 8)
                    SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, MAX_X-1, y);
                for (int x = MAX_X-offset; x > 0; x -= 8)
                    SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, x, MAX_Y-1);
                for (int y = MAX_Y-offset; y > 0; y -= 8)
                    SDL_RenderDrawLine(renderer, MAX_X/2, MAX_Y/2, 0, y);

/*
                SDL_RenderDrawLine(renderer, 320, 200, 300, 240);
                SDL_RenderDrawLine(renderer, 300, 240, 340, 240);
                SDL_RenderDrawLine(renderer, 340, 240, 320, 200);
*/
                SDL_RenderPresent(renderer);

                if (++offset >= 8)
                {
                    offset = 0;
                }

                SDL_Delay(25);

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
