import sys
import csv
import os

INPUT_FILE = "../NLP_ML/input/user_input_songs.csv"
OUTPUT_FILE = "data.txt"

#add string to the input osv of NLP script
def add_input_string():
    fields=['user name',input_string[:10],'link',input_string]
    with open(r''+INPUT_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

#Running NLP script on user input string
def run_nlp():
    os.system('python3 ../NLP_ML/Python_File.py ' + input_string)

#if __name__ == "__main__":
# Takes first name and last name via command
# line arguments and then display them
input_string = sys.argv[1]
run_nlp()
with open(OUTPUT_FILE, 'r') as f:
    print(f.read())
