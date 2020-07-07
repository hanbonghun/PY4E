fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.split()
    for wrd in word:
        if wrd in lst:
            continue
        else:
            lst.append(wrd)
lst.sort()
print(lst)
