import os, time


class file:
    def file_name(self, path):
        self.path = os.path.abspath(path)
        filename_list = os.listdir(path)
        self.s = [filename for filename in filename_list if os.path.isfile(path + os.sep + filename)]  # 文件列表

    # 文件类型
    def type_file(self):
        dic_type = {
            '可执行文件': ['exe', 'bat'],
            '压缩文件': ['zip'],
            '阅读文件': ['pdf', 'docx', 'txt', 'log', 'ini'],
            '镜像文件': ['iso'],
            'mysql文件': ['sql'],
            'python文件': ['py'],
            '网页文件': ['html'],
            '其他文件': ['dll', 'prx', 'dat', 'bin']
        }
        list_file = []
        for k, v in dic_type.items():
            for s in self.s:
                if s[s.rfind('.') + 1:] in v:
                    list_file.append(k + ';' + s[:s.rfind('.')] + ';' + str(
                        os.path.getsize(self.path + os.sep + s) / 1024 / 1024) + ';' + time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(self.path + os.sep + s))))
        list_file = [i.split(';') for i in list_file]
        return list_file


if __name__ == '__main__':
    file = file()
    file.file_name('C:\\Windows')
    # 打印
    print(
        "============================================================================================================")
    print('文件类型', '文件名称', '文件大小\MB', '文件时间', sep="\t" * 15, end="\n")
    for i in file.type_file():
        print('%-50s' % i[0], '%-70s' % i[1], '%-58.2f' % float(i[2]), '%-100s' % i[3], sep="\t", end="\n")
    print(
        "============================================================================================================")
