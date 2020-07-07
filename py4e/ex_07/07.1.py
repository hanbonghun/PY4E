# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
num_line = 0
s =0.0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        ipos = line.find(" ")
        b= line[ipos+1:]
        s = s + float(b)
        num_line = num_line+1
print("Average spam confidence:", s/num_line)
