from os import system
import keyboard
import msvcrt
import sys
import os

import listTofile
import backupFromlist

# Welcome
print("")
print("***XCopy Backup (G0LD edition)***")
print("*Select Directory to Copy* ")
print("")

parameters = "/S /Q /f /e /h /k /y"

if len(sys.argv) == 2:
   print("Except: Invalid Argument Two")
   sys.exit()
   try:
     sys.exit() # this always raises SystemExit
   except SystemExit:
     print("sys.exit() worked as expected")
   except:
     print("Something went horribly wrong")
elif (len(sys.argv) == 3):
     #print(sys.argv[1])
     x = sys.argv[1]
     y = sys.argv[2]
     #print(len(x) - 1)

     arg1 = x[0:9]
     arg2 = x[0:8]
     arg3 = x[0:7]
     arg4 = x[0:6]
     arg5 = x[0:5]
     arg6 = x[0:4]
     arg7 = x[0] + x[-1]
     argB1 = y[0:14]
     argB2 = y[0:13]
     argB3 = y[0:12]
     argB4 = y[0:7]
     argB5 = y[0:6]
     argB6 = y[0:5]
     argB7 = y[0:6]
     argB8 = y[0:5]
     argB9 = y[0:4]
     argB10 = y[0] + y[-1]

     if (arg1 == "--source="):
       sourcePath = x[9:]
     elif (arg2 == "-source="):
       sourcePath = x[8:]
     elif (arg3 == "source="):
       sourcePath = x[7:]
     elif (arg4 == "--src="):
       sourcePath = x[6:]
     elif (arg5 == "-src="):
       sourcePath = x[5:]
     elif (arg6 == "src="):
       sourcePath = x[4:]
     elif (arg7 == '"'):
       sourcePath = x
     else:
       sourcePath = x

     if (argB1 == "--destination="):
       destinationPath = y[14:]
     elif (argB2 == "-destination="):
       destinationPath = y[13:]
     elif (argB3 == "destination="):
       destinationPath = y[12:]
     elif (argB4 == "--dest="):
       destinationPath = y[7:]
     elif (argB5 == "-dest="):
       destinationPath = y[6:]
     elif (argB6 == "dest="):
       destinationPath = y[5:]
     elif (argB7 == "--dst="):
       destinationPath = y[6:]
     elif (argB8 == "-dst="):
       destinationPath = y[5:]
     elif (argB9 == "dst="):
       destinationPath = y[4:]
     elif (argB10 == '"'):
       destinationPath = y
     else:
       destinationPath = y
else:
  sourcePath = input("Enter your source path > ")
  #destinationPath = "O:\\NeroBackup\\AppData"
  destinationPath = input("Enter your destination path > ")



     


# Main Code

listTofile.list(sourcePath)
backupFromlist.backup(listTofile.tmp, sourcePath, destinationPath, parameters)
listTofile.cleanup()
print("Press ENTER to exit: ", end="", flush=True)
while True:
    keyboard.wait("ENTER")
    while msvcrt.kbhit():
        msvcrt.getch()    
    print("End")      # print the letter "p" next to the previous print statement above
    break


