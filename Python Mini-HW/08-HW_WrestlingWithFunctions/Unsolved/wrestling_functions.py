import os
import csv

path = "/Users/redea/gwu-arl-data-pt-09-2020-u-c/02-Homework/03-Python/01-Mini-Assignment/3.08-HW_WrestlingWithFunctions/Resources/WWE-Data-2016.csv"
wrestlerdata = os.path.join(path)
def getpercentages(wrestlerdata):
            wrestler = str(wrestlerdata[0])
            won = int(wrestlerdata[1])
            lost = int(wrestlerdata[2])
            drawn = int(wrestlerdata[3])
            total_matches = won + lost + drawn
            percent_won = (won/total_matches)*100
            percent_lost = (lost/total_matches)*100
            percent_drawn = (drawn/total_matches)*100
            if percent_lost > 50:
                type_of_wrestler = "Jobber"
            else:
                type_of_wrestler = "Superstar" 
                print(f"Stats for {wrestler}: ")
                print(f"Win Percent: {percent_won}")
                print(f"Loss Percent: {percent_lost}")
                print(f"Draw Percent: {percent_drawn}")
                print(f"{wrestler} is a {type_of_wrestler}")
with open(wrestlerdata, 'r') as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    name_to_check = input("What wrestler do you want to look for? ")
    for row in csvfile:
        if(name_to_check == row[0]):
            getpercentages(row)            
  
            
  
    
   