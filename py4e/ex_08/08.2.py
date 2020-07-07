fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line =='':
        continue
    else:
        ln= line.split()
        if ln[0]=="From":
            print(ln[1])
            count=count+1

print("There were", count, "lines in the file with From as the first word")
