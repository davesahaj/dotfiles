import os
import random
from subprocess import call
from datetime import date
import datetime


path = os.getcwd() #current directory

def calcdate():
    d0 = date(2020, 3, 7) # Commit start date YYYY MM DD
    current_time = datetime.datetime.now() #Present date
    d1 = date(current_time.year,current_time.month,current_time.day)# current date object
    
    delta = d1 - d0 # days from start date to current date.
    
    return(delta.days) #return number of days

rstart = calcdate() #number of days from start date to end

filelist = []

for root, dirs, files in os.walk(path):

    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for file in files:
        if file!="commitbot.py":
            
            if rstart == 1:
                print("DATE REACHED QUITTING!")
                quit()
            gitfile = os.path.join(root, file)
            call(['git','add',gitfile])

            rnum = random.randint(rstart-4, rstart)
            rstart = rstart - 1
            dstr = str(rnum) + " day ago"

            call(['git', 'commit', '--date', dstr, '-m', 'Arch config files'])
