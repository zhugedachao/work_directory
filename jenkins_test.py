# -*- coding: utf-8 -*-
import re
import os

"""
   sh '''
                    sed -i '11s/11/17/g' CMakeLists.txt
                    git submodule init 
                    git submodule update
                    mkdir -p build && cd build
                    cmake .. -DCMAKE_BUILD_TYPE=Release && make -j
                    cd tests
                    ./dbtest
                    cd ..
                    cd .. && rm -rf *'''
"""

import os
commands17 = ["sed -i '11s/11/17/g' CMakeLists.txt", 
"git submodule init", "git submodule update", 
"mkdir -p build && cd build", "cmake .. -DCMAKE_BUILD_TYPE=Release && make -j", 
"cd tests", "./dbtest", "cd ..", "cd .. && rm -rf *"]
commands14 = ["sed -i '11s/11/17/g' CMakeLists.txt", 
"git submodule init", "git submodule update", 
"mkdir -p build && cd build", "cmake .. -DCMAKE_BUILD_TYPE=Release && make -j", 
"cd tests", "./dbtest", "cd ..", "cd .. && rm -rf *"]
commands11 = ["sed -i '11s/11/17/g' CMakeLists.txt", 
"git submodule init", "git submodule update", 
"mkdir -p build && cd build", "cmake .. -DCMAKE_BUILD_TYPE=Release && make -j", 
"cd tests", "./dbtest", "cd ..", "cd .. && rm -rf *"]

def run_func_C17():
    """
    编译C++17
    """
    try:
        for com in commands17:
            os.system(com)
        return "PASS"
    except Exception as err:
        return "FAIL" + str(err)
def run_func_C14():
    """
    编译C++14
    """
    try:
        for com in commands14:
            os.system(com)
        return "PASS"
    except Exception as err:
        return "FAIL" + str(err)
def run_func_dbtest():
    """
    dbtest执行
    """
    try:
        for com in commands14:
            os.system(com)
        return "PASS"
    except Exception as err:
        return "FAIL" + str(err)

def Jenkins_func():

    KVDK_result = []

    for mun in range(10):
        print(mun)
        

Jenkins_func()
