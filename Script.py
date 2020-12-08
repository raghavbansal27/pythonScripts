import os
from datetime import date
curr_dir="GNE/Mech/Academics/"
i=1

heading=str(input("Enter the Notice Heading:- "))

pre=''

if os.path.isfile("GNE/Mech/Academics/noticeX.md"):
    file=open("GNE/Mech/Academics/noticeX.md","r")
    pre=file.read()
    file.seek(0,0)
    line=file.readlines()
    i=int(line[2][16:])
    file.close()
    os.rename(os.path.join(curr_dir,str(i)),os.path.join(curr_dir,str(i+1)))
    i+=1
else:
    os.mkdir(os.path.join(curr_dir,str(i)))
file=open("GNE/Mech/Academics/noticeX.md","w")
file.write("## "+heading+"\nDate : "+str(date.today())+"  \nNotice Number : "+str(i)+"\n"+pre)
file.flush()
file.close()
