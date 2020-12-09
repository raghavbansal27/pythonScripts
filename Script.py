import os
import re
from datetime import date
base_dir = os.path.dirname(os.path.realpath(__file__))
md_dir="GNE/Mech/Academics/"
curr_dir = os.path.abspath(os.path.join(base_dir, md_dir))
regex = re.compile(r'\d+')

pre = ''
heading=str(input("Enter the Notice Heading:- "))

total_notices = []
for file in os.listdir(curr_dir):
    if file.endswith(".md"):
    	total_notices.append(file)
if len(total_notices) != 0:    	
	str1 = "".join(total_notices)

	file_number_str = regex.findall(str1)
	file_number_list = list(map(int, file_number_str)) 
	file_number = max(file_number_list)
	md_path = "GNE/Mech/Academics/notice" + str(file_number) + ".md"
	path = os.path.abspath(os.path.join(base_dir, md_path))
	#print(path)
	if os.path.isfile(path):

		new_md_path = "GNE/Mech/Academics/notice" + str(file_number + 1) + ".md"
		new_path = os.path.abspath(os.path.join(base_dir, new_md_path))
		#print(new_path)
		file_number+=1
		file=open(new_path,"w")
		file.write("## " + heading + "\nDate : " + str(date.today()) + "  \nNotice Number : " + str(file_number) + "\n" + pre)
		file.flush()
		file.close()
		print("Notice added successfully!")
	else:
		print("File not found")


# Create new file if no .md file exist
else:
	file_number = 1
	md_path = "GNE/Mech/Academics/notice" + str(file_number) + ".md"
	path = os.path.abspath(os.path.join(base_dir, md_path))
	#print(path)
	file=open(path,"w")
	file.write("## " + heading + "\nDate : " + str(date.today()) + "  \nNotice Number : " + str(file_number) + "\n" + pre)
	file.flush()
	file.close()
	print("Notice added successfully!")

