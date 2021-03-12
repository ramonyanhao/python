def list_of_groups(list_info, per_list_len):
    '''
    :param list_info:   列表
    :param per_list_len:  每个小列表的长度
    :return:
    '''
    list_of_group = zip(*(iter(list_info),) * per_list_len) # (iter(list_info),) 乘 per_list_len，注意iter中的逗号，需要生成多个iter时，使用元组格式
    # 如果不加zip中的*,结果是有per_list_len个迭代器:(<list_iterator object at 0x0000025758560EC8>, <list_iterator object at 0x0000025758560EC8>, <list_iterator object at 0x0000025758560EC8>)
    # 加了zip(*)把结果解压为[['name zhangsan', 'age 10', 'sex man'], ['name lisi', 'age 11', 'sex women']]
    print(list_of_group)
    end_list = [list(i) for i in list_of_group] # i is a tuple
    count = len(list_info) % per_list_len
    end_list.append(list_info[-count:]) if count != 0 else end_list
    return end_list

if __name__ == '__main__':
    list_info = ['name zhangsan', 'age 10', 'sex man', 'name lisi', 'age 11', 'sex women']
    ret = list_of_groups(list_info,3)
    print(ret)
    list_dict = []
    for item in ret:
        data = {}
        data['name'] = item[0].split(' ')[1]
        data['age'] = item[1].split(' ')[1]
        data['sex'] = item[2].split(' ')[1]
        list_dict.append(data)
    print(list_dict)