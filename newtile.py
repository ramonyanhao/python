#*字塔
i=1
#j=1
while i<=100:
   if i<=50:
      print ("*"*i)

   elif i<=100 :
      j=i-2*(i-50)
      print("*"*j)
   i+=1
else :
   print("")