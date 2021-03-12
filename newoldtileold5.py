for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print(num)
         print(i)
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环,重要的意思是参数i只要第一个值可以被num整除就可以不用后面的值了，
         # 例如for i in range(2,num)，只要num能整除2运行到break就会跳到下个num，
         # 不能被整除的在确定第一个因子就不通过，程序转到else
   else:                  # 循环的 else 部分
      print (num, '是一个质数')