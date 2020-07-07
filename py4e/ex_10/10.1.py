name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    line = line.rstrip()
    lst = line.split(':')
    if 'From ' in lst[0]:
        hr = lst[0][-2:]
        dic[hr]= dic.get(hr,0)+1


for hr,count in sorted(dic.items()):
    print(hr,count)
