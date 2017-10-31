# Author:Gamebu
import os

fp = open("logfile.scr", 'r')
userlist = fp.readlines()
fp.close()
#print(userlist)
tag = 0
while tag == 0:
    username = input("login name:")
    password = input("passwoed:")
    for i in range(len(userlist)):
        if userlist[i].split(":")[0] == username:
            while True:
                _password = userlist[i].split(":")[1]
                _try_times = int(userlist[i].split(":")[2])
                if _try_times == 3:
                    print("That account been LOCK,fuck off!")
                    tag = 1
                    break
                elif _password != password:
                    _try_times += 1
                    userlist[i] = username + ":" + _password + ":" + str(_try_times) + "\n"
                    print("Wrong PAss,try again")
                    break
                else:
                    tag = 1
                    print("Welcome user %s login" % username)
                    userlist[i] = username + ":" + _password + ":0\n"
                    break
            break
        elif i == len(userlist)-1:
            print("No account named %s,fuck off" % username)
        else:
            continue

os.remove("logfile.scr")
fp1 = open("logfile.scr", "w")
for j in range(len(userlist)):
    if userlist[j].split():
        fp1.writelines(userlist[j])
fp1.close()