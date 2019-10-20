import xlrd
import databases.db

def open_book(path):
    # opening the exel book
    book = xlrd.open_workbook(path)

    # open first sheet
    firstSheet = book.sheet_by_index(0)
    row = 1
    try:
    	while(row < 20):
    		data = firstSheet.row_values(row)

         	units = []
         	venues = []

	        for item in data:
	        	unit, sep, ven = item.partition(".")
	        	units.append(unit)
	        	venues.append(ven)

	        db.insertunit(units[0], units[1], units[2], units[3], units[4], units[5])
	        print("inserted units for row %d" % row)

	        db.insertvenue(venues[0], venues[1], venues[2], venues[3], venues[4], venues[5])
	        print("inserted venues for row %d" % row)
	        print("\n" + "-"*50 +"\n")

	        	
	        row += 1
    except IndexError:
        print("All Records saved successfully")



open_book('timetable_sample.xls')