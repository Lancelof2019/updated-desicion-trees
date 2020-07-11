import numpy as np
from math import log
from function import *
from test import *

from function_entro import *
def function_inter_process(attributes,set_ytemp,set_ntemp,target,attri,default):
    counter_yy=0
    counter_yn=0
    set_yy=[]
    set_yn=[]
     ###########in Y
    for y in range(len(set_ytemp)):
        if(set_ytemp[y][target]==default):
           set_yy.append(set_ytemp[y])
           counter_yy+=1
        else:
            set_yn.append(set_ytemp[y])
            counter_yn+=1
    print("############################################################")
    print("--------------------------------------------------------------------------------------------------")
    print("|The atrribute of ",target," in the item of ",attri," with value of ",attri,":",attributes[attri][0],"|")
    #print("")
    print("--------------------------------------------------------------------------------------------------")
    print("yy counter",counter_yy)
    print(set_yy)
    print("yn counter",counter_yn)
    print(set_yn)
    #function_entro(set_yy,set_yn,counter_yy,counter_yn)
    #function_entropy(set_yy,target,default)
    print("------------------Y--------AND------------N---------------------------------")
    counter_ny=0
    counter_nn=0
    set_ny=[]
    set_nn=[]
    for z in range(len(set_ntemp)):
        if(set_ntemp[z][target]==default):
           set_ny.append(set_ntemp[z])
           counter_ny+=1
        else:
            set_nn.append(set_ntemp[z])
            counter_nn+=1
    #print("The atrribute of ",target," in the itme of ",attri)
    print("--------------------------------------------------------------------------------------------------")
    print("|The atrribute of ",target," in the item of ",attri," with value of ",attri,":",attributes[attri][1],"|")
    print("--------------------------------------------------------------------------------------------------")
    print("ny counter",counter_ny)
    print(set_ny)

    print("nn counter",counter_nn)
    print(set_nn)
    #function_entro(set_ny,set_nn,counter_ny,counter_nn)
   # function_entropy(set_nn,target,default)
    print("############################################################")
    return function_entro(set_yy,set_yn,counter_yy,counter_yn),function_entro(set_ny,set_nn,counter_ny,counter_nn)
