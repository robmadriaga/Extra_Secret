# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:42:20 2020

@author: markm
"""

from faker import Faker
fake = Faker()
from random import randrange
from datetime import date, timedelta #importing date and timedelta for date calculation
import random #importing random for date generation
import os

def generateName():
    name = fake.name()
    return(name)
    
def generateUsername(name, birthday):
    Name = name.split() #assume a space between first and last name
    firstname = Name[0];
    Date = birthday.split('-') #date format is year-month-day
    year = Date[0];
    return firstname+year #creates username from firstname and year
    
def generateAddress():
    return fake.address()
    
def nameGeneration(birthday):
    name = generateName()
    birthday = generateBirthday()
    user = generateUsername(name, birthday)
    email = generateEmail(user)
    return name, user, email;
    

def generatePassword():
    #set up all the types of characters
    password = "";
    numlist = [0,1,2,3,4,5,6,7,8,9]
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = []
    for g in lower:
        upper.append(g.capitalize())
    specials = ['!', "&","$", "#","@"]
    
    i = 0
    while (i < 13):
        #determine what type of character will be added
        rand1 = randrange(4)
        
        if (rand1 == 0):
            password += str(numlist[randrange(8)])
        elif (rand1 == 1):
            password += lower[randrange(25)]
        elif (rand1 == 2):
            password += upper[randrange(25)]
        elif (rand1 == 3):
            password += specials[randrange(5)]
        
        i+=1
    return(password)

def generateInformation():
    address = generateAddress()
    bday = generateBirthday()
    name, user, email = nameGeneration(bday)
    password = generatePassword()
    return name, user, email, bday, password, address, "https://thispersondoesnotexist.com/image";
'''
def writeToFile(name, username, email, birthday, password, address,  image, filename):
    file = open(filename, "wt")
    file.write(name+"\n"+username+"\n"+email+"\n"+birthday+"\n"+password+"\n"+address+"\n"+image+"\n")
    file.close()
  '''  
def generateAccount(number):
    
    i = 0
    while i < number:
        name, username, email, birthday, password, address, image = generateInformation()
       # writeToFile(name, username, email, birthday, password, address, image, createFileName())
        i+=1


    return ('%s \n %s \n %s \n %s \n %s \n %s \n %s \n' $(name, username, email, birthday, password, address, image))
        
def generateAccountP(number,password):
    i = 0
    while i < number:
        name, username, email, birthday, p, address, image = generateInformation()
       # writeToFile(name, username, email, birthday, password, address, image, createFileName())
        i+=1
        
    return ('%s \n %s \n %s \n %s \n %s \n %s \n %s \n' $(name, username, email, birthday, password, address, image))

def generateBirthday(): 
    today =date.today() #getting the current date
    
    daysBack=random.randint(5510, 18250) #randomly picking a number of days between 14 and 50 years

    endDate=today-timedelta(daysBack) #calculating the date [daysBack] form the current date
    return str(endDate)

def generateEmail(username):
    
    email=username+'@mailnesia.com' #adding the mailing adress to username

    return email
'''
def createFileName():

    dir_path=os.path.dirname(os.path.realpath(__file__)) #get the directory the python file is located in
    
    currentFileNum=0

    fileName='profiles'+str(currentFileNum)+'.txt' #set the name of the file

    filePath=str(dir_path)+'/'+fileName #set the path to where the output file should be

    fileExist=os.path.isfile(filePath) #check if the file exists already
    while(fileExist): # while a file of the same name exists loop untill   number is reached that doenst have the same name

        currentFileNum=currentFileNum+1 #increment file name
        
        fileName='profiles'+str(currentFileNum)+'.txt' #rename file
        filePath=str(dir_path)+'/'+fileName #set the new path



        fileExist=os.path.isfile(filePath) #check if it exists

    return fileName 
'''

random.seed() # seeing the random funciton
generateAccount(2)
