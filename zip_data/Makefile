TEST1_FILE=test1.zip
TEST2_FILE=test2.zip

clean:
	rm -f *.zip

build:
	rm -f *.zip
	zip -q -j $(TEST1_FILE) data_files/test1_*.dat
	zip -q -j $(TEST2_FILE) data_files/test1_*.dat

test1:
	python3 zip_data1.py $(TEST1_FILE)

test2:
	python3 zip_data2.py $(TEST2_FILE)
