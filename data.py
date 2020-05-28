import os
import time
##Specifically written for linux only
os.system("rm summary.json")
os.system("wget https://api.covid19api.com/summary")
time.sleep(5)
os.system("mv summary summary.json")
os.system("git push -u origin master")
os.system("git add .")
os.system("git commit -m \"update\" ")
os.system("git push")

