from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words_byte =[]
    story_words = []

    for line in story:
        line_words_byte = line.split()
        line_words = line.decode('UTF-8').split()

        for word in line_words_byte:
            story_words_byte.append(word)

        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)

#print(story_words)
#print(story_words_byte)