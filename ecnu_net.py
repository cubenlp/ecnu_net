#!/usr/bin/env python3

import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from argparse import ArgumentParser

# create the parser
parser = ArgumentParser(description='Script description')
## add arguments
parser.add_argument('--user', '-u', help='Username')
parser.add_argument('--password', '-p', help='Password')
parser.add_argument('--method', '-m', help='Login or logout', default='login')
parser.add_argument('--url', help='Login page url', default='https://login.ecnu.edu.cn/srun_portal_pc?ac_id=1&theme=pro')
parser.add_argument('--force', help='Force login/logout', action='store_true')

# parse the arguments
args = parser.parse_args()
## set values to variables
assert args.user is not None and args.password is not None, "Username and password are required"
username = args.user
password = args.password
method = args.method.lower()
LoginPageUrl = args.url
force = args.force # False by default

# Ping test: return 0 if success
pingtest = lambda: os.system("ping -c 2 -W 3 baidu.com")

# Login
def Login(delay=5):
	if pingtest() == 0: # the network is connected
		print("Already connected to the Internet")
		if not force:
			print("Use --force to login anyway")
			return
    # start the device
	driver = webdriver.PhantomJS(executable_path="./phantomjs/bin/phantomjs")
	driver.get(LoginPageUrl)
	time.sleep(delay)
 
	# set username
	driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        
	# set password
	driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
 
	# click to login
	driver.find_element(By.XPATH, '//*[@id="login-account"]').click()
 
	# wait for the response
	time.sleep(2)

def Logout():
    # start the device
    driver = webdriver.Chrome()
    driver.get(LoginPageUrl)
    time.sleep(3)

    # click to logout
    driver.find_element(By.XPATH, '//*[@id="logout"]').click()

	# wait for the response
    time.sleep(2)


def main():
	if args.method == 'login':
		Login()
		exit()
	elif args.method == 'logout':
		Logout()
		exit()
	else:
		print("Unknown method: " + args.method)
		exit()

if __name__ == '__main__' :
    main()