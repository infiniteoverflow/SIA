from tkinter import *
from screens.CvsTA import *
from screens.Highest import *

class Analysis:
    def __init__(self,branch):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Attendence")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/electives12.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")

        self.b1 = Button(self.c,text='TOTAL APPEARED / TOTAL PLACED',bg='white',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",20,'bold'),command=lambda:Appeared(branch))
        self.b1.place(x=700,y=400,width=600,height=80)

        self.b2 = Button(self.c,text='HIGHEST PACKAGE',bg='white',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",20,'bold'),command=lambda:Package(branch))
        self.b2.place(x=700,y=500,width=600,height=80)


        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1400,y=900,width=100,height=40)



        def back():
            self.root.destroy() 


        def Appeared(branch):
            dd = CvsTa(branch) 


        def Package(branch):
            ee =  Highest(branch)



        self.c.pack()
        self.root.mainloop()