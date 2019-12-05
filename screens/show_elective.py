from tkinter import *
import sqlite3

class Show_elective:
    def __init__(self,subject):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
              
        # Setting the background

        connection = sqlite3.connect('databases/student.db')
            
        cursor = connection.cursor()
            
        sql_command = '''SELECT NAME,USN FROM ELECTIVES WHERE P_E='{}';'''.format(subject)
            
        cursor.execute(sql_command)
            
        row = cursor.fetchall()
            
        print(row)
        print(len(row))
        
        if(len(row) == 0):
            sql_command = '''SELECT NAME,USN FROM ELECTIVES WHERE O_E='{}';'''.format(subject)
            
            cursor.execute(sql_command)
            
            row = cursor.fetchall()

        usn = [x[1] for x in row]
        name = [x[0] for x in row]

        b = Label(self.c,text="USN",bg="red",fg='white',width=25,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=0)
        
        b = Label(self.c,text="NAME",bg="red",fg='white',width=25,height=2,font=('palatino',20,'bold'))
        b.grid(row=0,column=1)

        for i in range(len(usn)): #Rows
            b = Label(self.c,text=usn[i],bg="white",width=40,height=2,font=('palatino',30,'bold'))
            b.grid(row=i+1, column=0)
        i = 0
        for i in range(len(name)): #Rows
            b = Label(self.c,text=name[i],bg="white",width=40,height=2,font=('Times',30,'bold'))
            b.grid(row=i+1, column=1)

        print(usn)
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=200,height=30)

        def back():
            self.root.destroy() 

        
        
        self.c.pack()
        self.root.mainloop()