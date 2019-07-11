my_dict={
    "admin":"123321",
    "user1":"123456"
}

username=input()
while not username in my_dict:
    username = input()

print("please input your password")

errorcount=0
password=input()

while (errorcount < 3):

    if(my_dict[username] != password):
        errorcount=errorcount+1
        if errorcount<3:
            print("密码错误，还有%d机会" %(3-errorcount))
            password=input()

    else:
        break

if(errorcount ==3):
    print("密码输入次数超限")
else:
    print("用户 %s 登录成功！" % username)
