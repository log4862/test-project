txt = 'but soft what light in yonder window breaks'
words = txt.split()

l = list()

for word in words:
    l.append((len(word), word))

print ('list is ...' )
print (l)

l.sort()

res = list()

for length, word in l:
    res.append(word)

print(res)

