import json
uid = 42
iid_list = [1, 2, 3, 4, 5]
userprediction = uid, iid_list
with open('tets.json', 'w') as f:
    json.dump(userprediction, f)
