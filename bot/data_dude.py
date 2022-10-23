words = []


def da_collector(data):
    word_map = dict()
    collected_words = data.content.lower().split(' ')
    for wrd in collected_words:
        if wrd not in word_map:
            word_map[wrd] = 1
        else:
            word_map[wrd] += 1
    collected_words.append(word_map)
    return word_map


print(words)
