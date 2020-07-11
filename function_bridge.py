import numpy as np
#from test import compileAttrs,compileExamples
from function import calculate_atrri_entorpy
#from test import *
#from function_branch import *
from math import log
#from function import *
#from test import *
#from function_entro import *
#import dtl 
#import dtl
def function_bridge(examples, attributes, target, default,original_target,original_default):
    list_attributes=list(attributes.keys())
    list_attributes.remove(target)
    del attributes[target]
    sub_examples=[]
    for xx in range(len(examples)):
        if examples[xx][target]==default:
           sub_examples.append(examples[xx])
    print(sub_examples)


    print("..............................................................START.............................................................................")
    print("The orginal list:")
    print(attributes)
    print("Target is :",target)
    print("The default value is :",default)
    print("The length of sub_ examples is")
    print(len(sub_examples))
    print("*******************DTL space test**************************")
    #original_target=target
    # original_default=default


    print(original_target)
    print(original_default)
    #print("*******************DTL space test**************************")
    #set_y=[]
    #set_n=[]
    #counter_y=0
    #counter_n=0
    #for i in range(len(sub_examples)):
        #if (sub_examples[i][target]==default):
           #counter_y+=1
           #set_y.append(sub_examples[i])
        #else:
           #counter_n+=1
           #set_n.append(sub_examples[i])

    #print(f"The vote for {target} :",counter_y)
    #print(set_y)
    #print(f"The vote for {target} :",counter_n)
    #print(set_n)
    #pset_y=counter_y/(counter_y+counter_n)
    #pset_n=counter_n/(counter_y+counter_n)
    
    #Entropy0=-(pset_y)*log(pset_y,2)-(pset_n)*log(pset_n,2)
    #print("The original entropy is : ",Entropy0)

    #original_target=target
    #original_default=default
    #print("The orginal list:")
    #print(attributes)
    #print("Target is :",target)
    #print("The default value is :",default)
    #print("The length of sub_examples is")
    #print(len(sub_examples))
    set_y=[]
    set_n=[]
    counter_y=0
    counter_n=0
    for i in range(len(sub_examples)):
        if (sub_examples[i][original_target]==original_default):
           counter_y+=1
           set_y.append(sub_examples[i])
        else:
           counter_n+=1
           set_n.append(sub_examples[i])

    print(f"The vote for {original_target} :",counter_y)
    print(set_y)
    print(f"The vote for {original_target} :",counter_n)
    print(set_n)
    pset_y=counter_y/(counter_y+counter_n)
    #reverse_original_default=attributes[original_target][0]
    print(" The percent of original target with value YES is ",pset_y)
    pset_n=counter_n/(counter_y+counter_n)
    print(" The percent of original target with value NO is ",pset_n)
    Entropy_show=-(pset_y)*log(pset_y,2)-(pset_n)*log(pset_n,2)
    print("The original entropy is : ",Entropy_show)
    print("..............................................................END...............................................................................")
    #print(list_sample)
    

    print(list_attributes)
    

    for list_sample in list_attributes:
        print("△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△")
        calculate_atrri_entorpy(examples,attributes,list_sample,target,default,original_target,original_default)
    #consequence[list_sample]=calculate_atrri_entorpy(examples,attributes,"Furniture",target,default)
    #print(consequence)
        print("▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽")






