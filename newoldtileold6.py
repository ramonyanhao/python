num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i): #质数是只能被1和它本身整除，不能有其他因数，例如4，可以被1和它本身整除，也可以被2整除，所以4不是质数
      if(i%j==0): #这里就是for j in range(2,4):j只能是2和3，if(4%2==0)跳出循环，反之加入列表为质数，就是i这个数可以被j整除，4就不是质数
         break
   else:
      num.append(i)
print(num)