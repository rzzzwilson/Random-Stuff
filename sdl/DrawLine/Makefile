test3: test3.c
	gcc test3.c -o test3 -I /usr/local/include/SDL2/ -l SDL2-2.0.0

test2: test2.c
	gcc test2.c -o test2 -I /usr/local/include/SDL2/ -l SDL2-2.0.0

test: test.c
	gcc test.c -o test -I /usr/local/include/SDL2/ -l SDL2-2.0.0

test_display:  
	gcc -o test_display test_display.c display_sdl.c -I /usr/local/include/SDL2 -l SDL2-2.0.0 -l SDL2-2.0.0

clean:
	rm -f *.o test test2 test3 test_display
