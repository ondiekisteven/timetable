import pymysql
import db

"""
@param program : Name of the program you want to search its units
@return : returns units for the program otherwise returns null
"""
def getunitsbycourse(program):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("select * from coursedetails where coursename = '%s'" % program)
	data = cursor.fetchone()
	units = []
	units = data[2].split(".")
	cursor.close()
	dbase.close()
	return units

"""
@param program_name : 	Name of the program you want to search if it exists. it performs a wildcard search
						meaning it matches programs which contain name provided
@return : returns true if any such program exists, otherwise null. 
"""
def isexistprogram(program_name):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT * FROM coursedetails WHERE coursename LIKE '%%%s%%'" % (program_name.lower()))
	
	if(cursor.rowcount == 0):
		return False
	else:
		return True
	
	cursor.close()
	dbase.close()

"""
@param regno : Registration number of student which you are searching for.
@return : returns True if reg number is found, otherwise False
"""
def isexistreg(regno):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT * FROM students WHERE regnumber = '%s'" % (regno.lower()))
	
	if(cursor.rowcount == 0):
		return False
	else:
		return True
	
	cursor.close()
	dbase.close()

"""
@param program_name : An expression or name of program you are searching for. Can be full name 
					or part of name of the program you are seraching for
@return : returns list of programs which contain the specified name, otherwise retuns null
"""
def getprogramslike(program_name):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT * FROM coursedetails WHERE coursename like '%%%s%%'" % (program_name))
	result = cursor.fetchall()
	cursor.close()
	dbase.close()
	return result

"""
@param null : 
@return : returns a list of all programs saved in database
"""
def getallprogramnames():
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT coursename FROM coursedetails")
	result = cursor.fetchall()
	cursor.close()
	dbase.close()
	return result

"""
@param id : id of the program you are searching for
@return : returns name of program, otherwise null
"""
def getprogrambyid(id):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT * FROM coursedetails WHERE id = %d" % (id))
	data = cursor.fetchone()
	coursename = data[1]
	cursor.close()
	dbase.close()
	return coursename

"""
@param program_name : Name of the program you want to search
@return : returns the course id if successful, otherwise returns -1 if no such progra found
"""
def getprogramid(program_name):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("SELECT * FROM coursedetails WHERE coursename = '%s'" % (program_name))
	
	if(cursor.rowcount >0):
		data = cursor.fetchone()
		courseid = data[0]
		return courseid
	else:
		return -1

	cursor.close()
	dbase.close()
	

"""
@param program : Registration number of student 
@return : returns the registration number taken by student if student exists, 
			otherwise null of either student doesnt exist or no course found[however second option is unlikely]
"""
def getcoursebyregno(regno):
	dbase = db.connect()
	cursor = dbase.cursor()

	if (isexistreg(regno)):
		cursor.execute("SELECT * FROM students WHERE regnumber = '%s' " % (regno.lower()))
		data = cursor.fetchone()
		course = getprogrambyid(data[3])
		return course
	else:
		pass


"""
@param regno : registration number of student you re registering
@param coursename : name of course the student is doing. must be a registered course 
					otherwise the insertion will fail.
@return : returns 0 if operation is successful, or 0 if any error occurs
"""
def insertcourse(regno, coursename):
	dbase = db.connect()
	cursor = dbase.cursor()

	if(isexistprogram(coursename) and isexistreg(regno)):
		cursor.execute("UPDATE TABLE students SET courseid = %d WHERE regnumber = '%s'" % (getprogramid(coursename), regno))
		dbase.commit()
		return 0
	else:
		return 1

def register(regno, fname, lname, courseid, year):
	dbase = db.connect()
	cursor = dbase.cursor()
	cursor.execute("INSERT INTO students (regnumber, firstname, surname, courseid, year) values ('%s', '%s', '%s', %d, %d)" % (regno, fname, lname, courseid, year))
	dbase.commit()
	cursor.close()
	dbase.close()