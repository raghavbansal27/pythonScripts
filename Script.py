import os
from datetime import date
curr_dir="C:/Users/abv93/OneDrive/Documents/GitHub/pythonScripts/"
i=1
check_dir=os.path.join(curr_dir,str(i))
while os.path.isdir(check_dir)==True:
    i+=1
    check_dir=os.path.join(curr_dir,str(i))
heading=str(input("Enter the Notice Heading:- "))
os.mkdir(check_dir)
file=open("C:/Users/abv93/OneDrive/Documents/GitHub/pythonScripts/noticeX.md","a")
file.write("## "+heading+"\nDate : "+str(date.today())+"  \nNotice Number : "+str(i)+"  \n")
file.flush()
file.close()
