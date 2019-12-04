from tkinter import *
from screens.teach_attendance import *

from screens.sub_marks import *

class Teach_marks_Authenticate:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")


        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((700, 400),text="AUTHENTICATION PLEASE!", fill="white", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))
        self.c.create_text((540, 500), text="ENTER THE DETAILS", fill="white", anchor="nw"
                           ,font=self.fnt)
        
        # Setting the login entry boxes
        self.c.create_text((650, 610), text="Username: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 615, anchor=NW, window=self.button1)
        
        
        self.c.create_text((650, 710), text="Password: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'),show="*")
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 715, anchor=NW, window=self.button2)
        
        
        self.loginButton = Button(self.c,text="Submit",width=15,height=2,bg='red',fg='white',command=lambda:authenticate(),
                                  font=("Times",15,'bold'))
        self.loginButton.configure(width=15,relief=FLAT)
        login_button_window = self.c.create_window(800,860,anchor=NW,window=self.loginButton)
        
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=200,height=30)

        def back():
            self.root.destroy() 

        def authenticate():
            username = self.button1.get()
            password = self.button2.get()
            
            if username.upper() == password.upper() and username.upper() == "ADMIN": 
                a = Teach_marks()
        
        self.c.pack()
        self.root.mainloop()
        
class Teach_marks:
        
        
    def __init__(self):
            
        
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        
        self.c.create_text((630, 290), text="Enter USN: ", fill="black", anchor="nw"
                           ,font=('Times',40,'bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 300, anchor=NW, window=self.button1)
        
        
        self.sub1 = Button(self.c,text='17CS51',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS51"))
        
        self.sub2 = Button(self.c,text='17CS52',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS52"))
        
        self.sub3 = Button(self.c,text='17CS53',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS53"))
        
        self.sub4 = Button(self.c,text='17CS54',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS54"))
        
        self.sub5 = Button(self.c,text='17CS552',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS552"))
        
        self.sub6 = Button(self.c,text='17CS562',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=3, font=("Times",15,'bold'),command=lambda:give_marks(self,"17CS562"))
        
        self.sub1.place(x=850,y=500,width=200,height=30)
        self.sub2.place(x=850,y=560,width=200,height=30)
        self.sub3.place(x=850,y=620,width=200,height=30)
        self.sub4.place(x=850,y=680,width=200,height=30)
        self.sub5.place(x=850,y=740,width=200,height=30)
        self.sub6.place(x=850,y=800,width=200,height=30)
        
        def give_marks(self,subject):
            usn = self.button1.get()
            a = Sub_marks(subject,usn)
        
        self.c.pack()
        self.root.mainloop()
    
        
        
    