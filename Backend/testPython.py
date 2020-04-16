import sys
import csv
import os

INPUT_FILE = "../NLP/input/user_input_songs.csv"
OUTPUT_FILE = "../NLP/user_features.csv"

#add string to the input osv of NLP script
def add_input_string():
    fields=['user name',input_string[:10],'link',input_string]
    with open(r''+INPUT_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

#Running NLP script on user input string
def run_nlp():
    print("RUNNING NLP")
    os.system('python3 ../NLP/Project_Source_Code.py '+ INPUT_FILE + ' ' + OUTPUT_FILE)

if __name__ == "__main__":
    # Takes first name and last name via command
    # line arguments and then display them
    print("Output from Python")
    #print(sys.argv)
    #print("First name: " + sys.argv[1])
    #print("Last name: " + sys.argv[2])
    input_string = sys.argv[1]
    print(input_string)
    add_input_string()
    run_nlp()