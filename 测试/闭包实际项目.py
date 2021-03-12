#【闭包实现快速给不同项目记录日志】
# 这段代码实现了给不同项目logging的功能，只需在你想要logging的位置添加一行代码即可。
import logging

def log_header(logger_name):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s] %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(logger_name)

    def _logging(something, level):
        if level == 'debug':
            logger.debug(something)
        elif level == 'warning':
            logger.warning(something)
        elif level == 'error':
            logger.error(something)
        else:
            raise Exception("I dont know what you want to do?")

    return _logging


project_1_logging = log_header('project_1')

project_2_logging = log_header('project_2')


def project_1():
    # do something
    project_1_logging('this is a debug info', 'debug')
    # do something
    project_1_logging('this is a warning info', 'warning')
    # do something
    project_1_logging('this is a error info', 'error')


def project_2():
    # do something
    project_2_logging('this is a debug info', 'debug')
    # do something
    project_2_logging('this is a warning info', 'warning')
    # do something
    project_2_logging('this is a critical info', 'error')


project_1()
project_2()
