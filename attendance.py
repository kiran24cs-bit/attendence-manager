import os.path,sys,logging 
x= open("d:/kiran programming/attendance.txt","a")
wd=0
att={}
clg=input("enter college name:").upper()
cl="--"*20
n=int(input("enter no of students:"))
s=0
x.write(f"{cl}{clg}{cl}\n\nNumber of students are:{n}\n")
while n>s:
    name=input("enter student name:").upper().strip()
    if name not in att:
        att.setdefault(name,0)
        print("name added ✅")
        s+=1
    else:
        print("name alreafy exist ❌")
def week(day):
    a=[]
    fn="d:/kiran programming/"+day+".txt"
    d= open(fn,"a")
    d.write(f"{day} ATTENDANCE\n\nworking day number={wd}\n\n")
    for q in att.keys():
        pa=input(f"{q}:").upper()
        if pa=="" or pa=="p":
            att[q]=att[q]+1
        else:
            a.append(q)
    d.write(f"Today total present are : {n-len(a)}\nToday total absent are  : {len(a)}\nAbsent students are:{a}\n\n{cl}\n\n")   
while True:
    day=input("enter day of attendance:").upper()
    if day=="MONDAY" or day=="TUESDAY" or day=="WEDNESDAY" or day=="THURSDAY" or day=="FRIDAY" or day=="SATURDAY" or day=="SUNDAY":
        wd=wd+1
        week(day)
    elif day=="":
        break
    else:
        print("ENTER A VALID DAY")
x.write(f"TOTAL WORKING DAYS ARE:{wd}\n\n")
x.write("ATTENDANCE OF STUDENTS ARE:\n\nNAME       : ATTENDANCE\n\n")
for n,a in att.items():
    n=n.ljust(10)
    a=str(a).ljust(10)
    x.write(f"{n} : {a}\n")
