import time
import os
import sys

countdown = 1000

while countdown > 0:
    print (countdown)
    countdown = countdown - 1
    time.sleep(0.000000001)
    os.system("cls")

if countdown == 0:
    while True:
        print(''' 
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████           
        █████░░░██████████████░░░███░░░██████░░░░██████░░███████████░░░░░██░░░░░█████████░░░░░░░░░███░░░░░░░░░███░░░█████████░░░░█████      
        █████░░░░░░░░███░░░░░░░░░███░░░██████░░░░██████░░███████████░░░░░██░░░████░░░░░████░░░░░░░███░░░░░░░░░███░░░███░░░░░██░░░█████
        █████░░░░░░░░███░░░░░░░░░███░░░███░░██░░██░░███░░███░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░███░░░░░░░░░███░░░███░░░░░░██░░█████
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░████░░░███░░███░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░░░███░░░███░░░░░░██░░█████
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░██░░░░███░░███████████░░░░░░░░░░░░███████░░░░░░░░░░░███░░░░░░░░░███░░░███░░░░░██░░░█████ 
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░███░░███████████░░░░░░░░░░░░░░░░░░████░░░░░░░░███░░░░░░░░░███░░░█████████░░░░█████ 
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░███░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░█████  
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░███░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░███░░░░░░░███░░░░███░░░░░░░░░░█████   
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░███░░███████████░░░░░░░░░░████░░░░█████░░░░░░░░░███░░░░░███░░░░░███░░░░░░░░░░█████
        █████░░░░░░░░███░░░░░░░░░███░░░███░░░░░░░░░░███░░███████████░░░░░░░░░░░░████████░░░░░░░░░░░░░░███████░░░░░░░███░░░░░░░░░░█████
        █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████   
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒
        ''')
        time.sleep(0.5)
        os.system("cls")
        print(''' 
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
        █████▒▒▒██████████████▒▒▒███▒▒▒██████▒▒▒▒██████▒▒███████████▒▒▒▒▒██▒▒▒▒▒█████████▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒█████████▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒██████▒▒▒▒██████▒▒███████████▒▒▒▒▒██▒▒▒████▒▒▒▒▒████▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒██▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒██▒▒██▒▒███▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒██▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒████▒▒▒███▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒██▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒██▒▒▒▒███▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒██▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒███▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒█████████▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒███▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒███▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒███▒▒▒▒███▒▒▒▒▒▒▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒███▒▒███████████▒▒▒▒▒▒▒▒▒▒████▒▒▒▒█████▒▒▒▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒▒▒▒███▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒█████
        █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 
        ''')
        time.sleep(0.5)
        os.system("cls")