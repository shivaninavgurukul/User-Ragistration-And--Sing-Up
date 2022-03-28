import json
import re
import os.path
print("WELCOME TO LOGIN SINGUP PAGE")

file=os.path.exists("text.json")
if file==False:
    login_singup=input("what is choose login or signup:-")
    if login_singup=="signup":
        l=[]
        d={}
        first_name=input("enter your first name:-")
        RegEx="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|org)"
        email=input("enter your email:-")
        if (re.search(RegEx,email)): 
            strong="[a-zA-Z0-9]+@[a-zA-Z0-9]"
            pass1=input("enter the password:-")
            if re.fullmatch(r'[A-Za-z0-9@#$%&%^$+=]{8,}',pass1):
                con_pass=input("confirm your password:-")
                if pass1==con_pass:
                    print("** SINGUP SUCCESSFUL **")
                    d1=["first name","email","password"]
                    d2=[first_name,email,pass1]
                    # for i in range(len(d1)):
                    #     d.update({d1[i]:d2[i]})
                    d=dict(zip(d1,d2))
                    l.append(d)
                    # print(l)
                    with open("text.json","a") as f:
                        json.dump(l,f,indent=4)
            else:
                print("password did not match")
elif file==True:
    login_singup=input("what is choose login or signup:-")
    if login_singup=="signup":
        first_name=input("enter your first name:-")
        strong="[a-zA-Z0-9]+@[a-zA-Z0-9]"
        pass1=input("enter your password:-")
        if re.fullmatch(r'[A-Za-z0-9@#$%&%^$+=]{8,}',pass1):
            con_pass=input("confirm your password:-")
            if pass1==con_pass:
                m= open("text.json","r")
                b=m.read()
                if pass1 in b:
                    print("your account is already exists")
                else:
                    k={}
                    RegEx="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|org)"
                    email=input("enter your email:-")
                    if (re.search(RegEx,email)):
                        print("** SINGUP SUCCESSFUL **")
                        d1=["first name","email","password"]
                        d2=[first_name,email,pass1]
                        # for i in range(len(d1)):
                        #     k.update({d1[i]:d2[i]}) 
                        k.update(zip(d1,d2))
                        # k=dict(zip(d1,d2))
                        # print(k)
                        with open("text.json","r")as f:
                            y=json.load(f)
                        y.append(k)    
                            # p=json.dump(p,f,indent=3)
                        with open("text.json","w") as t:
                            json.dump(y,t,indent=4)
                    
                
                    else:
                        print("wrong password")
    else:

        if login_singup=="login":
            user2=input("enter the name:-")
            pass2=input("enter the password:-")
            with open("text.json","r")as f:
                b=json.load(f)
                for i in b:
                    if i["first name"]==user2:
                        print("your name is correct")
                        if i["password"]==pass2:
                            print("LOGIN SUCCESSFUL")
                            print(b)
                    else:
                        print("LOGIN NOT SUCCESSFUL")
        
        else:
            print("YOU MADE A MISTAKE IN CHOOSING")


