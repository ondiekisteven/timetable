import pymysql

def connect():
	db = pymysql.connect("LOCALHOST", "root", "Steven.1998", "timetable")
	return db

def insertunit(first, second, third, fourth, fifth, sixth):
	db = connect()
	cursor = db.cursor()
	cursor.execute("INSERT INTO units (7to9, 9to11, 11to1, 1to3, 3to5, 5to7) VALUES ('%s', '%s','%s','%s','%s','%s')" % (first, second, third, fourth, fifth, sixth))
	db.commit()
	cursor.close()
	db.close()

def insertvenue(first, second, third, fourth, fifth, sixth):
	db = connect()
	cursor = db.cursor()
	cursor.execute("INSERT INTO venues (7to9, 9to11, 11to1, 1to3, 3to5, 5to7) VALUES ('%s', '%s','%s','%s','%s','%s')" % (first, second, third, fourth, fifth, sixth))
	db.commit()
	cursor.close()
	db.close()