#Name:          Counter.py
#Author:        Raitis Kupce
#Updated:       10/07/2013
#Updated by:    Raitis Kupce

class Process():

    def __init__ (self):
        self.rowCount = 0
        self.total = 0.0
        self.staff_Name   = [] # List All Staff.
        self.staff_ID     = {} # show staff by it ID
        self.staff_Total  = {}
        self.staff_cost   = {}
        #self.total_Cost_Type = {}
        
        
    def runProcess(self, staff_ID, date, name, location, reason, cost):
        '''runs all the methods in one go '''
        
        self.rowCount +=1
        self.totalSum(cost)
        self.list_Of_Name(staff_ID, date, name, location, reason, cost)
        self.staff_By_ID()
        
    def getRowCount(self): return self.rowCount
        
    def totalSum(self,cost):
        self.total += cost
    def getTotalSum(self): return self.total

    def list_Of_Name(self, staff_ID, date, name, location, reason, cost):
        self.staff_Name.append((staff_ID, date, name, location, reason, cost))
    def getListOfName(self): return self.staff_Name
    
    def staff_By_ID(self):
            for name in self.staff_Name:
                if name[0] in self.staff_ID.keys():
                    self.staff_ID[name[0]] = name[2]             
                else:
                    self.staff_ID[name[0]] = name[2]
    def getStaff(self): return self.staff_ID  

    def totalCost(self):          
        for cost in self.staff_Name:
            
            if cost[0] in self.staff_Total.keys():
                self.staff_Total[cost[0]] += cost[5]
            else:
                self.staff_Total[cost[0]] = cost[5]      
    def getStaffCost(self): return self.staff_Total

    def spendingType(self,ID):
        self.total_Cost_Type = {}
        for reason in self.staff_Name:
            if ID == reason[0]:
                if reason[4] in self.total_Cost_Type.keys():
                    self.total_Cost_Type[reason[4]] += reason[5]
                else:
                    self.total_Cost_Type[reason[4]] = reason[5]
            else:
                continue
        return self.total_Cost_Type
    
    def getSpendings(self): return self.total_Cost_Type
        


    def aa(self):
        for v in self.staff_Total.keys():
            print(v,self.staff_Total[v]," aaa" )



    
    
            
            
        
        
        
        
