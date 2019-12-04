from tkinter import *
import sqlite3

class ShowMarks:
    def __init__(self,usn='1MV17CS018'):
        self.usn = usn.upper()
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("{} Details".format(self.usn))
        
        self.c = Canvas(self.root,bg = "white",height=2000,width=2024,cursor='pencil')
        
        
        b = Label(self.c,text="Sunject Code",bg="red",fg='white',width=20,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=0)
        
        b = Label(self.c,text="Test 1",bg="red",fg='white',width=20,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=1)
        
        b = Label(self.c,text="Test 2",bg="red",fg='white',width=20,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=2)
        
        b = Label(self.c,text="Test 3",bg="red",fg='white',width=20,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=3)
        
        b = Label(self.c,text="Final IA",bg="red",fg='white',width=20,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=4)
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.grid(row=10,column=2)
        
        connection = sqlite3.connect("databases/student.db")
        cursor = connection.cursor()
        
        sql_command = '''SELECT * FROM MARKS WHERE USN='{}';'''.format(usn)
        
        cursor.execute(sql_command)
        
        row = cursor.fetchall()
                
        subjects = [x[2] for x in row]
        test1 = [x[3] for x in row]
        test2 = [x[4] for x in row]
        test3 = [x[5] for x in row]
        final_ia = [x[6] for x in row]
        
        for i in range(1,len(subjects)+1): #Rows
            b = Label(self.c,text=subjects[i-1],bg="white",width=20,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=0)
            
        for i in range(1,len(test1)+1): #Rows
            if test1[i-1]==0:
                b = Label(self.c,text="-",bg="white",width=20,height=2,font=('palatino',30,'bold'))
            else:
                b = Label(self.c,text=test1[i-1],bg="white",width=20,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=1)
        
        for i in range(1,len(test2)+1): #Rows
            if test2[i-1]==0:
                b = Label(self.c,text="-",bg="white",width=20,height=2,font=('palatino',30,'bold'))
            else:
                b = Label(self.c,text=test2[i-1],bg="white",width=20,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=2)
            
        for i in range(1,len(test3)+1): #Rows
            if test3[i-1]==0:
                b = Label(self.c,text="-",bg="white",width=20,height=2,font=('palatino',30,'bold'))
            else:
                b = Label(self.c,text=test3[i-1],bg="white",width=20,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=3)
            
        for i in range(1,len(final_ia)+1): #Rows
            if final_ia[i-1]==0:
                b = Label(self.c,text="-",bg="white",width=20,height=2,font=('palatino',30,'bold'))
            else:
                b = Label(self.c,text=final_ia[i-1],bg="white",width=20,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=4)
        
        self.c.pack()
        
        def back():
            self.root.destroy()

        
        #self.c.pack()
        self.root.mainloop()
        
        def disp_details(self):
            pass
        
