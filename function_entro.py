import numpy as np
from math import log
def function_entro(dataSet_y,dataSet_n,counter_y,counter_n):
    if(counter_y==0 and counter_n!=0):
      print("This node is leaf target is NO",counter_n)
      Entro_dataSet=0
    elif(counter_y!=0 and counter_n==0):
        print("This node is leaf target is YES",counter_y)
        Entro_dataSet=0
    else:
        py=counter_y/(counter_y+counter_n)
        #print("py is :",py)
        pn=counter_n/(counter_y+counter_n)
        #print("pn is :",pn)

        Entro_dataSet=-py*log(py,2)-pn*log(pn,2)
      
    print(Entro_dataSet)  
    return Entro_dataSet 
    
    
