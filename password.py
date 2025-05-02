from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as keyfile:
        keyfile.write(key)

def load_key():
    return open('key.key','rb').read()

key=load_key()
cipher=Fernet(key)   

def add():
    username=input("Enter site name or user name: ")
    password=input("Enter password!: ")
    encrypted=cipher.encrypt(password.encode())
    with open('password.txt','a') as f:
        f.write(username.lower() +"|"+ encrypted.decode()+ "\n")
    print("Password Store Successfully")
    choice()  
    
def view():
    username=input("Enter site name or user name: ").lower()
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()  
            user,pwd=data.split("|") 
            if username==user.lower():
                print("username: "+user+" , Password: "+cipher.decrypt(pwd.encode()).decode())
        choice()
      

def login(a,b):
    with open('llogin.txt','r') as f:
        for lines in f.readlines():
            data=lines.rstrip()
            user,pwd=data.split("|")
    if a.lower()==user.lower() and b==pwd:
        print(f"Login sucessfull {a}")
        return True
    else :
        return False
def choice():
        key=load_key()
        cipher=Fernet(key)
        choice =input("Want to Add a New password or view the existing password(view,add,quit): ").lower()
        if choice=="view":
            view()
        elif choice=="add":
            add()
        elif  choice=="quit":
            pass
        else:
            print("invalid attemp!")
        
def main():
    # write_key()
    
    print("Welcome to password manager \nTo access the password user must login!")
    Username=input("Enter username: ")
    password=input("Enter password: ")
    f=login(Username,password)
    if f:
        choice()
    else:
        print("Invalid Credential!")
  

main()