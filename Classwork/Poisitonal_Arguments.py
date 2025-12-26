def display(username,mail,pwd):
    print(f'username: {username}\nMail:{mail}\npassword:{pwd}')

uname=input("Enter the username:")
mail=input("Enter the mail:")
pwd=input("Enter the password:")

display(uname,mail,pwd)
display(mail,uname,pwd)
display(pwd,uname,mail)
display(uname,pwd,mail)


#2.logic

def display(username,mail,pwd):
    print(f'username: {username}\nMail:{mail}\npassword:{pwd}')

uname=input("Enter the username:")
mail=input("Enter the mail:")
pwd=input("Enter the password:")

display(username=uname,mail=mail,pwd=pwd)
display(pwd=pwd,username=uname,mail=mail)
display(username=uname,pwd=pwd,mail=mail)


display(uname,mail,pwd)
display(mail,uname,pwd)
display(pwd,uname,mail)
display(uname,pwd,mail)

#3.Default arguments:

def display(username,mail,pwd='1234'):
    print(f'username: {username}\nMail:{mail}\npassword:{pwd}')

uname=input("Enter the username:")
mail=input("Enter the mail:")
pwd=input("Enter the password:")


display(uname,mail)
display(mail,uname,pwd)
