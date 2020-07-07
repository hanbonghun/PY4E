name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic= dict()

for line in handle:
    line = line.rstrip()
    if line=='':
        continue
    else:
        ln = line.split()
        if ln[0]=="From":
            dic[ln[1]]= dic.get(ln[1],0)+1


user = None
count= None
for users,counts in dic.items():
    if user is None or counts>count:
        user = users
        count =counts

print(user,count)
