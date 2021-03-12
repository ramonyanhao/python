'''
1.创建一个空目录，用于存放conda虚拟环境和所需要的安装包

2.在cmd中运行conda create -p=空目录路径，创建一个虚拟环境在这个空目录中，例如: conda create -p=D:\anacondaenv

3.运行conda env list可以查看虚拟环境目录，目前应该只有两条，base是conda默认的虚拟环境目录，还有一条就是刚刚创建的虚拟环境目路，以后的虚拟环境都会存放在这个目录中

4.再运行conda create -n 虚拟环境名称 需要安装的python工具包,例如: conda create -n 虚拟环境名称 numpy pandas,这样就创建了一个虚拟环境，名称是condaenv,存放在D:\anacondaenv中

5.虚拟环境中安装包conda install -n 虚拟环境名称 numpy，卸载包运行conda remove -n 虚拟环境名称 numpy,更新虚拟环境中的包:conda update -n 虚拟环境名称 numpy

6.激活这个虚拟环境使用activate 虚拟环境名称 激活，退出虚拟环境使用deactivate，linux使用conda activate 虚拟环境名称，conda deactivate退出虚拟环境

7.导入导出虚拟环境:conda env export > environment.yaml把当前虚拟环境导出到environment.yaml文件中
conda env create -f environment.yaml创建一个从environment.yaml文件中获取的虚拟环境

8.删除虚拟环境:conda remove --name 虚拟环境名称 --all

9.设置安装包为国内镜像服务器：conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

10.查看conda信息，包括刚添加的镜像服务器，版本，虚拟环境存放路径和工具包路径:conda info,查看虚拟环境列表：conda info -e和conda env list是同样的效果

11.复制虚拟环境:conda create --name condaenv1 --clone condaenv,克隆出一个新的虚拟环境名为condaenv1,condaenv1和condaenv拥有一样的配置和已安装的工具包

12.pip freeze > piplist.txt导出pip已安装的工具包列表到piplist.txt文件中，pip install -r piplist.txt在新的虚拟环境中从piplist.txt文件中的包列表开始安装

13.在pycharm中创建conda虚拟环境，是conda可以在pycharm中使用，file-settings-ADD-conda Environment-指定一个空目录
'''