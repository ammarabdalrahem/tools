#!/usr/bin/env python3
#@AbdalrahemAmmar


# Takes ref to list of numbers and returns median, 
# lower and upper cutoff (scalars) to call outliers:
# i)   median
# ii)  Q1 - 1.5 IQR 
# iii) Q3 + 1.5 IQR

import glob
import sys

#cutoff precentage
cut=95
path=sys.argv[1]
for filename in glob.glob(path, recursive=True):
    file_name=str(filename).split("/")[-1] # file name
    values=[]
    with open(filename) as file:
        #convert txt file into list
        for line in file :
            v= line.strip()
            values.append(v)
        #convert str values to float
        values =list(map(float, values))

        # sort the list
if type(values) is str:
    values = float(values)
values=sorted(values)
count=0
# 25% percentile (Q1)
Q1 = values[int(len(values)*0.25)]
# 50% median
Q2 = values[int(len(values)*0.50)]
# 75% percentile (Q3)
Q3 = values[int(len(values)*0.75)]

IQR = Q3-Q1 

minlimit=(Q1 - (1.5 * IQR))
maxlimit=(Q3 + (1.5 * IQR))

#minlimit outlier means poor alignment 
for v in values:
    if v < minlimit or v > maxlimit:
        count =count+1

print ("Q1:",Q1,"Q2:",Q2,"Q3:",Q3,"IQR:",IQR)
print("in",file_name,count/len(values)*100,"%","are outliers")
