import  numpy as np
from test import * 
from function_branch import *
from math import log
#def  get_further_atrri(n):  
     
     #for j in range(len(attributes)):def 
         #print(attributes)
     #print(attributes.keys())
     #list_attributes=list(attributes.keys())[:-1]
     #print(list_attributes)
     
     
def calculate_atrri_entorpy(examples,attributes,attri,target,default,original_target,original_default):
    set_ytemp=[]
    set_ntemp=[]
    counter_ytemp=0
    counter_ntemp=0
    for x in range(len(examples)):
        print("Attri : ",attri," Value: ",examples[x][attri])
        if(examples[x][attri]==attributes[attri][1]):
          set_ytemp.append(examples[x])
          counter_ytemp+=1
        else:
          set_ntemp.append(examples[x])
          counter_ntemp+=1
    print("---------------------------------------")
    print("************Y :*********************")
    print("The attribute ",attri,":",attributes[attri][1]," is :")
    print(set_ytemp)
    print("-----The number of ",attri,":",attributes[attri][1]," is ",counter_ytemp)
    print("************N :*********************")
    print("The attribute ",attri,":",attributes[attri][0]," is :")
    print(set_ntemp)
    print("-----The number of ",attri,":",attributes[attri][0]," is ",counter_ntemp)
    print("---------------------------------------")
    possi_y=counter_ytemp/(counter_ytemp+counter_ntemp)
    possi_n=counter_ntemp/(counter_ytemp+counter_ntemp)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(possi_y)
    print(possi_n)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    data_result=function_inter_process(attributes,set_ntemp,set_ytemp,target,attri,default)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("data_result 0 is ",data_result[0])
    print("data_result 1 is ",data_result[1])
    print(possi_y*data_result[1]+possi_n*data_result[0])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return possi_y*data_result[1]+possi_n*data_result[0]
    ########in attri =Y to find target acceptable Y or N#######
    #counter_yy=0
    #counter_yn=0
    #set_yy=[]
    #set_yn=[]
     ###########in Y
    #for y in range(len(set_ytemp)):
        #if(set_ytemp[y][target]==default):
           #set_yy.append(set_ytemp[y])
           #counter_yy+=1
        #else:
            #set_yn.append(set_ytemp[y])
            #counter_yn+=1
   # print("############################################################")
   # print("The atrribute of ",target," in the item of ",attri)
   # print("yn counter",counter_yy)
   # print(set_yy)
   # print("yn counter",counter_yn)
   # print(set_yn)

    
