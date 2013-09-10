#Name:       Demonstrator.py
#Author:     Raitis Kupce
#Updated:    10/07/2013
#Updated by: Raitis Kupce
from process import Process       # Imports class Process
from filereader import FileReader

       
class Demonstrator():
    ''' Runs both files in one go process and filereader '''
    
    def __init__(self,filename):
        self.process = Process()                        # Creats an object                    
        self.reader = FileReader(filename,self.process) # Creates an object
        self.reader.run()                               # call the run method
        self.process.totalCost()

    def displayRow(self):          return self.process.getRowCount()
    def displayTotalSum(self):     return '\u00A3%0.2f'% (self.process.getTotalSum())
    def displayCostDate(self):     return self.process.dateList()
    def displayStaff_Names(self):  return self.process.getListOfName()
    def displayStaffCost(self):    return self.process.getStaffCost()
    def displaySpendings(self,ID):    return self.process.spendingType(ID)


    #Last Method Run
    def total_Cost(self):       return self.process.totalCost() #Must be run after
    def displayStaffSum(self): return self.process.getStaffCost()
    def staffName(self): return self.process.getStaff()

    
##a = Demonstrator("Demo.xlsx")
##print(a.displaySpendings())


