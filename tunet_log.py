import os
import md5

LOGIN_STR = 'curl -d "username=%(username)s&password=%(password)s&drop=0&type=1&n=100" http://net.tsinghua.edu.cn/cgi-bin/do_login'
CHECK_STR = 'curl -d "action=check_online" http://net.tsinghua.edu.cn/cgi-bin/do_login'
LOGOUT_STR = 'curl http://net.tsinghua.edu.cn/cgi-bin/do_logout'

def login(username,password):
    if (not isinstance(username,str)) or (not isinstance(password,str)):
        print "[ERROR] invalid parameters"
        return
    ps = md5.md5(password).hexdigest()
    #print "[INFO] ps = %s" %(ps)
    os.system(LOGIN_STR %(dict(username=username,password=ps)))

def check_login():
    os.system(CHECK_STR)

def logout():
    os.system(LOGOUT_STR)
