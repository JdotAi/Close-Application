import os
from datetime import datetime
import time



applicationName = input("Give me the name of the application you want to close: ")
terminatorTime= input("What time do you want to close the application: ")

timeNow = datetime.now()
timeString = timeNow.strftime("%H:%M")


codeStoper = False

while(not codeStoper):
    while timeString!= terminatorTime:
        time.sleep(10)
        timeNow = datetime.now()
        timeString = timeNow.strftime("%H:%M")
    os.system("killall "+applicationName)
    codeStoper = True





