import os
import time
i=0


#write main code here 
while(i<=13):
    

    os.system(f"echo Hello_{i} world> Hello_{i}.txt")
    os.system(f"git add .")
    os.system(f'git commit -m "Added file {i}"')
    os.system(f"git push origin main")
    
    i=i+1

    #halka rest
    time.sleep(2)