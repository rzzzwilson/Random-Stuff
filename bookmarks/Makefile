# A makefile to automate certain phases of testing.

clean:
	echo "Nothing done..."

test:
	rm -f test.html
	python3 bookmarks2chrome.py test.data test.html

data:
	rm -f bookmarks_11_20_19.data
	python3 html2data.py bookmarks_11_20_19.html.ORIG bookmarks_11_20_19.data

html:
	rm -f bookmarks_11_20_19.html
	python3 data2html.py bookmarks_11_20_19.data bookmarks_11_20_19.html
