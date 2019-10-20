import studentdb
import db




std_reg = raw_input("Enter your registration number: \n> ")

if(studentdb.isexistreg(std_reg)):
	print("student already exists")
else:
	std_fname = raw_input("Enter your first name\n> ")
	std_sname = raw_input("Enter your surname\n> ")
	print("SELECT NUMBER WHICH CORRESPONDS TO YOUR COURSE")
	count = 1
	for prog in studentdb.getallprogramnames():
		print("{}. {}").format(count, prog)
		count += 1
	coursid = raw_input("\n\n> ")
	std_prog = int(coursid)-1
	std_year = int(raw_input("Enter your year of study. eg 1,2,3 or 4 \n> "))

	studentdb.register(std_reg, std_fname, std_sname, std_prog, std_year)

