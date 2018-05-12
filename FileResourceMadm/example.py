f = open('wasteland.txt', mode='wt', encoding='utf-9')
f.write('What are the roots that clutch')
f.close()
ls -s wasteland.txt
dir wasteland.txt

g = open('wasteland.txt', mode='rt', encoding='utf-8')

# text mode read char , in b reads bytes
g.read(32)
g.read()

# move back to the start
g.seek(0)

g.readline()

