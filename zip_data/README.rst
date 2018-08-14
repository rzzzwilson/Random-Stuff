On the /r/learnpython subreddit I saw a question where someone wanted to store
multiple data files (still image and video) as encoded source that could be
converted back to a still image or video for viewing in a GUI program.  I 
thought that wasn't a good idea as the encode source data would be **HUGE**.
Instead I suggested that the data should be stored as files outside the program.
The OP didn't want this as s/he wanted few files in a program that would be
distributed to others.  I also suggested that the data files could be kept in
a ZIP file and read from there.  I don't know if the OP used that approach, but
the code here is a proof-of-concept exercise of keeping multiple data files
(text, still images, etc) in a zip file.

Various steps in the exercise:

* simple "read data from the ZIP" example (zip_data1.py),
* try using a password on the ZIP file (zip_data2.py), and
* allow user to "write back" to the ZIP file (zip_data3.py).

The `Makefile` allows you to:

* `make build`
