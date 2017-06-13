This is an old version of a "memory allocation check" program
that I wrote *years* ago.  It used to track down those nasty memory
allocation errors like:

* not freeing memory before program exit
* freeing memory twice
* memory overruns (accessing past the end of the allocated block)
* memory underruns (accessing before the start of the block)
* changing the contents of a block after freeing it

It shows one way of debugging memory malloc/free problems in the 
C programming language.  It does this by (ab)using the preprocessor
to replace all memory function calls with the appropriate function
in the memcheck library.

Another way uses similar checking code but gets control **without**
hijacking the malloc/free calls in the source code, but uses a DLL/SO
library approach to capture malloc/free calls before passing them to
the normal library code.  I've seen this approach called
`shimming <https://en.wikipedia.org/wiki/Shim_\(computing\)>`_.
