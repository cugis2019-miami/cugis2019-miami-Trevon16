studentallinfo= [['steve',32,'male'],['lia',28,'female'],['Vin',45,'male'],['Katie',38,'female']]
print(studentallinfo)

df =pandas.DataFrame(studentallinfo)
print(df)
df2=pandas.DataFrame(studentallinfo)
print(df2)








#day4
import pandas
import plotly

studentlist = [["{Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
print(studentlist)



studentlistdf = pandas.DataFrame(studentlist, columns = ["name","age","gender"],index = [1,2,3,4])



#graph our data
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])















import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go


df = pd.read_excel("GISdata.Xlsx", sheet_name = "womenOccupation")



womenoccupation = go.Bar(x= df["occupation"], y=df["women"])


plot([womenoccupation])


fig = go.Figure(data=[womenoccupation])

plot(fig)









































#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1


uname = input("Hello, What is your username?")

print("Hello",uname = ".",)

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print(""oh..okay")

if question =="y":
    print("I'm thinking of a number between 1 & 10"")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower...")
    if guess < number:
        print("Guess higher..")
        while guess != number:
            tries += 1
            guess = int(input("Try again: "))
            if guess < number:
                print("Guess Higher")
                if guess == number:
                    print("you're right! you win! The number was", number, \
                          "and it only", treis, "tries!")
    





























import turtle
import os

wn = 























































































