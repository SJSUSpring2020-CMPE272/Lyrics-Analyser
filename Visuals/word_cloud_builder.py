import csv as csv

# Open the file in read mode 
outtext = open("billboard_data_out.txt","w")

readdata = csv.reader(open("../NLP_ML/input/top_words.csv", "r")) 
data = []
for row in readdata:
    data.append(row)
data.pop(0)

# Create an empty dictionary 
d = dict() 

for i in range(1,len(data)):
    outtext.write("{text: \""+data[i][1]+"\", value: "+data[i][2]+"},\n")

outtext.close()
