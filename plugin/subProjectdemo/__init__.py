# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: __init__.py
# @Author: myloe
# @Time: Nov 06, 2020
# ---
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: __init__.py
# @Author: myloe
# @Time: Nov 06, 2020
# ---
"""
使用__init__可以解决直接使用自己写的其它项目时由于项目目录结构不同带来的import为问题。
eg:subProjectdemo是希望直接引用的项目
注：
    1.如果把subProjectdemo放在当前项目目录时，subProjectdemo子目录中会出现包引用的错误。因为，subProjectdemo的编写时依赖于其本身的子目录的，
    即环境变量（sys.path）中是subProjectdemo的路径，而在新的项目中使用时，环境变量不含subProjectdemo的路径，因此会出现import问题。
    此时在subProjectdemo项目中使用sys.path.append(os.path.dirname(__file__))将其扩充至系统变量中即可。
    2.究其根源是：从某个文件启动代码时，python会自动将该文件所在目录自动追加至环境变量中去。该问题同样导致了命令行运行一个项目时
    有时会出现import问题，而使用编译器却不存在import问题。
    3.基于这样的原因，如果一个项目想要使用多个已有项目，可以新增个插件目录（plugin）以上述方式使用
    
注2：
    在父级目录中，添加方法 plugin.subProjectdemo.main.main.get_datasource() 可进行该问题测试。
    注意区别有下述代码和没有的区别
    >>> import sys,os
    >>> sys.path.append(os.path.dirname(__file__))

"""

import sys,os
sys.path.append(os.path.dirname(__file__))
