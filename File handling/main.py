from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.glob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")
    
def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name:-")
        p=Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                Data =input("what you want to write in he file:--")
                fs.write(Data)
                
            print(f"file created successfully")
        else:
            print("this file already exists")
    except Exception as err:
        print(f"an error ocuurred {err}")
        
def readfile():
    try:
        readfileandfolder()
        name=input("which will u want to read:-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                Data=fs.read()
                print(Data)
                
            print("successfully read")
        else:
            print("the file doesnt exists")
        
    except Exception as err:
        print(f" en error occured {err}")  
        
     
def updatefile():
    try:
        readfileandfolder()
        name=input("which file u want to update")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing file name ")
            print("press 2 for overwriting the data") 
            print("press 3 for appending some data")
            res=int(input("tell ur response:- "))
            
            if res==1:
                name2=input("tell ur new name:-")
                p2=Path(name2)
                p.rename(p2)
                
            if res ==2:
                with open(p,"w") as fs:
                    Data=input("what u want to write (over write):-")
                    fs.write(Data)
                    
            if res==3:
                with open(p,"a") as fs:
                    Data=input("what u want to write (over write):-")
                    fs.write(" "+Data)
    except Exception as err:
        print(f"en error ocuured {err}")
        
def deletefile():
    try:
        readfileandfolder()
        name = input("while file u want to delete: - ")
        p=Path(name)  
        
        if p.exists() and p.is_file():
            os.remove(p)
            
            print("file removed successfully")
            
        else:
            print("no such file exists")
            
    except Exception as err:
        print(f"an error occurred {err}")   
     
     
        
        
print("press 1 for a creating file")
print("press 2 for a reading file")
print("press 3 for a updating file")
print("press 4 for a deletion file")
check=int(input("Give your response:--"))


if check==1:
    createfile()
    
if check==2:
    readfile()
    
if check==3:
    updatefile()
    
if check == 4:
    deletefile()