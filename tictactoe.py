import imp
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint



#Global variables
Activeplayer=1
p1=[] # what player 1 selected
p2=[] # what player 2 selected

root=Tk()

root.title('Tic-Tac-Toe')

# Adding buttons
bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,sticky='snew',ipadx=50,ipady=50)
bu1.config(command=lambda :but_clicked(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=50,ipady=50)
bu2.config(command=lambda :but_clicked(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=50,ipady=50)
bu3.config(command=lambda :but_clicked(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=50,ipady=50)
bu4.config(command=lambda :but_clicked(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=50,ipady=50)
bu5.config(command=lambda :but_clicked(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=50,ipady=50)
bu6.config(command=lambda :but_clicked(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=50,ipady=50)
bu7.config(command=lambda :but_clicked(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=50,ipady=50)
bu8.config(command=lambda :but_clicked(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=50,ipady=50)
bu9.config(command=lambda :but_clicked(9))


def but_clicked(id):
    global Activeplayer
    global p1
    global p2
    
    if (Activeplayer==1):
        SetLayout(id,'X')
        p1.append(id)
        root.title('Tic-Tac-Toe : Player 2')
        print('Tic-Tac-Toe : Player 2')
        Activeplayer=2
        print('P1 {}'.format(p1))
        autoplay()

    
    elif(Activeplayer==2):
        SetLayout(id,'O')
        p2.append(id)
        root.title('Tic-Tac-Toe : Player 1')
        print('Tic-Tac-Toe : Player 1')
        Activeplayer=1
        print('P2 {}'.format(p2))
    
    
    checkwinner()
        

def SetLayout(id,playersymbol):
    if id==1:
        bu1.config(text=playersymbol)
        bu1.state(['disabled'])
        
    elif id==2:
        bu2.config(text=playersymbol)
        bu2.state(['disabled'])
        
    elif id==3:
        bu3.config(text=playersymbol)
        bu3.state(['disabled'])
        
    elif id==4:
        bu4.config(text=playersymbol)
        bu4.state(['disabled'])
        
    elif id==5:
        bu5.config(text=playersymbol)
        bu5.state(['disabled'])
        
    elif id==6:
        bu6.config(text=playersymbol)
        bu6.state(['disabled'])
        
    elif id==7:
        bu7.config(text=playersymbol)
        bu7.state(['disabled'])
        
    elif id==8:
        bu8.config(text=playersymbol)
        bu8.state(['disabled'])
        
    elif id==9:
        bu9.config(text=playersymbol)
        bu9.state(['disabled'])
    
def checkwinner():
    winner=0
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner=2
        
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner=1
    
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner=2
    
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner=1
    
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner=2
        
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner=1
    
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner=2
    
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner=1
    
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner=2
    
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner=1
    
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner=2
        
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner=1
    
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner=2
        
    if ((3 in p1) and (5 in p1) and (6 in p1)):
        winner=1
    
    if ((3 in p2) and (5 in p2) and (6 in p2)):
        winner=2
    
    if winner==1:
        messagebox.showinfo(title='Congratulations',message='Player 1 is the winner')
    
    elif winner==2:
        messagebox.showinfo(title='Congratulations',message='Player 2 is the winner')
        
    # elif winner !=1 and winner!=2:
    #     messagebox.showinfo(title='Drawn',message='Game is drawn')
    
def autoplay(): 
    emptycells=[]
    for cell in range(9):
        if (not((cell+1 in p1 ) or (cell+1 in p2))):
            emptycells.append(cell+1)
            
    Randindex=randint(0,len(emptycells)-1)
    but_clicked(emptycells[Randindex])
            
        
        
        
        

root.mainloop()