import os
import time
from socket import AF_INET, SOCK_STREAM, socket

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir('Answers')


#TASK 1

inOut = [
    ('python 1.py http://www.chinatoday.com.cn/ctenglish/2018/et/202411/t20241104_800382564.html', '310\n'),
    ('python 1.py https://www.apachefriends.org/blog/new_xampp_20231119.html', '62\n'),
    ('python 1.py https://jassemrl.github.io', '77\n'),
]

passed = 0
for i,o in inOut:
    with os.popen(i) as process:
        if o == process.read():
            passed += 1

print(f'TASK 1: {passed}/{len(inOut)}')