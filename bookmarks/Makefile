# A makefile to automate certain phases of testing.

clean:
	echo "Nothing done..."

test:
	rm -f test.html
	python3 bookmarks2chrome.py test.data test.html

html:
	rm -f bookmarks_3_22_19.html
	python3 bookmarks2chrome.py bookmarks_3_22_19.data bookmarks_3_22_19.html
