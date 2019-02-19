#_*_coding: utf-8 _*_
'''
@uthor:aLun@july
Copyright(c)2019 SZ_MB-QTC
FileName:Ch2_designasimplegame.py
@DATE:2019-Feb-18;Mon
@TIME:16:56:55
用Python設計第一個游戏
'''

print('---------------------------I love fishc workingroom--------------------------------------')
temp = input('Guess what number I am thinking right now?')
guess = int(temp)  #在Python中，一个等号表示”赋值“，2个等号表示”判断是否相等”；int表示把temp改成整形
if guess == 8:   # 冒号后面按下回车，下一行会自动缩进
    print('Amazing~~~')
    print('Sorry, no prize')   #如果这行没有缩进，可以执行看看是不是会报错
else:
    print('WORNG!!,the number I am thinking right now is 8')
print('GAME OVER')

'''
BIF == Built-in functions 内置函数
Python是脚本程序，int，input，print，这种都属于内置函数
如何知道Python中有多少内置函数？
>>>dir(__builtins__)
出来的结果中，英文字母全小写的属于BIF
如何查询BIF的用法？#以查询input为例
>>>help(input)
'''
