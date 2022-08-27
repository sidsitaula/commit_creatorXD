from ast import main
import os
import time


i=0


while(i<8):

    os.system(f"echo Hello_{i} world> Hello_{i}.txt")
    os.system(f"git add .")
    os.system(f'git commit -m "Added file {i}"')
    os.system(f"git push -u origin creator")
    os.system(f"git pull origin main")
    os.system(f"git checkout main")
    os.system(f"git merge creator")
    os.system(f"git push -u origin main")
    os.system(f"git branch -d creator")
    os.system(f"git push origin -d creator")
    os.system(f"git checkout -b creator")

    i=i+1

    #rest
    time.sleep(2)