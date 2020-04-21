from bankClass import Bank
import csv

import tkinter as tk 
from tkinter import *
from tkinter import Text, filedialog
from PIL import ImageTk, Image 
import os
from pandastable import Table, TableModel
userSecret = Bank()



def getData(entry1, entry2, entry3, labetset, bot):
    
    bot.destroy() #destroy button just clicked
    
    #get inputs from the user
    dataAccount = entry1.get()
    dataLogin = entry2.get()
    dataPassword = entry3.get()
    
    userSecret.updateInfo(dataAccount, dataLogin, dataPassword)
    userSecret.savingInfo()
    
    newFrame = Label(labetset, text= "Congratulations! You're all set!", font=('Courier', 18, 'bold'), bg='black', fg='white', compound=CENTER)
    newFrame.grid(row = 10, columnspan =3)
    newFrame.place(y= 300, x=20)

def retrievePassword(root, userSecret):
    root.destroy()

    hoje = Tk()
    hoje.geometry("480x300")
    hoje.title('SmartLocker')

    FILENAME = Image.open('photo.png')
    tk_img = ImageTk.PhotoImage(FILENAME) 

    frame1 = tk.Frame(hoje, bg = 'black')
    frame1.place(relwidth=1.0, relheight=1.0)
    
    frame1.place(relwidth= 1.0, relheight=1.0)
    labetse2 = Label(frame1, image= tk_img)
    labetse2.pack()
    labetset = Label(frame1, image= tk_img)
    #labetset.grid(row=0, column=0)
    labetset.pack()
    labetset.place(relwidth=1.0, relheight=0.6)

    frameText = Label(labetset, text="Take a look on what info we have!", bg='black', fg='white', font=('Courier', 17))
    #frameText.grid(row=2, columnspan=3)
    frameText.place(x= 15, y= 280)

    #userSecret.showServices()

    toolbar = tk.Frame(labetset)
    
    pt = Table(labetset, width=480, height=150)
    
    
   
    button = tk.Button(frame1, text="Quit",font='Courier',  fg='red' , background='blue', highlightbackground='green', command= quit)
    button.place(x=220, y=250)
    buttonSwitch = tk.Button(frame1, text="Add New Account",font='Courier',  fg='red' , background='blue', highlightbackground='green', command= lambda :frameAddPassword(hoje))
    buttonSwitch.place(x=280, y=250)
    
    pt.importCSV(filename='password.csv')
    pt.show()

    pt.setColumnColors(cols=2, clr='red')
    
   

   #button.place(x=100, y =100)
   
   
   

    hoje.mainloop()

      

def setPassword():


    setting = True

    while(setting):

        print("Let's set up this new password!")
        new_account = input("Enter the name of the service: ")
        new_login = input("Enter the service's login: ")
        new_password = input("Enter the service's password: ")

        print("Please confirm all the information below is correct.")
        print("Login: " + new_login + "  " + "Password: " + new_password)

        confirmation = True

        while(confirmation):

            check = input("Enter Y = correct or N = There's wrong info \n")

            if(check== "Y" or check =="y"):
                setting = False
                confirmation = False

            elif (check == "N" or check == "n"):
                setting = True 
                confirmation = False
        
            else:
                print("Invalid Answer. Enter the answer again")
            # do nothing with the while loop and boolean confirmation.

    return new_account, new_login, new_password




def frameAddPassword(root):
    root.destroy()

    hoje = Tk()
    hoje.geometry("400x400")
    hoje.title('SmartLocker')

    """
    FILENAME = Image.open('photo.png')
    tk_img = ImageTk.PhotoImage(FILENAME)
    """
    
    canvas = tk.Canvas(hoje, width=400, height=400)
    FILENAME = Image.open('photo.png')
    tk_img = ImageTk.PhotoImage(FILENAME) 

    frame1 = tk.Frame(hoje, bg = 'black')
    frame1.place(relwidth=1.0, relheight=1.0)
    
    #frame1.place(relwidth= 0.9, relheight=0.9, relx = 0.1, rely=0.1)

    labetset = Label(frame1, image= tk_img)
    labetset.grid(row=1, column=1)
    labetset.place(relwidth=1.0, relheight=1.0)

    
    
    #startProcess = tk.Button(canvas, text="Store New Password",padx=25, pady=20, fg="purple", bg="white")
    #startProcess.pack()

   # label1 = tk.Label(frame, text="Welcome to the SmartLocker APP", fg="white", bg="red")r
    #label1.pack()

    label2 = tk.Label(frame1, text= "Account: ", font='Courier', bg="purple", width = 18)

    #label2.place(relwidth=0.4, relheight=0.4, relx=20)
    
    label3 = tk.Label(frame1, text= "Login: ",font='Courier', bg="purple", width = 18  )
    
    label4 = tk.Label(labetset, text= "Password: ",font='Courier', bg="purple", width = 18 )
  

 
    label2.grid(row=1, sticky='E')
    label2.place(y=120, x= 10)
    label3.grid(row=2, sticky ='E')
    label3.place(y=180, x=10)
    label4.grid(row=3, sticky= 'E')
    label4.place(y=240, x=10)

    entry1 = tk.Entry(labetset, bg="purple",font='Courier', fg="white", width= 17 )
    
    #entry1.place(x= 40 , y = 60)
    #entry1.pack(side=BOTTOM, pady= 10)
    entry2= tk.Entry(labetset, bg="purple", fg="white",font='Courier', width= 17)
    #entry2.place(x= 100 , y = 50)
    #entry2.pack(side=BOTTOM)
    entry3 = tk.Entry(labetset, bg="purple", fg="white",font='Courier', width= 17)
    #entry3.pack( pady = 20, padx= 20)
    
    entry1.grid(row=1, column=1)
    entry1.place(y=120, x=220)
    entry2.grid(row=2, column=1)
    entry2.place(y=180, x= 220)
    entry3.grid(row=3, column=1)
    entry3.place(y=240, x=220)
    

    confirm = tk.Button(labetset, text="Add it up into my SmartLocker", font='Courier',
    bg='yellow', command= lambda:getData(entry1, entry2, entry3, labetset, confirm))
    confirm.grid(columnspan=2, row=5)
    confirm.place(x=100, y=330)

    saida = Button(labetset, text='Quit', font='Courier',  fg='red' , background='blue', highlightbackground='green', command= quit)

    saida.grid(row=7, columnspan=3)
    saida.place(x=40, y=30)

    switch = Button(labetset, text='Get a Password', font='Courier',  fg='red' , background='blue', highlightbackground='green', command= lambda:retrievePassword(hoje, userSecret))
    switch.grid(row=9, columnspan=4)
    switch.place(x= 265, y=360)
    



    hoje.mainloop()

    
 
    


root = tk.Tk()
root.title('SmartLocker')
root.iconbitmap('cadeado.icns')
canvas = tk.Canvas(root, width=400, height=400)
FILENAME = Image.open('photo.png')
tk_img = ImageTk.PhotoImage(FILENAME)

canvas.create_image(200,200, image=tk_img)
canvas.pack()




label1 = Label(canvas, text="Welcome to SmartLocker", bg="black", fg="red", font=("Helvetica bold", 15, UNDERLINE))

label1.place(width= 40, height=20)
label1.pack(padx= 100, pady=30)
 
button_OptionOne = tk.Button(canvas, text= "Insert New Account", width=15, height=2, font= 'Helvetica' ,fg = 'purple', background='red',highlightbackground = 'green', compound =CENTER, command= lambda : frameAddPassword(root))
button_OptionOne.place(relheight= 0.8, relwidth=0.2)


button_OptionTwo = tk.Button(canvas, text="Retrieve an account info", width=25, height=2, font='Helvetica', highlightbackground = 'green',  bg='red', fg= 'purple', compound=CENTER, command=lambda : retrievePassword(root, userSecret))
button_OptionTwo.place(relheight= 0.8, relwidth=0.2)

button_OptionOne.pack(side=LEFT, padx=100, pady=50)

button_OptionTwo.pack(side= RIGHT, padx=80, pady= 50)



root.mainloop()





def first_Frame():


    root = tk.Tk()
    background = "giphy.gif"
    photo = tk.PhotoImage( file = background, height=300, width=400)

    canvas = tk.Canvas(root, height= 300, width= 400, bg="#203C42")

    label1 = Label(root, image= photo)
    label1.place(height=200, width=130)
    label1.place(x=0.3,y=0.3,width=1,height=1)

    labelText = Label(Text="Welcome to SmartLocker", bg="black", fg="white", font=("Helvetica", 50))



    label1.pack()






"""
print("Welcome to your password locker \n \nIf you want to add a new password enter 1 \nIf you want to retrieve a password enter 2")
answer = int(input('What do you want to do? \n'))

userPassword =""
userLogin =""
userAccount=""


if (answer == 1):

    print("Okay. Let's set up this new password")
    userAccount, userLogin, userPassword = setPassword()
    
    userSecret.updateInfo(userAccount, userLogin, userPassword)
    userSecret.savingInfo()  


elif (answer==2):
    print("Let's get this password, folk! \n")
    userSecret.showServices()
    nameService = input("From which service do you want us to provide you your info: \n")
    userSecret.getInfo(nameService)

    



print("")
print("Thanks for using our locker! See you next time!\n")
"""
