from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as keyfile:
        keyfile.write(key)

def load_key():
    return open('key.key','rb').read()
    
key=load_key()
cipher=Fernet(key)
choice=input("Want to Add a New password or view the existing password(view,add,Quit): ").lower()


def add():
    username=input("Enter site name or user name: ")
    password=input("Enter password!: ")
    encrypted=cipher.encrypt(password.encode())
    with open('password.txt','a') as f:
        f.write(username.lower() +"|"+ encrypted.decode()+ "\n")
    print("Data is sucessfully added")
def view():
    username=input("Enter site name or user name: ").lower()
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()  
            user,pwd=data.split("|") 
            if username==user.lower():
                print("username: "+user+" , Password: "+cipher.decrypt(pwd).decode() )
if choice=="view":
    view()
elif choice=="add":
    add()
elif choice=="quit":
    print("Quit")
else:
    print("invalid attempt!")
    