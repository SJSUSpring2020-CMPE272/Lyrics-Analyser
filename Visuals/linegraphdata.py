import numpy as np
import csv as csv
#Open the file in read mode 

#Data generation for scatterplot
text = open("featured_dataset.csv", "r") 
outtext1 = open("linegraph1.txt","w")
outtext2 = open("linegraph2.txt","w")
outtext4 = open("linegraph4.txt","w")

#outtext5= open("bargraph.txt","w")
  
# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Split the line into words 
    words = line.split(",") 
    
    output = "{x: "+words[1]+" ,y: "+words[6]+", color: 10},"
    outtext1.write(output+"\n")    

    output = "{x: "+words[2]+" ,y: "+words[6]+", color: 10},"
    outtext2.write(output+"\n") 

    output = "{x: "+words[4]+" ,y: "+words[6]+", color: 10},"
    outtext4.write(output+"\n") 

outtext1.close()
outtext2.close()
outtext4.close()
text.close()

#Data generation for bar graph
readdata = csv.reader(open('featured_dataset.csv', 'r')) 
data = []
for row in readdata:
    data.append(row)
data.pop(0)
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []

# ========================================
for i in range(1,len(data)):
    q1.append(float(data[i][1]))
    q2.append(float(data[i][2]))
    q3.append(float(data[i][3]))
    q4.append(float(data[i][4]))
    q5.append(float(data[i][5]))
    q6.append(float(data[i][6]))
        
print ('Mean - Length:            ', (np.mean(q1)))
print ('==============================================')
print ('Mean - Most:            ', (np.mean(q2)))
print ('==============================================')
print ('Mean - Average:            ', (np.mean(q3)))
print ('==============================================')
print ('Mean - Unique:            ', (np.mean(q4)))
print ('==============================================')
print ('Mean - WeightLength:            ', (np.mean(q5)))
print ('==============================================')
print ('Mean - WeightUnique:            ', (np.mean(q6)))
print ('==============================================')
