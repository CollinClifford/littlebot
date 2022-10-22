words = []

def da_collector(data):
    map = dict()
    words = data.content.lower().split(' ')
    for wrd in words:
        if wrd not in map:
            map[wrd] = 1
        else:
            map[wrd] += 1
    words.append(map)
    return map

print(words)