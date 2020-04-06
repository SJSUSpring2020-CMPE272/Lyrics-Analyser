import hashlib
from wordcloud import WordCloud
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from pprint import pprint
from subprocess import check_output
import numpy as np
import pandas as pd 

print(check_output(["ls", "input"]).decode("utf8"))

stopwords = stopwords.words('english')
stopwords.append("verse")
stopwords.append("chorus")
stopwords.append("repeat")

data_set = pd.read_csv("input/songdata.csv")

def clean(song_lyric):
    symbols_to_remove = [ "\n" , "'" , "," , "]" , "[" , ")" , "(" , ":" , "." , "-" , "?" , "!" ]

    for each_symbol in symbols_to_remove:
        song_lyric = song_lyric.replace(each_symbol, "")

    final_song_lyric = []

    for word in song_lyric.split(' '):
        word = word.lower()
        if len(word) > 3 and word not in stopwords:
            final_song_lyric.append(word)

    return final_song_lyric


def update(dic1, dic2):
    for key, value in dic2.items():
        if key in dic1:
            dic1[key] = dic1[key] + dic2[key]
        else:
            dic1[key] = dic2[key]

def avg_rep_word(song):
    avg_rep_value = 0
    for key, val in sorted(song.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)[:5]:
        avg_rep_value=avg_rep_value+val
    
    avg_rep_value = round(avg_rep_value/5,2)
    return avg_rep_value

def most_rep_word(song):
    most_rep_value = 0
    for key, val in song.items():
        if val>most_rep_value:
            most_rep_value=val
    return most_rep_value

def unique_words(song):
    return len(song)

def top_index_wt(value,length):
    value = round(value/length,5)
    return value
  
def length_wt(avg_length,gap_length,song_length):
    value = abs(song_length-avg_length)
    value = round(value/gap_length,2)
    value = round(1- value,2)
    if(value<0):
        value=0
    return value 

def most_rep_wt(most_avg,song_most):
    value = abs(most_avg-song_most)
    value = value/most_avg
    value = round(1- value,2)
    if(value<0):
        value=0
    return value

def avg_rep_wt(avg_avg,song_avg):
    value = abs(avg_avg-song_avg)
    value = value/avg_avg
    value = round(1- value,2)
    if(value<0):
        value=0
    return value

def unique_word_wt(unique_avg,unique_song):
    value = abs(unique_avg-unique_song)
    value = value/unique_avg
    value = round(1- value,2)
    if(value<0):
        value=0
    return value
    
def song_length_list(song_dict):
    length_list = list()
    most_avg = 0
    avg_avg = 0
    unqiue_avg=0
    for artist in song_dict:
        for song in song_dict[artist]:
            for each_song in song:
                length_list.append(song[each_song][0])
                most_avg = most_avg + song[each_song][1]
                avg_avg = avg_avg + song[each_song][2]
                unqiue_avg = unqiue_avg + song[each_song][3]
    
    length_list.sort()
    most_avg=round(most_avg/len(length_list),2)
    avg_avg=round(avg_avg/len(length_list),2)
    unqiue_avg=round(unqiue_avg/len(length_list),2)
    gap_length = get_gap_length(length_list)
    new_list = [gap_length,most_avg,avg_avg,unqiue_avg]
    return new_list 

def xls_function(song_dict):
    list2 = [["Artist Name","Name of Song","Song's Length","Most Repeated","Avg of Top 5","No of Unique Word"]]
    for artist in song_dict:
        for song in song_dict[artist]:
            for each_song in song:
                print(each_song)
                list1 = list()
                list1.append(artist)
                list1.append(each_song)
                list1.append(song[each_song][0])
                list1.append(song[each_song][1])
                list1.append(song[each_song][2])
                list1.append(song[each_song][3])
                list2.append(list1)
    return list2

def get_gap_length(length_list):
    low_sum = 0
    high_sum = 0
    for num in length_list[:5000]:
        low_sum = low_sum + num 
    for num in length_list[-5000:]:
        high_sum = high_sum + num
 
    low = round(low_sum/5000)      
    high = round(high_sum/5000)
    gap_length = round(high -low)
    return gap_length

def get_song_at(song_dict,artist_name,song_name):
    for song in song_dict[artist_name]:
        try:
            new_list = song[song_name]
        except KeyError:
            continue
    return new_list

group_data = data_set.groupby('artist')

dataset_unique_wordslist = {}
dataset_complete_wordslist = []
dataset_total_num_of_songs = 0
dataset_each_song = {}

for artist_name, songs in group_data:
    if artist_name not in dataset_each_song:
        dataset_each_song[artist_name] = []
    
    artists_all_songs_list = []
    words = {}
    song_length = 0

    most_rep_num=0
    for index, rows in songs.iterrows():
        song_words= {}
        dataset_total_num_of_songs += 1
        clean_text_list = clean(rows["text"])
        dataset_complete_wordslist += clean_text_list
       
        for word in clean_text_list:
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1
        
        for word in clean_text_list:
            if word in song_words:
                song_words[word] = song_words[word] + 1
            else:
                song_words[word] = 1
        
        song_name = rows["song"]
        song_length = len(clean_text_list)
        avg_rep_num = avg_rep_word(song_words)
        most_rep_num = most_rep_word(song_words)
        unique_words_len = unique_words(song_words)
        artists_all_songs_list.append({song_name:[song_length,most_rep_num,avg_rep_num,unique_words_len,list(clean_text_list)]})

        update(dataset_unique_wordslist, song_words)
        
    dataset_each_song[artist_name] = artists_all_songs_list

dataset_features = {"Total Words":len(dataset_complete_wordslist),"Unique Words":len(dataset_unique_wordslist),"Avg Length per Song":round(len(dataset_complete_wordslist)/dataset_total_num_of_songs)} 
print(dataset_total_num_of_songs)
print(dataset_features)
param_list = song_length_list(dataset_each_song)
print(param_list)
top_words = dict()
for key, val in sorted(dataset_unique_wordslist.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)[:1000]:
            top_words[key] = val
hash_table = dict()
length_dataset = len(dataset_complete_wordslist)
for key,value in top_words.items():
    key = key.encode("utf-8")
    hash_key = hashlib.md5(key)
    hash_key = hash_key.hexdigest()
    hash_table[hash_key] = top_index_wt(value,length_dataset)

for i in range (1):
    song_list=["PillowTalk"]
    song_param_list = get_song_at(dataset_each_song,"Zayn Malik",song_list[i])
    print(song_param_list)
    word_index_value=0
    weight0 = length_wt(96,param_list[0],song_param_list[0])
    weight1 = most_rep_wt(param_list[1],song_param_list[1])
    weight2 = avg_rep_wt(param_list[2],song_param_list[2])
    weight3 = unique_word_wt(param_list[3],song_param_list[3])

    song_lyric = song_param_list[4]
    default = 0.01
    for word in song_lyric:
        word_index_value = word_index_value + default
        word = word.encode("utf-8")
        hash_key = hashlib.md5(word)
        hash_key = hash_key.hexdigest()
        try:
            if hash_table[hash_key]:
                word_index_value = word_index_value + hash_table[hash_key]
        except KeyError:
                continue
    print(word_index_value)
    word_index_value = (word_index_value*100)/song_param_list[0]
    weight4 = round(word_index_value,2)

    print(weight0,weight1,weight2,weight3,weight4)
    print(round((weight0*0.25+weight1*0.12+weight2*0.18+weight3*0.20+weight4*0.25),2))