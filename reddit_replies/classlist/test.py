# -*- coding: utf-8 -*-
# Python 3

class Downloader:
    def __init__(self, list_to_download=[]):
        self._list_to_download = list_to_download   # [ [url, target_file_path], [...],  ]
        print("__init__:", self._list_to_download)
        

    def add_downloads(self, list_url_path_filename: list):
        print("add_downloads:", len(list_url_path_filename))      # will print "2" as expected
        
        for x in list_url_path_filename:
            # x is a list: [url, local-folder-path, file-name]
            
#             THE FOLLOWING WILL PRINT: 
#                 [1, 1, 1]
#                 [2, 2, 2]
#                 [1, 'file_name']        << Where is this from???
#                 and then error with IndexError: list index out of range
            print(x)
            if x[2]:
                pass
           
            # if I remove this line, it will work:
            self._list_to_download.append( [x[0], "file_name"] )




if __name__ == '__main__': 
    list_url_path_filename  = [ [1, 1, 1 ], [2, 2, 2] ]
    list_to_download        = [ [1, 1],     [2, 2] ]
    # This will give "IndexError: list index out of range" in add_downloads: if x[2]:
    downloader = Downloader(list_to_download=list_url_path_filename)
    # list_url_path_filename is a list with sublists of each _three_ values, but
    # list_to_download only should be a list with sublists of each _two_ values and in add_downloads,
    # I append sublists of each two values
    # But mixing them should not at all mess up the code, 
    # since I only append to that list right now, and don't use it
    downloader.add_downloads(list_url_path_filename)
    
    # ----------------------------------------------
    # This will work without errors:
    downloader = Downloader(list_to_download=list_to_download)
    downloader.add_downloads(list_url_path_filename)
