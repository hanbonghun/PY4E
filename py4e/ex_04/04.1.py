def computepay(h,r):
    if float(h)<=40:
        return float(h)*float(r)
    else :
      return float(h)*float(r) + (float(h)-40)*float(r)/2

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay",p)
