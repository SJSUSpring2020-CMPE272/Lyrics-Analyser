import hashlib
import pandas as pd
import RandomForest
import KNN
import LogisticRegression
import sys
import json


import sys
import csv
import os

INPUT_FILE = "input/user_input_songs.csv"
OUTPUT_FILE = "data.txt"

BILLBOARD_DATASET = { 'Len Avg' : 143 , 'Most Rep Avg' : 15.78 , 'Avg Rep' : 9.21 , 'Unique Avg' : 68.5 , 'Normalize Length' : 183 }
OTHER_DATASET = { 'Len Avg' : 96 , 'Most Rep Avg' : 9.65 , 'Avg Rep' : 5.84 , 'Unique Avg' : 54.85 , 'Normalize Length' : 112 }
top_1000_words = pd.read_csv("../NLP_ML/input/top_words.csv")
top_words = dict()
for index, rows in top_1000_words.iterrows():
    top_words[rows[1]] = rows[2]

def clean(song_lyric):
    song_lyric = song_lyric.replace("\n"," ")
    symbols_to_remove = [ "'", ",", "]", "[", ")", "(", ":", ".", "-", "?", "!"]

    for each_symbol in symbols_to_remove:
        song_lyric = song_lyric.replace(each_symbol, "")

    final_song_lyric = []

    for word in song_lyric.split(' '):
        word = word.lower()
        if len(word) > 2:
            final_song_lyric.append(word)

    return final_song_lyric

def update(dic1, dic2):
    for key, value in dic2.items():
        if key in dic1:
            dic1[key] = dic1[key] + dic2[key]
        else:
            dic1[key] = dic2[key]


def avg_rep_of_words_in_song(song):
    avg_rep_value = 0
    for key, val in sorted(song.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)[:5]:
        avg_rep_value = avg_rep_value + val

    avg_rep_value = round(avg_rep_value / 5, 2)
    return avg_rep_value


def most_rep_word_in_song(song):
    most_rep_value = 0
    for key, val in song.items():
        if val > most_rep_value:
            most_rep_value = val
    return most_rep_value


def total_words_in_song(song):
    return len(song)


def unique_words_in_song(song):
    return len(set(song))


def length_wt(avg_length, gap_length, song_length):
    if(song_length>10):
        value = abs(song_length - avg_length)
    else:
        value = gap_length
    value = round(value / gap_length, 2)
    value = round(1 - value, 2)
    if (value <= 0):
        value = 0.01
    return value


def most_rep_wt(most_avg, song_most):
    value = abs(most_avg - song_most)
    value = value / most_avg
    value = round(1 - value, 2)
    if (value <= 0):
        value = 0.01
    return value


def avg_rep_wt(avg_avg, song_avg):
    value = abs(avg_avg - song_avg)
    value = value / avg_avg
    value = round(1 - value, 2)
    if (value <= 0):
        value = 0.01
    return value


def unique_word_wt(unique_avg, unique_song):
    value = abs(unique_avg - unique_song)
    value = value / unique_avg
    value = round(1 - value, 2)
    if (value <= 0):
        value = 0.01
    return value

def top_words_wt_by_total_length(value, length):
    value = round(value*100/length,4)
    return value

def top_words_wt_by_unique_length(value, length):
    value = round(value*10/length,4)
    return value

def wordcloud_list(song_words):
    wordcloud_user_list = list()
    for key in song_words:
        user_words = dict()
        user_words['text'] = key;
        user_words['value'] = song_words[key];
        wordcloud_user_list.append(user_words)
    return wordcloud_user_list

def parse_user_input(user_string):
    INPUT_STRING = user_string
    #INPUT_STRING = "and I miss you, Like the desert miss the rain!"
    INPUT_SONG_FEATURES_LIST = list()
    clean_text_list = clean(INPUT_STRING)
    song_words= {}
    for word in clean_text_list:
        if word in song_words:
            song_words[word] = song_words[word] + 1
        else:
            song_words[word] = 1

    song_length = total_words_in_song(clean_text_list)
    avg_rep_num = avg_rep_of_words_in_song(song_words)
    most_rep_num = most_rep_word_in_song(song_words)
    unique_words_len = unique_words_in_song(song_words)
    INPUT_SONG_FEATURES_LIST.append(song_length)
    INPUT_SONG_FEATURES_LIST.append(most_rep_num)
    INPUT_SONG_FEATURES_LIST.append(avg_rep_num)
    INPUT_SONG_FEATURES_LIST.append(unique_words_len)
    INPUT_SONG_FEATURES_LIST.append(list(clean_text_list))

    wordcloud_user_list = wordcloud_list(song_words)
    wordcloud_dataset_list = wordcloud_list(top_words)

    length_of_dataset = 617254
    unique_words_length_of_dataset = 38905

    hashed_weight_table_length = dict()
    hashed_weight_table_unique = dict()
    for key, value in top_words.items():
        key = key.encode("utf-8")
        hash_key = hashlib.md5(key)
        hash_key = hash_key.hexdigest()
        hashed_weight_table_length[hash_key] = top_words_wt_by_total_length(value, length_of_dataset)
        hashed_weight_table_unique[hash_key] = top_words_wt_by_unique_length(value, unique_words_length_of_dataset)

    features_in_song = INPUT_SONG_FEATURES_LIST
    absolute_list = list()
    normalized_list = list()

    weight0 = length_wt(BILLBOARD_DATASET['Len Avg'], BILLBOARD_DATASET['Normalize Length'], features_in_song[0])
    weight1 = most_rep_wt(BILLBOARD_DATASET['Most Rep Avg'], features_in_song[1])
    weight2 = avg_rep_wt(BILLBOARD_DATASET['Avg Rep'], features_in_song[2])
    weight3 = unique_word_wt(BILLBOARD_DATASET['Unique Avg'], features_in_song[3])

    songs_words_wt_length = 0
    songs_words_wt_unique = 0
    song_lyric = features_in_song[4]

    for word in song_lyric:
        word = word.encode("utf-8")
        hash_key = hashlib.md5(word)
        hash_key = hash_key.hexdigest()
        try:
            if hashed_weight_table_length[hash_key]:
                songs_words_wt_length = songs_words_wt_length + hashed_weight_table_length[hash_key]
                songs_words_wt_unique = songs_words_wt_unique + hashed_weight_table_unique[hash_key]
        except KeyError:
            continue

    #    print(f"Calculated Total Weight By Total Length : {round(songs_words_wt_length,2)}")
    #    print(f"Calculated Total Weight By Unique Words Length : {round(songs_words_wt_unique,2)}")
    if(songs_words_wt_length>0):
        normalised_wt_by_length = round(songs_words_wt_length / features_in_song[0], 2)
        normalised_wt_by_unique = round(songs_words_wt_unique / features_in_song[3], 2)
    else:
        normalised_wt_by_length = 0
        normalised_wt_by_unique = 0
    #    print(f"Normalized Weight By Total Length : {normalised_wt_by_length}")
    #    print(f"Normalized Weight By Unique Words Length : {normalised_wt_by_unique}")

    weight4 = normalised_wt_by_length
    weight5 = normalised_wt_by_unique

        #    print(weight0,weight1,weight2,weight3,weight4,weight5)
        #    print(round((weight0*0.20+weight1*0.10+weight2*0.15+weight3*0.15+weight4*0.20+weight5*0.20),2))

#    print(round((weight0 * 0.25 + weight1 * 0.12 + weight2 * 0.12 + weight3 * 0.15 + weight4 * 0.18 + weight5 * 0.18), 2))

    normalized_list.append(weight0)
    normalized_list.append(weight1)
    normalized_list.append(weight2)
    normalized_list.append(weight3)
    normalized_list.append(weight4)
    normalized_list.append(weight5)

    absolute_list.append(features_in_song[0])
    absolute_list.append(features_in_song[1])
    absolute_list.append(features_in_song[2])
    absolute_list.append(features_in_song[3])
    absolute_list.append(round(songs_words_wt_length, 2))
    absolute_list.append(round(songs_words_wt_unique, 2))

    abs_bb = pd.read_csv("../NLP_ML/input/billboard_abs_features_dataset.csv")
    abs_os = pd.read_csv("../NLP_ML/input/otherds_abs_features_dataset.csv")
    abs_merged = abs_bb.append(abs_os)
    abs_merged = abs_merged.drop(['Unnamed: 0'],axis=1)

    Absolute_RFC , Absolute_RFR , Absolute_RF_Accuracy = RandomForest.run_random_forest(abs_merged,absolute_list)
    Absolute_KNN_Accuracy , Absolute_KNN_Prediction = KNN.run_knn(abs_merged,absolute_list)
    Absolute_LRC_Accuracy , Absolute_LRC = LogisticRegression.run_logreg(abs_merged,absolute_list)

    norm_bb = pd.read_csv("../NLP_ML/input/billboard_norm_features_dataset.csv")
    norm_os = pd.read_csv("../NLP_ML/input/otherds_norm_features_dataset.csv")
    norm_merged = norm_bb.append(norm_os)
    norm_merged = norm_merged.drop(['Unnamed: 0'],axis=1)

    Normalized_RFC , Normalized_RFR , Normalized_RF_Accuracy= RandomForest.run_random_forest(norm_merged,normalized_list)
    Normalized_KNN_Accuracy , Normalized_KNN_Prediction =  KNN.run_knn(norm_merged,normalized_list)
    Normalized_LRC_Accuracy , Normalized_LRC = LogisticRegression.run_logreg(norm_merged,normalized_list)

    output = dict()

    output["Billboard Dataset"] = BILLBOARD_DATASET
    output["Other Dataset"] = OTHER_DATASET

    absoulte_graph = dict()
    absoulte_graph['Length'] = absolute_list[0]
    absoulte_graph['Most'] = absolute_list[1]
    absoulte_graph['Average'] = absolute_list[2]
    absoulte_graph['Unique'] = absolute_list[3]
    absoulte_graph['WeightLength'] = absolute_list[4]
    absoulte_graph['WeightUnique'] = absolute_list[5]
    output['User Graph Features '] = absoulte_graph

    output['Absolute Features'] = absolute_list
    output['Normalized Features'] = normalized_list

    output['Absolute RFC CLASSIFICATION'] = Absolute_RFC
    output['Absolute RF Accuracy'] = Absolute_RF_Accuracy
    output['Absolute RFR REGRESSION'] = Absolute_RFR
    output['Normalized RFC CLASSIFICATION'] = Normalized_RFC
    output['Normalized RF Accuracy'] = Normalized_RF_Accuracy
    output['Normalized RFR REGRESSION'] = Normalized_RFR

    output['Absolute KNN CLASSIFICATION'] = Absolute_KNN_Prediction
    output['KNN Accuracy'] = Absolute_KNN_Accuracy
    output['Normalized KNN CLASSIFICATION'] = Normalized_KNN_Prediction

    output['Absolute LRC'] = Absolute_LRC
    output['LRC Accuracy'] = Absolute_LRC_Accuracy
    output['Normalized LRC'] = Normalized_LRC

    output['User Wordcloud'] = wordcloud_user_list
    #output['Dataset Wordcloud'] = wordcloud_dataset_list

    if absolute_list[0]<15 or normalized_list[4]<0.08 or normalized_list[5]<0.09:
        output['Absolute RFC CLASSIFICATION'] = str([0])
        output['Normalized RFC CLASSIFICATION'] = str([0])
        output['Absolute KNN CLASSIFICATION'] = str([0])
        output['Normalized KNN CLASSIFICATION'] = str([0])       
        output['Absolute RFR REGRESSION'] = str([0])
        output['Normalized RFR REGRESSION'] = str([0])

    value1 = float(str(output['Absolute RFC CLASSIFICATION']).replace("[","").replace("]",""))+float(str(output['Absolute RFR REGRESSION']).replace("[","").replace("]",""))
    value2 = float(str(output['Normalized RFC CLASSIFICATION']).replace("[","").replace("]",""))+float(str(output['Normalized RFR REGRESSION']).replace("[","").replace("]",""))
    value3 = float(str(output['Absolute LRC'].replace("[","")).replace("]",""))+ float(str(output['Normalized LRC']).replace("[","").replace("]",""))
    value4 = float(str(output['Absolute KNN CLASSIFICATION']).replace("[","").replace("]",""))+float(str(output['Normalized KNN CLASSIFICATION']).replace("[","").replace("]",""))

    verdict = value1+value2+value3+value4
    index = 0
    if verdict > 3.25:
        for val in normalized_list:
            index = index + float(val)
        index = (index + verdict)*9.25
        index = round(index,2)
        if(index>100):
            index = 100
        output['verdict'] = ["POPULAR", index]
    else:
        output['verdict'] = ["NEEDS IMPROVEMENT",index]
    #output['Dataset Wordcloud'] = wordcloud_dataset_list


    #for key in output:
    #    print(str(key)+"   "+str(output[key]))

    # Write output in file
    with open('data.txt', 'w') as outfile:
        json.dump(output, outfile)

    with open('data.txt', 'r') as f:
	    print(f.read())

    return output


#add string to the input osv of NLP script
def add_input_string():
    fields=['user name',input_string[:10],'link',input_string]
    with open(r''+INPUT_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


if __name__ == '__main__':
    user_string = sys.argv[1]
    parse_user_input(user_string)