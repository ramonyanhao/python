def file_replace(file_name, rep_word, new_word):#文本中替换字符串：
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:#遍历读取的文件，eachline函数就是文件所有内容
        if rep_word in eachline:#如果需要替换的内容在eachline里
            count = count+eachline.count(rep_word)#计数共有多少个需要替换的字符串，count用法：所有内容.count(搜索的字符串）
            print(count)
            eachline = eachline.replace(rep_word, new_word)#进行替换字符串
        content.append(eachline)#把替换过的字符换添加到空列表中
        print(content)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()
    if decide == 'no':
        print('退出')

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)