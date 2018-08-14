TEST1_FILE=test1.zip

clean:
	rm -f *.zip

build:
	rm -f *.zip
	zip -q -j add $(TEST1_FILE) data_files/test1_*.dat

test1:
	python3 zip_data1.py $(TEST1_FILE)
