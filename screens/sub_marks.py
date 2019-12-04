from tkinter import * 
import sqlite3
import math

class Sub_marks:
    def __init__(self,sub="17CS52",usn="1MV17CS018"):
        
        self.sub = sub
        self.usn = usn
        
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("{}".format(sub))
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
        
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        
        self.c.create_text((650, 410), text="Test 1: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 10, relief = FLAT)  
        button1_window = self.c.create_window(800, 415, anchor=NW, window=self.button1)
        
        self.submit = Button(self.c,text="Submit",width=15,height=2,bg='red',fg='white',command=lambda:submit_test1(self),
                                  font=("Times",15,'bold'))
        self.submit.configure(width=15,relief=FLAT)
        submit_button = self.c.create_window(720,470,anchor=NW,window=self.submit)
        
        
        
        
        self.c.create_text((650, 570), text="Test 2: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'))
        self.button2.configure(width = 10, relief = FLAT)  
        button1_window = self.c.create_window(800, 575, anchor=NW, window=self.button2)
        
        self.submit = Button(self.c,text="Submit",width=15,height=2,bg='red',fg='white',command=lambda:submit_test2(),
                                  font=("Times",15,'bold'))
        self.submit.configure(width=15,relief=FLAT)
        submit_b = self.c.create_window(720,630,anchor=NW,window=self.submit)
        
        
        
        
        self.c.create_text((650, 730), text="Test 3: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button3 = Entry(self.c,font=('Times',20,'bold'))
        self.button3.configure(width = 10, relief = FLAT)  
        button1_window = self.c.create_window(800, 735, anchor=NW, window=self.button3)
        
        self.submit = Button(self.c,text="Submit",width=15,height=2,bg='red',fg='white',command=lambda:submit_test3(),
                                  font=("Times",15,'bold'))
        self.submit.configure(width=15,relief=FLAT)
        submit_b = self.c.create_window(720,800,anchor=NW,window=self.submit)
        
        
        self.final = Button(self.c,text="Calculate Final IA",width=15,height=2,bg='yellow',fg='black',command=lambda:calc_final(),
                                  font=("Times",20,'bold'))
        self.final.configure(width=25,relief=FLAT)
        final_b = self.c.create_window(1100,630,anchor=NW,window=self.final)
        
    
        
        def submit_test1(self):
            test1 = int(self.button1.get())
            print(type(test1))
            print(test1)
            connection = sqlite3.connect('databases/student.db')
            cursr = connection.cursor()
            sql_c = '''UPDATE MARKS SET TEST_1 = {} WHERE USN='{}' AND SUB_CODE='{}';'''.format(test1,self.usn,self.sub)
            
            cursr.execute(sql_c)
            print("Successful")
            
            connection.commit()
    
        def submit_test2():
            test2 = int(self.button2.get())
            connection = sqlite3.connect('databases/student.db')
            cursr = connection.cursor()
            sql_c = '''UPDATE MARKS SET TEST_2 = {} WHERE USN='{}' AND SUB_CODE='{}';'''.format(test2,self.usn,self.sub)
            
            cursr.execute(sql_c)
            print("Successful")
            
            connection.commit()
        
        def submit_test3():
            test3 = int(self.button3.get())
            connection = sqlite3.connect('databases/student.db')
            cursr = connection.cursor()
            sql_c = '''UPDATE MARKS SET TEST_3 = {} WHERE USN='{}' AND SUB_CODE='{}';'''.format(test3,self.usn,self.sub)
            
            cursr.execute(sql_c)
            print("Successful")
            
            connection.commit()
            
        def calc_final():
            connection = sqlite3.connect('databases/student.db')
            cursr = connection.cursor()
            
            sql_c = '''SELECT TEST_1,TEST_2,TEST_3 FROM MARKS WHERE USN='{}' AND SUB_CODE='{}' ;'''.format(self.usn,self.sub)
            
            cursr.execute(sql_c)
            
            row = cursr.fetchall()
            print(row)
            test1,test2,test3 = (x for x in row[0])
            
            print(test1,test2,test3)
            
            sql_c = '''UPDATE MARKS SET FINAL_IA = {} WHERE USN = '{}' AND SUB_CODE = '{}' ;'''.format(math.floor(((test1+test2+test3)/3)),self.usn,self.sub)
            
            cursr.execute(sql_c)
            
            connection.commit()
            
            self.root.destroy()
        
        self.c.pack()
        
        self.root.mainloop()
        


