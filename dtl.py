
# Example query:
# dtl(
#    examples = [
#         {'Furniture': 'No', 'Nr. of rooms': '3', 'New kitchen': 'Yes', 'Acceptable': 'Yes'},
#         {'Furniture': 'Yes', 'Nr. of rooms': '3', 'New kitchen': 'No', 'Acceptable': 'No'},
#         {'Furniture': 'No', 'Nr. of rooms': '4', 'New kitchen': 'No', 'Acceptable': 'Yes'},
#         {'Furniture': 'No', 'Nr. of rooms': '3', 'New kitchen': 'No', 'Acceptable': 'No'},
#         {'Furniture': 'Yes', 'Nr. of rooms': '4', 'New kitchen': 'No', 'Acceptable': 'Yes'}
#    ],
#    attributes = {'Furniture': ['Yes', 'No'], 'Nr. of rooms': ['3', '4'], 'New kitchen': ['Yes', 'No'], 'Acceptable': ['Yes', 'No']},
#    target = 'Acceptable',
#    default = 'Yes'
# )
#
# Warning: the target attribute must not be used in the decision tree
# Warning: attributes are not necessarily binary
#
#
# Expected result:
# ('Nr. of rooms', {
#     '4': 'Yes',
#     '3': ('New kitchen', {
#         'Yes': 'Yes',
#         'No': 'No'}
#     )
#     }
# )

import numpy as np
from math import log
from test import compileAttrs,compileExamples
from function import calculate_atrri_entorpy 
from function_bridge import *
#original_target=""
#original_default=""
def dtl(examples, attributes, target, default):
     print("..............................................................START.............................................................................")    
     original_target=target
     original_default=default
     print("The orginal list:")
     print(attributes)
     print("Target is :",target)
     print("The default value is :",default)
     print("The length of examples is")
     print(len(examples))
     set_y=[]
     set_n=[]
     counter_y=0
     counter_n=0
     for i in range(len(examples)):
         if (examples[i][target]==default):
            counter_y+=1
            set_y.append(examples[i])
         else:
            counter_n+=1
            set_n.append(examples[i])

     print(f"The vote for {target} :",counter_y)
     print(set_y)
     print(f"The vote for {target} :",counter_n)
     print(set_n)
     pset_y=counter_y/(counter_y+counter_n)
     pset_n=counter_n/(counter_y+counter_n)
     Entropy0=-(pset_y)*log(pset_y,2)-(pset_n)*log(pset_n,2)
     print("The original entropy is : ",Entropy0)
     print("..............................................................END...............................................................................")
     list_attributes=list(attributes.keys())
     list_attributes.remove(target)
     del attributes[target]
     print("After del the attri left are")
     print(attributes)
     print("After del the list left are ")
     print(list_attributes)
     consequence={}
     final_consequence={}
     temp_nameAttri_consequence=[]
     for list_sample in list_attributes:
         print("△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△△")
         calculate_atrri_entorpy(examples,attributes,list_sample,target,default,original_target,original_default)
         consequence[list_sample]=calculate_atrri_entorpy(examples,attributes,list_sample,target,default,original_target,original_default)
         print("▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽")
     print(consequence)
     max=Entropy0-consequence[list(consequence.keys())[0]]
     for zeiger in list(consequence.keys()):
         if Entropy0-consequence[zeiger]>=max:
            max=Entropy0-consequence[zeiger]
            temp_nameAttri_consequence=zeiger
     print("----------------------------------------------------------------------------------------------------------------------")       
     print(f"The max Entropy with attribute {temp_nameAttri_consequence}")
     print(max)
     final_consequence[temp_nameAttri_consequence]=max
     print(final_consequence)
     print("----------------------------------------------------------------------------------------------------------------------")
     print(len(examples))    
     print(examples)
     print("Old list is :")
     print(list_attributes)
     print(temp_nameAttri_consequence,":",attributes[temp_nameAttri_consequence])
     ############################################New serie###################################
     #     list_attributes.remove(temp_nameAttri_consequence)
     #     print("New list:")
     #     print(list_attributes)
     #print(attributes[temp_nameAttri_consequence][1])
     print("###############################################################")
     print(attributes[temp_nameAttri_consequence])
    # default_change=attributes[temp_nameAttri_consequence][0]
     default_change=attributes[temp_nameAttri_consequence][1]
     target_change=temp_nameAttri_consequence
     #del attributes[temp_nameAttri_consequence]
     print(temp_nameAttri_consequence)
     print("-------------",attributes,"-----------------") 
     print("************************************************************")
     print("The left attributes: ")
     print(attributes)
     print("Target chnage is : ",target_change)
     print("Default change is : ",default_change)
     print("************************************************************")
     #if len(attributes)!=1:
     #   dtl(examples, attributes,target_change ,default_change) 
     #else:
     #   print("The attri of attributes is empty")a
 

     function_bridge(examples, attributes, target_change, default_change,original_target,original_default)
