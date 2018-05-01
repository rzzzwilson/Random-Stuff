lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "down": 'down',
    "up": 'direction',
    "left": 'direction',
    "right": 'direction',
    "back": 'direction',
    "go": 'verb',
    "stop": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "from": 'stop',
    "at": 'stop',
    "it": 'stop',
    "bear": 'noun',
    "door": 'noun',
    "princess": 'noun',
    "cabinet": 'noun',
    "0": 'number',
    "1": 'number',
    "2": 'number',
    "3": 'number',
    "4": 'number',
    "5": 'number',
    "6": 'number',
    "7": 'number',
    "8": 'number',
    "9": 'number',
}

# Scan Method
def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type, word))
    return results

result = scan('north up go eat bear door 0 9 xyzzy test.')
print(result)
