#_*_coding: utf-8 _*_
'''
@uthor:aLun@july
Copyright(c)2019 SZ_MB-QTC
FileName:Ch2_designasimplegame.py
@DATE:2019-Feb-18;Mon
@TIME:16:56:55
'''

print('---------------------------I love fishc workingroom--------------------------------------')
temp = input('Guess what number I am thinking right now?')
guess = int(temp)
if guess == 8:
    print('Amazing~~~')
    print('Sorry, no prize')
else:
    print('WORNG!!,the number I am thinking right now is 8')
print('GAME OVER')
