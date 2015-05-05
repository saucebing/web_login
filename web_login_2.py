#!/usr/bin/python
import os
import md5
import time
username = "hch13"
password = "hch7223522"
f = open('web_login.log','a')

LOGIN_STR = 'curl -d "username=%(username)s&password=%(password)s&drop=0&type=1&n=100" http://net.tsinghua.edu.cn/cgi-bin/do_login'
CHECK_STR = 'curl -d "action=check_online" http://net.tsinghua.edu.cn/cgi-bin/do_login'
LOGOUT_STR = 'curl http://net.tsinghua.edu.cn/cgi-bin/do_logout'

def login(username,password):
  if (not isinstance(username,str)) or (not isinstance(password,str)):
    print "[ERROR] invalid parameters"
    return
  ps = md5.md5(password).hexdigest()
  #print "[INFO] ps = %s" %(ps)
  return os.popen(LOGIN_STR %(dict(username=username,password=ps))).read()

def check_login():
  return os.popen(CHECK_STR).read()

def logout():
  result = str(os.popen(LOGOUT_STR).read())
  result_list = result.split(",")
  return result_list

def get_local_ip(ifname): 
  import socket, fcntl, struct 
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15])) 
  ret = socket.inet_ntoa(inet[20:24]) 
  return ret 

def current_time():
  return time.strftime('%Y-%m-%d %H:%M:%S')

index = 0
result = check_login()
f.write("==================================================================================================\n")
f.write(current_time() + " Check: " + result + "\n")
while result == "" and index < 60:
  result = login(username,password)
  f.write(current_time() + " Login: " + result + "\n")
  result = check_login()
  f.write(current_time() + " Check: " + result + "\n")
  time.sleep(5)
  index += 1
  f.write(current_time() + " Num: " + str(index) + "\n")
