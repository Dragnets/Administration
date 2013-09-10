#Name:          Guiss.py
#Author:        Raitis Kupce
#Updated:       18/07/2013
#Updated by:    Raitis Kupce

from demonstrator import *
from tkinter.filedialog import *
from tkinter import Tk, StringVar, ttk
import os


class TaskGUI():
    def __init__(self,master):

        self.browseActive= False    # Indicate that btn browse have not been used.
        self.activeBR = False       # Idicate wether break down have been used.
        
        
        # FRAMES Below >>>
        title     = Frame(master,)
        title.grid(row=1,column=2,sticky = W)
        header    = Frame(master, )
        header.grid(row=2,column=1,sticky=W)
        
        self.mainBody  = Frame(master,)
        self.mainBody.grid(row=3, column=1, sticky=W)
        gap       = Frame(self.mainBody,width=100,height=20,)
        gap.grid(column=1, sticky= W)

        gapBR     = Frame(self.mainBody, width=20,)
        gapBR.grid(row=2,column=3)
        
        self.fieldList = Frame(self.mainBody) # Name list
        self.fieldList.grid(row=2,column=2, sticky=W)
        
        self.bodySummary = Frame (self.mainBody,bg= 'yellow')
        self.bodySummary.grid(row=4,column=2, sticky = W)

        self.bottom  = Frame(self.mainBody,width=10,height=10,)
        self.bottom.grid(row=6,column=2, sticky=W)


        # SUMMAARY
        self.gapSUM = Frame(self.mainBody, width=10, bg='green')
        self.gapSUM.grid(row= 1, column=4)
        self.fieldSummary =Frame(self.mainBody,)
        self.fieldSummary.grid(row=2, column=5, sticky= W)

        
        
        
        #/SUMMARY
        #/Frame >>>



        #Header >>>
        Label(header,height=5,).grid(row=2, column=1) # GAP FOR TITLE
        Label(title,).grid(row=1, column=1)#Gap from top
        #Label(title, font='mono -36 bold', text="Project PY").grid(column=2,sticky=E)
        Label(header,width=3).grid(row=3,column=0,sticky=W)
        Label(header,text='File name: ', font='cornsilk -20 bold').grid(row=3, column=1, sticky=W)
        Label(header,width=2).grid(row=3, column=3) #SPACE

        self.combo(header)
        
        Button(header, text='Browse...',width=10,font='mono -15 bold', bg='lightblue',
               command=self.open_file).grid(row=3, column=4,)
        Label(header,width=3,).grid(row=3, column=5) # SPACE
        Button(header, text="Process",width=20,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=3, column=6,)
        Label(header,width=3).grid(row=3, column=7)
        Button (header, text="Show Expenses", width = 15, font = 'mono -15 bold',
                command=self.break_Down).grid(row=3, column=8)
        
        #/Header >>>
        

        self.combo(header)  #Combo box
##        Button(self.bottom, text='QUIT', fg='red', font='arial -18 bold',
##               command=self.quitMessage).grid(row=3, column=3,)
        

    def staff_Frame(self):
        ''' Creates a table to display staffs'''
        
        Label(self.fieldList,width=18,text='Staff Name',font='arial -20 bold').grid(row=1,column=2)
        Label(self.fieldList,width=8,text='Total Cost', font='arial -20 bold').grid(row=1,column=3)
        Label (self.bottom,width=5,).grid(column=1,row=1) # Gap for Total Grand
        Label(self.bottom, text='Grand total:', font='arial -20 bold').grid(row=2, column=2, sticky=E)
        self.total = Label(self.bottom,width=9, font= 'arial -30 bold',  bg='lightblue')
        self.total.grid(row=2, column=3,sticky=E)
        
    def process_file(self, ev=None):
        '''Open the choosen file by calling Demonstrator Class'''
        
        filename=self.box.get() # gets value from self.box
        if self.browseActive == True:
            if self.check_combo(self.browsedFile) == True: # Add only to combo box
                self.fileUsed.append(self.browsedFile)     # if not already Used
            self.browseActive= False                # Resets browse button status
            filename=self.browsedFile

        self.reader=Demonstrator(filename)
        self.listAllStaff()
        self.staff_Frame()
        self.notify()
        #self.work_out_rows(self.reader.displayRow())
        

    def open_file(self):
        '''Ability to browse the file in your computer'''
        
        self.browsedFile = os.path.basename(askopenfilename(filetypes=[('','')]))
        self.box.set(self.browsedFile) 
        self.browseActive= True # To mark that this function has been used.

    def check_combo(self,filename):
        '''Check If file alreadi is in combo box'''

        for file in self.fileUsed:
            if file == filename:
                return False
        return True  
        
    def combo(self,frame):
        '''Creates a Combo box and gives 3 default files'''
        
        self.box_value = StringVar()
        self.box = ttk.Combobox(frame, textvariable=self.box_value,
                                state='readonly') # Creates a combo box
        self.fileUsed=['Demo.xlsx'] # Default combo list
        self.box['values'] = (self.fileUsed) 
        self.box.current(0) # Current value
        self.box.grid(row=3, column=2)

    def listAllStaff(self):
        ''' Make a list of all staff '''
        
        line=1
        self.var  = IntVar() #  Must be self. to disable hover.
        staffName = self.reader.staffName()
        for name in staffName:
            self.NameList  = Radiobutton (self.bodySummary, width=15, text= staffName[name], font= 'arial -20 bold',
                               bg='grey', anchor= W, variable = self.var, value = name, pady = 0,
                                          ).grid(row=line, column=2, sticky=W)
            amount = self.get_Total_Cost_By_Name(name)
            self.TotalCost = Label (self.bodySummary,pady=3, width=10, text="\u00A3"+str(amount), font= 'arial -20 bold',
                                bg='grey').grid(row=line, column=3)
            line +=1
    def get_Total_Cost_By_Name(self,ID):
        '''Displays cost for each staff '''
        
        staff_Cost = self.reader.displayStaffCost()
        for cost in staff_Cost:
            if cost == ID:
                return staff_Cost[cost]

    def break_Down(self):
        '''Creates a break down list of selected person '''

        if self.activeBR:
            self.destroy_Break_Down()
            
        self.field     = Frame(self.mainBody,) # Break down Summary
        self.field.grid(row=2, column=4, sticky = W)
        self.body    = Frame(self.mainBody)
        self.body.grid(row=4,column=4, sticky=NW)
        
        self.totalSummary = Frame(self.mainBody,)
        self.totalSummary.grid(row=4, column= 5, sticky=N)

        
        self.activeBR = True
        self.staffID = self.var.get()

        Label(self.field,width=10,text='Date', font='arial -20 bold').grid(row=1,column=1)
        Label(self.field,width=10,text='Location', font='arial -20 bold').grid(row=1,column=2)
        Label(self.field,width=15,text='Reason', font='arial -20 bold').grid(row=1,column=3)
        Label(self.field,width=10,text='Cost', font='arial -20 bold').grid(row=1,column=4)

        Label(self.fieldSummary,width=20).grid(row=1,column=0)
        Label(self.fieldSummary, width=10, text='Reason', font='arial -20 bold').grid(row=1, column=1)
        Label(self.fieldSummary, width=10, text='Total', font =' arial -20 bold').grid(row=1, column=2)

        self.work_out_rows()
        self.spendingType()

    def work_out_rows(self,):
        '''Generates list of rows'''
        
        staff_List = self.reader.displayStaff_Names()
        line =2
        for row in  staff_List:
            if self.staffID == row[0]:     
                index = 1    
                date = row[index]
                location = row[index+2]
                reason = row[index+3]
                cost =row[index+4]
                self.add_row(date, location, reason, cost,line)
                line +=1
            
        

        
    def add_row(self,date,location, reason,cost,line):
        '''Place values in break down list '''        
            
        self.date = Label(self.body,width=10, text=date, font='arial -20 bold',bg='grey')
        self.date.grid(row=line,column=1)
        self.location =Label(self.body,width=10, text=location, font='arial -20 bold', bg='grey')
        self.location.grid(row=line,column=2)
        self.reason = Label(self.body,width=15, text=reason, font='arial -20 bold',bg='grey')
        self.reason.grid(row=line,column=3)
        self.cost = Label(self.body,width=10, text="\u00A3"+str(cost), font='arial -20 bold',bg='grey')
        self.cost.grid(row=line,column=4)

    def spendingType(self,):
        '''Create a summary of spendings'''

        line = 1
        Label(self.totalSummary,width=20,).grid(row=1,column=0)
        expense = self.reader.displaySpendings(self.staffID)
        for key in expense:
            self.spend = Label(self.totalSummary, width=10, text=key, font='arial -20 bold', bg='grey')                    
            self.spend.grid(row=line,column=1,sticky=N)
            self.CostSum = Label(self.totalSummary,width=10, text=expense[key], font='arial -20 bold', bg='grey')                
            self.CostSum.grid(row=line,column=2,sticky=N)
            line +=1
            
    def destroy_Break_Down(self):
        '''Destroys two frames '''
        
        self.body.destroy()
        self.field.destroy()
        self.totalSummary.destroy()

    def notify(self):
        ''' Get the value from each question to display them on screen '''
        
        self.total['text'] = str(self.reader.displayTotalSum())

 

    def quitMessage(self,):
        '''Exit programme'''
        
##        message = messagebox.askyesno(title="Quit", message="Are you sure want to exit?",icon= "warning")    
##        if message:
        top.destroy() # On Yes exits application.


if __name__ == "__main__":
    top =Tk()
    top.geometry('10920x1080')
    top.title("Stella")
    top.grid()
    
    app = TaskGUI(top)

    top.mainloop()
