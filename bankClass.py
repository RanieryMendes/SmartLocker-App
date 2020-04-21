import csv
import pandas as pd 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from data import token
import os

import dropbox




class Bank():
    account =""
    login=""
    password = ""

    def __init__(self):
        self.account = "basic"
        self.login = "Zezin"
        self.password = "13324"

    def initalization_dropbox(self):
        dbx = dropbox.Dropbox(token)
        print("Test if connection with API works")
        dbx.users_get_current_account()
        #print(dbx.files_list_folder("/Apps/locker/"))

        with open("password.csv", "wb") as f:
            metadata, res = dbx.files_download(path="/apps/locker/teste.csv")
            f.write(res.content)

        
        #dbx.files_download_to_file(download_path="/password.csv", path="/apps/locker/teste.csv", rev='015a38af855ff11000000019efecaa0')
    

    
        
    



    def savingInfo(self):
        with open ("password.csv", "a+") as pw:

            writer = csv.writer(pw, delimiter=",")

            writer.writerow([self.account, self.login, self.password])

        dbx = dropbox.Dropbox(token)
        print("Test if connection with API works")
        dbx.users_get_current_account()    

        with open("password.csv", 'rb') as pw_drop:

            dbx.files_upload(pw_drop.read(), path="/apps/locker/teste.csv", mode= dropbox.files.WriteMode('overwrite'), autorename=True)
            

            print("Congratulations. You're all set!")
    
    def updateInfo(self, userAccount, userLogin, userPassword):
        self.account = userAccount
        self.login = userLogin
        self.password = userPassword


    def showServices(self):
        self.initalization_dropbox()
        col_list = ["Service", "Login", "Password"]
        df = pd.read_csv("password.csv", usecols=col_list)
        print("Here is the list with all service accounts we have:")
        print(df["Service"])

    def getInfo(self, account):
        userInfo =   pd.read_csv("password.csv")
        userInfo = userInfo[userInfo["Service"] == account]
        print('\nHere is your information: \n')
        print(userInfo)

        
    