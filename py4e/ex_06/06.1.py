text = "X-DSPAM-Confidence:    0.8475";
a= text.find(' ')
b= text[a:]
b= b.lstrip()
print(float(b))
