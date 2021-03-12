#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
#注意在pycharm运行django时报编码错误，因为encode就是编码byte,所以byte对象没有属性encode.先在错误文件handle.py把data=data.encode()改为data=data.decode(),要把byte解码为str
# 然后把write(data)改为write(data.encode()),这里写入时必须要byte才可以，所以再把str转为byte