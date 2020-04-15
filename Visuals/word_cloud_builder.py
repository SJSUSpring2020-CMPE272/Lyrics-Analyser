# Open the file in read mode 
text = open("billboard_data.csv", "r") 
outtext = open("billboard_data_out.txt","w")
  
# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.replace(","," ").split(" ") 
    
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
for key in list(d.keys()): 
    if d[key]>5:
        outtext.write("{text: \""+key+"\", value: "+str(d[key])+"},\n")

outtext.close()
text.close()