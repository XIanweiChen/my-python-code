#Mon Jun 11 15:29:51 2018
import os
import glob
import time
import sys
import random
print(os.getcwd())
#os.system('mkdir OK')


#时间 
print(time.strftime("%Y.%m.%d  %H:%m"))     #%y 两位数的年份表示（00-99）%y 两位数的年份表示（00-99）
											# %Y 四位数的年份表示（000-9999）
											# %m 月份（01-12）
											# %d 月内中的一天（0-31）
											# %H 24小时制小时数（0-23）
											# %I 12小时制小时数（01-12

print (time.localtime(time.time()))			#time.struct_time(tm_year=2018, tm_mon=6, tm_mday=11, tm_hour=15, tm_min=33, tm_sec=28, tm_wday=0, tm_yday=162, 
print (time.asctime( time.localtime(time.time()) ))				#Mon Jun 11 15:33:28 2018

print(glob.glob('*.py'))


a=random.randrange(2)     					#不包括2
print(a)

