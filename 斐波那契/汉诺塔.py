#Python汉诺塔函数
#重点是下面的每条move函数递归中都会执行三条move函数，除了move(1,x,y,z),因为它默认的n已经=1,符合if条件，所以不会运行其他两条move函数，例如:
#move(n-1,x,z,y)中会执行move(n-1,x,z,y)和move(1,x,y,z)和move(n-1,y,x,z),另一个重点执行到move函数时，都会重新传入参数move(3,a,b,c)
def move(n,x,y,z):

    if n==1:
        print(n,x,y,z,0)
        print(x,'-->',z)

    else:
        print(n, x, y, z,1)
        move(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        '''
        def move(n,x,y,z):  传入参数为 move(3, 'a', 'b', 'c')

            if n==1: (n=3) 条件不成立,不执行

                print(x,'-->',y)

            else:

               ① move(n-1,x,z,y) 参数发生变化->传入参数为 move(2, 'a', 'c', 'b')

                                  move(n, x, y, z)  参数发生变化->参数发生变化: n=2 x='a' y='c' z='b'

                    if n==1 : (n=2) 条件不成立,不执行

                        print(x,'-->',z)

                    else :

                        move(n-1,x,z,y) 这里传入参数为 move(1, 'a', 'b', 'c')

                                    move(n, x, y, z) 参数发生变化->参数发生变化: n=1 x='a' y='b' z='c'

                                    if n==1 : (n=1) 条件成立,执行

                                        print(x,'-->',z)  输出 a-->c 执行完毕,回退

                        向下执行

                        move(1,x,y,z)  n=2 x='a' y='c' z='b'

                                    move(n, x, y, z) 参数发生变化->这里传入参数为 move(1, 'a', 'c', 'b')

                                    if n==1 : (n=1) 条件成立,执行

                                        print(x,'-->',z)  输出 a-->b 执行完毕,回退

                                    向下执行  n=2 x='a' y='c' z='b'

                        move(n-1,y,x,z) 这里传入参数为 move(1, 'c', 'a', 'b')

                                    move(n, x, y, z) 参数发生变化->这里传入参数为 move(1, 'c', 'a', 'b')

                                    if n == 1 : n = 1 条件成立 执行完毕

                                        print(x,'-->',z)  输出 c-->b  执行完毕,回退
        '''
        print(n, x, y, z,2)
        move(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        #②move(1,x,y,z) 传入参数为move(3, 'a', 'b', 'c')，经过计算得出n=1 x='a' y='b' z='c'  输出 a-->c
        print(n, x, y, z, 3)
        move(n-1,y,x,z)#将y上的n-1个盘子移动到z上
        '''
        ③move(n-1,y,x,z)这里传入参数为move(3, 'a', 'b', 'c')，经过计算得出 move(2, 'b', 'a', 'c')

            move(n, x, y, z)  参数发生变化->参数发生变化: n=2 x='b' y='a' z='c'

            if n==1 : (n=2) 条件不成立,不执行

                print(x,'-->',z)

            else :

                move(n-1,x,z,y) 参数发生变化->这里传入参数为 move(1, 'b', 'c', 'a')

                            move(n, x, y, z) 参数发生变化->这里传入参数为: n=1 x='b' y='c' z='a'

                            if n==1 : (n=1) 条件成立,执行

                                print(x,'-->',z)  输出 b-->a 执行完毕,回退

                向下执行

                move(1,x,y,z)  n=2 x='b' y='a' z='c'

                            move(n, x, y, z) 参数发生变化->这里传入参数为 move(1, 'b', 'a', 'c')

                            if n==1 : (n=1) 条件成立,执行

                                print(x,'-->',z)  输出 b-->c 执行完毕,回退

                            向下执行  n=2 x='b' y='a' z='c'

                move(n-1,y,x,z) 参数发生变化->这里传入参数为 move(1, 'a', 'b', 'c')

                            move(n, x, y, z) 参数发生变化->这里传入参数为 move(1, 'a', 'b', 'c')

                            if n == 1 : n = 1 条件成立 执行完毕

                                print(x,'-->',z)  输出 a-->c  执行完毕,回退
        '''
        print(n, x, y, z, 4)
move(3,'a','b','c')
