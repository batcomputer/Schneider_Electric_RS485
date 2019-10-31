#import array as arr
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime



file = open("emdata.txt","r")

for line in file:
     if len(line) >= 15:
       words = line.split()
       sorted = np.array(words)
       stru = pd.DataFrame(sorted)
       stamps = pd.date_range(start='1/1/2019', freq ='S',periods=54)
       timestamps = pd.DataFrame(stamps)
       
      # print(stru[1:2])
      # powerf = re.sub(r"3055","powerfactor",file.read())
       
       current = re.sub(r"3059","voltage",file.read()) 
       final = re.findall("^.*voltage.*$",current,re.MULTILINE)
       series = pd.Series(final)
       matrix = pd.DataFrame(final)
       matrix.replace(regex=True,inplace=True,to_replace=r'^\D\D\D\D\D\D\D\D\D\D\D',value=r'')
       voltage = pd.DataFrame(matrix)
       finaltable = voltage.join(timestamps,lsuffix='voltage',rsuffix='time')
       #dataaa = np.array(matrix)  optional float array      
      

       #print(finaltable)
       plt.plot(timestamps,voltage)
       #plt.ylim([0,10])
       plt.show()

   #x = re.findall('.\s[0-9][0-9][0-9].*',line)
  # if len(x) != 0:
        #powerfactor = np.asarray(x[:1], dtype=np.float)
        #print(powerfactor)    
       # plt.show()
   
   #creation = pd.DataFrame({'register':words[0:1],'data':words[1:2]})   
  # print(words)
   
   #register = creation[0:1]
   #data = creation[1:2]

