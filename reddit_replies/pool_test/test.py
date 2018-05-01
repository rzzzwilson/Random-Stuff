from multiprocessing import Pool, Lock

counter = 0
msg_list = ["message1", "message2", "message3", "message4", "message5", "message6",
            "message7", "message8", "message9", "message10", "message11", "message12"]


def increment(item):
    global counter
    global msg_list

    print(counter, item, msg_list[counter])
    counter = counter + 1


if __name__ == '__main__':

    item_list = ["item1",
                 "item2",
                 "item3",
                 "item4",
                 "item5",
                 "item6",
                 "item7",
                 "item8",
                 "item9",
                 "item10",
                 "item11",
                 "item12"]

    p = Pool(4)
    p.map(increment, item_list)
    p.terminate()
