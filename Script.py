import os
import re
from datetime import date
base_dir = os.path.dirname(os.path.realpath(__file__))
md_dir="GNE/Mech/Academics/"
curr_dir = os.path.abspath(os.path.join(base_dir, md_dir))
regex = re.compile(r'\d+')

heading=str(input("Enter the Notice Heading:- "))

pre=''
for file in os.listdir(curr_dir):
    if file.endswith(".md"):
        path = os.path.join(curr_dir, file)
if os.path.isfile(path):
    file_number = regex.findall(path)
    file_number = int(file_number[0])

    new_md_path = "GNE/Mech/Academics/notice" + str(file_number + 1) + ".md"
    new_path = os.path.abspath(os.path.join(base_dir, new_md_path))
    print(new_path)
    file_number+=1
    file=open(new_path,"w")
    file.write("## " + heading + "\nDate : " + str(date.today()) + "  \nNotice Number : " + str(file_number) + "\n" + pre)
    file.flush()
    file.close()
    print("Notice added successfully!")
else:
    print("File not found")