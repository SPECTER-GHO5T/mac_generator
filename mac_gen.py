# A-F 65-70
# a-f 97-102
# 0-1 48-57
import random

def ascii():
	n = random.randint(1,3)
	if n == 1 :
	    dg=random.randint(65,90)
	elif n == 2:
	    dg=random.randint(97,122)
	else:
	    dg=random.randint(48,57)
	return dg
fq=int(input("enter the number of mac address to be generated > "))
for i in range (fq): 
  a1=chr(ascii())
  a2=chr(ascii())
  b1=chr(ascii())
  b2=chr(ascii())
  c1=chr(ascii())
  c2=chr(ascii())
  d1=chr(ascii())
  d2=chr(ascii())
  e1=chr(ascii())
  e2=chr(ascii())
  f1=chr(ascii())
  f2=chr(ascii())
  macid=(a1+a2+":"+b1+b2+":"+c1+c2+":"+d1+d2+":"+e1+e2+":"+f1+f2)
  print (macid)
