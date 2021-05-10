import os
import ctypes
import random

os.system('mode con: cols=35 lines=13')
ctypes.windll.kernel32.SetConsoleTitleW("Password generator")
os.system('color 1f')

i = 0

d1 = 'qwertyuiopasdfghjklzxcvbnm'
d2 =  'QWERTYUIOPASDFGHJKLZXCVBNM'
d3 =  '0123456789'
d4 = '#!'

dfull = d1 + d2 + d3 + d4

lenght = 16

print('  ------password generator------ \n')

for x in range(8):
	password = "".join(random.sample(dfull, lenght))
	i = i + 1
	print('       #' + str(i), ' | ', password)

input("\n  <> Press any key to continue <>")
