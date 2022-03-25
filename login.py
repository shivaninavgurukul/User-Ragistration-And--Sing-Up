import json
import re
import os.path
print("***WELCOME TO LOGIN SIGNUP PAGE***")
login_signup=input("What is choose login or signup:- ")
file_exists=os.path.exists("login.json")
def dump(obj):
    with open("login.json","w") as f:
        json.dump(obj,f,indent=2)
if login_signup=="signup":
    first_name=input("enter your fast name:-")
    last_name=input("enter your last name:-")
    RegEx="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com)"
    email=input("enter your email:-")
    if (re.search(RegEx,email)):
        strong="[a-zA-Z0-9]+@[a-zA-Z0-9]"
        pass1=input("enter the password:- ")
        if (re.search(strong,pass1)):
            com_password=input("comfirm your password:- ")
            if pass1==com_password:
                dict={"first name":first_name,"last_name":last_name,"email":email,"password":pass1}
                if file_exists==False:
                    with open("login.json","w") as file:
                        d=file.read()
                        p=json.loads(d)
                        p.append(dict)
                        dump(p)
                else:
                    with open("login.json","a") as file:
                        json.dump([dict],file,indent=4)         
            else:
                print("password did not match")
        else:
            print("invalid password")
    else:
        print("invalid email address")
elif login_signup=="login":
        user2=input("enter the name:-")
        password2=input("enter your password:-")
        with open("login.json","r") as f1:
            re=f1.read()
            b=json.loads(re)
            for i in b:
                if i["user2"]==user2:
                    if i["password2"]==password2:
                        print("LOGIN SUCCESSFULLY")
                    else:
                        print("wrong password")
                else:
                    print("wrong user name")
else:
    print("wrong id")                                