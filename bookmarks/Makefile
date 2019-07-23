# A makefile to automate certain phases of testing.

clean:
	rm -f xyzzy.html

html:
	python3 bookmarks2chrome.py test.data xyzzy.html

bmark:
	python3 chrome2bookmarks.py test.data test.html
