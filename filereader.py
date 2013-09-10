#Name:          Filereader.py
#Author:        Raitis Kupce
#Updated:       18/07/2013
#Updated by:    Raitis Kupce

import xlrd
import datetime

class FileReader():

    def __init__(self, filename, process):
        self.process = process
        self.filename = filename
        self.workbook = xlrd.open_workbook(self.filename)
        self. worksheet = self.workbook.sheet_by_name('Sheet1')
        self.num_rows = self.worksheet.nrows - 1
        self.num_cells = self.worksheet.ncols - 1
        self.firstline = True
        self.curr_row = 0
        
    def run(self):
        '''Reads the travel log file.xlsx '''

        myCount= 0
        while myCount < self.num_rows:
            staff_ID = int(self.getField(0))
            forename = self.getField(1)
            surname = self.getField(2)
            staff_Name = forename, surname
            location = self.getField(6)
            reason = self.getField(8)
            date = self.getField(17)
            #tup = xlrd.xldate_as_tuple(xls_timestamp_number,self.workbook.datemode)
            #print(tup)
            #date =self.minimalist_xldate_as_datetime(data,0)
            cost = float(self.getField(12))

            self.curr_row += 1    
            self.process.runProcess(staff_ID, date, staff_Name,location, reason,cost,)
            myCount +=1
            
    def getField(self,cell_Index):
        "find the value in give specific cell using excel"
        row = self.worksheet.row(self.curr_row)
        curr_cell = cell_Index
        if self.firstline: # skip first line
            self.firstline = False
            self.curr_row +=1
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        cell_type = self.worksheet.cell_type(self.curr_row, curr_cell)
        cell_value = self.worksheet.cell_value(self.curr_row, curr_cell)
        
        return cell_value

    def minimalist_xldate_as_datetime(self,xldate,datemode):
        return(
            datetime.datetime(30,12,1899)
            + datetime.timedelta(days=xldate + 1462 * datemode)
            )
