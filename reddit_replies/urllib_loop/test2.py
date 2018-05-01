import urllib.request

links = ['https://upload.wikimedia.org/wikipedia/commons/d/d9/Opossum_fur.jpg',
         'https://static1.squarespace.com/static/58d56678bebafb1f82465030/t/59a08b0ff43b55c13a2666b1/1503693586253/pat-flesher-fur-beautiful-brown-.jpg?format=2500w']

def go(links):
    for (i, link) in enumerate(links):
        download(link, 'fname'+str(i))

def download(link, fname):
    print(f"downloading '{link}' to '{fname}'")
    urllib.request.urlretrieve(link, fname)

go(links)
