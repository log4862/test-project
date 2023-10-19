#sort words by length

txt = 'but soft what light in yonder window breaks'
words = txt.split()

l = list()

for word in words:
    #make a list of tuples
    l.append((len(word), word))

print ('list is ...' )
print (l)

l.sort()


results = list()

#each tuple in the list MUST have exacrly 2 elements
for length, word in l:
    results.append(word)

print(results)

