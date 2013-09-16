#Name:          Guiss.py
#Author:        Raitis Kupce
#Updated:       18/07/2013
#Updated by:    Raitis Kupce

from demonstrator import *
from tkinter.filedialog import *
from tkinter import Tk, StringVar, ttk
from PIL import ImageTk, Image
import os


class TaskGUI():
    def __init__(self,master):

        self.browseActive   = False     # Indicate that btn browse have not been used.
        self.activeBR       = False     # Indicate wether break down have been used.
        self.processUsed    = False     # Indicate wether calculation have been done.
        self.scrollBarActive = False    # Indicate wether expense scroll bar is active
        
        # FRAMES Below >>>
        logoFrame = Frame(master)
        logoFrame.grid(row=0,column=1,sticky=W)
        title     = Frame(master,)
        title.grid(row=1,column=2,sticky = W)
        self.header    = Frame(master, )
        self.header.grid(row=2,column=1,sticky=W)
        
        self.mainBody  = Frame(master,)
        self.mainBody.grid(row=3, column=1, sticky=W)
        gap       = Frame(self.mainBody,width=100,height=20,)
        gap.grid(column=1, sticky= W)

        gapBR     = Frame(self.mainBody, width=20,)
        gapBR.grid(row=2,column=3)

        # Content
        
        # Staff canvas
        self.fieldList = Frame(self.mainBody) # Name list
        self.fieldList.grid(row=2,column=2, sticky=W)
        #/Staff canvas
        
        self.bottom  = Frame(self.mainBody,width=10,height=10,)
        self.bottom.grid(row=6,column=2, sticky=W)

        # /Content
        
        # SUMMAARY
        self.gapSUM = Frame(self.mainBody, width=20,) # GAP for expenses
        self.gapSUM.grid(row= 2, column=3)
        self.gapSummary = Frame(self.mainBody,width=50)
        self.gapSummary.grid(row=2, column=6)         # Gap for Type expenses
        self.fieldSummary =Frame(self.mainBody,width=5,)
        self.fieldSummary.grid(row=2, column=7, sticky= W)
        #/SUMMARY
        
        #/Frame >>>

        #Header >>>
        imgLogo = Canvas(logoFrame, width=420, height=115)
        imgLogo.grid(row=1,column=1)
        self.img = PhotoImage( file = 'logo.gif')
        imgLogo.create_image(10,10, image = self.img, anchor= NW)
        
            
        Label(title,height=1).grid(row=1, column=1)#Gap from top
        #Label(title, font='mono -36 bold', text="Project PY").grid(column=2,sticky=E)
        Label(self.header,width=3).grid(row=3,column=0,sticky=W)
        Label(self.header,text='File name: ', font='cornsilk -20 bold').grid(row=3, column=1, sticky=W)
        Label(self.header,width=2).grid(row=3, column=3) #SPACE
        self.box = Label(self.header,relief='sunken',width=25,font='Arial -15 bold',anchor=W)
        self.box.grid(row=3,column=2)

       
        
        Button(self.header, text='Browse...',width=10,font='mono -15 bold', bg='lightblue',
               command=self.open_file).grid(row=3, column=4,)
        Label(self.header,width=3,).grid(row=3, column=5) # SPACE
        Button(self.header, text="Process",width=20,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=3, column=6,)
        Label(self.header,width=3).grid(row=3, column=7)
        Button (self.header, text="Show/Hide Expenses", width = 15, font = 'mono -15 bold',
                command=self.break_Down).grid(row=3, column=8)
        
        #/Header >>>
        

        #self.combo(header)  #Combo box
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
        
        if self.processUsed == True:
            self.leftFrame.destroy()
        filename=self.box['text'] # gets value from self.box
##        if self.browseActive == True:
##            if self.check_combo(self.browsedFile) == True: # Add only to combo box
##                self.fileUsed.append(self.browsedFile)     # if not already Used
##            self.browseActive= False                # Resets browse button status
##            filename=self.browsedFile

        self.reader=Demonstrator(filename)
        self.listAllStaff()
        self.staff_Frame()
        self.notify()
        self.processUsed = True
        

    def open_file(self):
        '''Ability to browse the file in your computer'''
        
        self.browsedFile = os.path.basename(askopenfilename(filetypes=[('','')]))
        self.box['text'] = self.browsedFile
        print('lol')
        #self.box.set(self.browsedFile) 
        self.browseActive= True # To mark that this function has been used.
        

##    def check_combo(self,filename):
##        '''Check If file alreadi is in combo box'''
##
##        for file in self.fileUsed:
##            if file == filename:
##                return False
##        return True  
##        
##    def combo(self,frame):
##        '''Creates a Combo box and gives 3 default files'''
##        
##        self.box_value = StringVar()
##        self.box = ttk.Combobox(frame, textvariable=self.box_value,
##                                state='readonly') # Creates a combo box
##        self.fileUsed=['Demomax.xlsx'] # Default combo list
##        self.box['values'] = (self.fileUsed) 
##        self.box.current(0) # Current value
##        self.box.grid(row=3, column=2)
    
    def myfunction(self,event):
        '''Creates Scroll bar for Canvas'''
        
        self.staffCanvas.configure(scrollregion = self.staffCanvas.bbox("all"),width=325, height=400)


    def listAllStaff(self,):
        ''' Make a list of all staff '''

        self.leftFrame = Frame (self.mainBody,)
        self.leftFrame.grid(row=4,column=2, sticky = W)
        
        self.leftCanvas(self.leftFrame)
        line=1
        self.var  = IntVar() #  Must be self. to disable hover.
        staffName = self.reader.staffName()
        for name in staffName:
            self.NameList  = Radiobutton (self.bodySummary, width=17, text= staffName[name], font= 'arial -20 bold',
                               bg='grey', anchor= W, variable = self.var, value = name, pady = 0,
                                          ).grid(row=line, column=2, sticky=W)
            amount = self.get_Total_Cost_By_Name(name)
            self.TotalCost = Label (self.bodySummary,pady=3, width=10, text="\u00A3"+str(amount), font= 'arial -20 bold',
                                bg='grey', ancho=W).grid(row=line, column=3,)
            line +=1

    def leftCanvas(self,frame):
        '''creates canvas for stafff'''
        
        self.staffCanvas = Canvas (self.leftFrame,)  # 1
        self.bodySummary = Frame (self.staffCanvas) #2
        myscrollbar = Scrollbar(self.leftFrame, orient="vertical", command=self.staffCanvas.yview) #3
        self.staffCanvas.configure(yscrollcommand = myscrollbar.set) #4
        myscrollbar.pack(side="right",fill='y') #5
        self.staffCanvas.pack(side="left") #6
        self.staffCanvas.create_window((0,0), window=self.bodySummary, anchor= 'nw')
        self.leftFrame.bind("<Configure>", self.myfunction)
        frame.bind("<Configure>", self.myfunction)

        
    def get_Total_Cost_By_Name(self,ID):
        '''Displays cost for each staff '''
        
        staff_Cost = self.reader.displayStaffCost()
        for cost in staff_Cost:
            if cost == ID:
                return staff_Cost[cost]

    def break_Down(self):
        '''Creates a break down list of selected person (layout)'''

        if self.activeBR:
            self.destroy_Break_Down()
            
        
            
        self.field     = Frame(self.mainBody,)              # Break down field
        self.field.grid(row=2, column=4, sticky = W)


        self.middleFrame    = Frame(self.mainBody)          #Break down Content
        self.middleFrame.grid(row=4,column=4, sticky=NW)
        

        self.totalSummary = Frame(self.mainBody,)           # Spending Type
        self.totalSummary.grid(row=4, column= 7, sticky=N)

        
        self.activeBR = True
        self.staffID = self.var.get()

        Label(self.field,width=10,text='Date', font='arial -20 bold').grid(row=1,column=1)
        Label(self.field,width=10,text='Location', font='arial -20 bold').grid(row=1,column=2)
        Label(self.field,width=15,text='Reason', font='arial -20 bold').grid(row=1,column=3)
        Label(self.field,width=10,text='Cost', font='arial -20 bold').grid(row=1,column=4)

        #Label(self.fieldSummary,width=20).grid(row=1,column=0)
        Label(self.fieldSummary, width=10, text='Reason', font='arial -20 bold').grid(row=1, column=1)
        Label(self.fieldSummary, width=10, text='Total', font =' arial -20 bold').grid(row=1, column=2)

        self.work_out_rows()
        self.spendingType()

    def work_out_rows(self,):
        '''Generates list of rows for expenses to be ready to put in values'''

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.expensesCanvas = Canvas(self.middleFrame, width=550)
        self.body           = Frame(self.expensesCanvas,)
        #myscrollbar = Scrollbar(self.middleFrame, orient="vertical", command=self.expensesCanvas.yview)
        #self.expensesCanvas.configure(yscrollcommand = myscrollbar.set)
        #myscrollbar.pack(side="right",fill='y')
        self.expensesCanvas.pack(side="left")
        self.expensesCanvas.create_window((0,0),window=self.body, anchor='nw')
        #self.body.bind("<Configure>", self.myfunctionTwo) #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        staff_List = self.reader.displayStaff_Names()
        self.expenseline = 2 # Also for condition to appear scroll bar for expenses.
        for row in  staff_List:
            if self.staffID == row[0]:     
                index = 1    
                date = row[index]
                location = row[index+2]
                reason = row[index+3]
                cost =row[index+4]
                self.add_row(date, location, reason, cost,self.expenseline)
                self.expenseline +=1
                
        if self.expenseline > 11:
            self.myscrollbar2 = Scrollbar(self.middleFrame, orient="vertical", command=self.expensesCanvas.yview)
            self.expensesCanvas.configure(yscrollcommand = self.myscrollbar2.set)
            self.myscrollbar2.pack(side="right",fill='y')
            self.body.bind("<Configure>", self.myfunctionTwo)
            self.scrollBarActive = True

        if self.scrollBarActive:
            if self.expenseline < 11:
                self.myscrollbar2.destroy()
                self.scrollBarActive = False
                
                           

    def myfunctionTwo(self,event):
        self.expensesCanvas.configure(scrollregion=self.expensesCanvas.bbox("all"),height= 200,width= 550)
    
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
        #Label(self.totalSummary,).grid(row=1,column=0)
        expense = self.reader.displaySpendings(self.staffID)
        for key in expense:
            self.spend = Label(self.totalSummary, width=10, text=key, font='arial -20 bold', bg='grey')                    
            self.spend.grid(row=line,column=1,sticky=N)
            self.CostSum = Label(self.totalSummary,width=10, text=expense[key], font='arial -20 bold', bg='grey')                
            self.CostSum.grid(row=line,column=2,sticky=N)
            line +=1
            
    def destroy_Break_Down(self):
        '''Destroys frames '''
        
        self.body.destroy()
        self.field.destroy()
        self.totalSummary.destroy()

    def notify(self):
        ''' Get the value from each question to display them on screen '''
        
        self.total['text'] = str(self.reader.displayTotalSum())

    def quitMessage(self,):
        '''Exit programme'''
        
        message = messagebox.askyesno(title="Quit", message="Are you sure want to exit?",icon= "warning")    
        if message:
            top.destroy() # On Yes exits application.


if __name__ == "__main__":
    top =Tk()
    top.geometry('10920x1080')
    top.title("Stella")
    top.grid()
    
    app = TaskGUI(top)

    top.mainloop()
