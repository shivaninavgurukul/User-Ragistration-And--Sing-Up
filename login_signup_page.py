import json
import re
print("***WELCOME TO LOGIN SIGNUP PAGE***")
login_signup=input("What is choose login or signup:- ")
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
                print("**SIGNUP SUCCESSFUL**")
                dict={"first name":first_name,"last_name":last_name,"email":email,"password":pass1}
                with open("text.json","a") as f:
                    b=json.dump(dict,f,indent=4)         
            else:
                print("password did not match")
        else:
            print("invalid password")
    else:
        print("invalid email address")
elif login_signup=="login":
    if login_signup=="login":
        user2=input("enter the name:-")
        pas2="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)"
        email2=input("enter your email:-")
        if (re.search(pas2,email2)):
            strong2="[a-zA-Z0-9]+@[a-zA-Z0-9]"
            pw=input("enter the password:-")
            if (re.search(strong2,pw)):
                com_password2=input("comfirm your password:-")
                if pw==com_password2:
                    print("**LOGIN SUCCESSFUL**")
                    dict={"user2":user2,"email2":email2,"pw":pw}
                    with open("text2.json","w") as f:
                        b=json.dump(dict,f,indent=4)
                else:
                    print("*** LOGIN NOT SUCCESSFUL***")
            else:
                print("invalid password")
        else:
            print("invalid email address")
    else:
        print("** YOU MADE A MISTAKE IN CHOOSING**")
else:
    print("thrid option not allowed")
