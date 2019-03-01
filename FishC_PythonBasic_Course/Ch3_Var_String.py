#_*_coding: utf-8 _*_
'''
@uthor:aLun@july
Copyright(c)2019 SZ_MB-QTC
FileName:Ch3_Var_String.py
@DATE:2019-Feb-22;Fri
@TIME:08:17:50
Title:小插曲_变量与字符串
'''

'''
变量（Variable）
变量名就像我们的名字，把一个值赋值给一个名字的时候，此时python会将这个值储存在内存中；这种行为称为"变量赋值"
不过python的做法与其他编程语言稍有不同，比较像是把名字贴在值上面，所以有人会说，Python没有变量只有名字
'''
teacher = '小甲鱼'
print(teacher)

teacher = '老甲鱼'
print(teacher)

first = 3
second = 8
third = first + second
print(third)

myteacher = 'fish C'
yourteacher = 'blacknight'
ourteacher = myteacher + yourteacher  #字符串的拼接
print(ourteacher)

'''
变量注意事项：
1. 使用变量之前必须先对其赋值
2. 变量名可以包含：字母，数字，下划线  不可以：用数字开头
3. 字母不限定大小写，但是大小写对于Python来说是有区别的. 
4. 等号(=)是赋值，固定格式：变量名 = 值
5. 请给变量一个合适，专业，易懂的名字
'''

'''
字符串(string)
引号内的一切都属于字符串，字符串也称为文本；文本与数字是不同的资料类型
'''
stringsample1=5 + 8

stringsample2='5' + '8'
print(stringsample1)
print(stringsample2)

'''
注意事项：
1. 引号需要成对使用，单引号配对单引号，双引号配对双引号
2. 如果字符串中间需要出现单引号或是双引号 - 
    a.使用转义符号(\)对字符串中的引号进行转义
    b. 
'''
stringsample3='Let\'s go'
print(stringsample3)

stringsample4