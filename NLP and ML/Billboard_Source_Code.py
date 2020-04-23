import hashlib
from nltk.corpus import stopwords
import pandas as pd

stopwords = stopwords.words('english')
stopwords.append("verse")
stopwords.append("chorus")
stopwords.append("repeat")

data_set = pd.read_csv("input/billboard_dataset.csv")

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

def avg_rep_of_words_in_song(song):
    avg_rep_value = 0
    for key, val in sorted(song.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)[:5]:
        avg_rep_value=avg_rep_value+val
    
    avg_rep_value = round(avg_rep_value/5,2)
    return avg_rep_value

def most_rep_word_in_song(song):
    most_rep_value = 0
    for key, val in song.items():
        if val>most_rep_value:
            most_rep_value=val
    return most_rep_value

def total_words_in_song(song):
    return len(song)

def unique_words_in_song(song):
    return len(set(song))

def top_words_wt_by_total_length(value, length):
    value = round(value*100/length,4)
    return value

def top_words_wt_by_unique_length(value, length):
    value = round(value*10/length,4)
    return value

def length_wt(avg_length,gap_length,song_length):
    value = abs(song_length-avg_length)
    value = round(value/gap_length,2)
    value = round(1- value,2)
    if(value<0):
        value=0.01
    return value 

def most_rep_wt(most_avg,song_most):
    value = abs(most_avg-song_most)
    value = value/most_avg
    value = round(1- value,2)
    if (value < 0):
        value = 0.01
    return value

def avg_rep_wt(avg_avg,song_avg):
    value = abs(avg_avg-song_avg)
    value = value/avg_avg
    value = round(1- value,2)
    if (value < 0):
        value = 0.01
    return value

def unique_word_wt(unique_avg,unique_song):
    value = abs(unique_avg-unique_song)
    value = value/unique_avg
    value = round(1- value,2)
    if (value < 0):
        value = 0.01
    return value

def extract_dataset_features(song_dict):
    length_list = list()
    avg_leng = 0
    most_avg = 0
    avg_avg = 0
    unqiue_avg = 0
    for artist in song_dict:
        for song in song_dict[artist]:
            for each_song in song:
                length_list.append(song[each_song][0])
                avg_leng = avg_leng + song[each_song][0]
                most_avg = most_avg + song[each_song][1]
                avg_avg = avg_avg + song[each_song][2]
                unqiue_avg = unqiue_avg + song[each_song][3]
    
    length_list.sort()
    avg_leng     =   round(avg_leng/len(length_list))
    most_avg     =   round(most_avg/len(length_list),2)
    avg_avg      =   round(avg_avg/len(length_list),2)
    unqiue_avg   =   round(unqiue_avg/len(length_list),2)
    gap_length = get_gap_length(length_list)
    new_list = [avg_leng,most_avg,avg_avg,unqiue_avg,gap_length]
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
    for num in length_list[:1000]:
        low_sum = low_sum + num 
    for num in length_list[-1000:]:
        high_sum = high_sum + num
 
    low = round(low_sum/1000,2)
    high = round(high_sum/1000,2)
    gap_length = round(high - low)
    return gap_length

def get_song_at(song_dict,song_name):
    for artist in song_dict:
        for song in song_dict[artist]:
            try:
                new_list = song[song_name]
            except KeyError:
                continue
    return new_list

def main():
    group_data = data_set.groupby('artist')

    dataset_unique_wordslist = {}
    dataset_complete_wordslist = []
    dataset_total_num_of_songs = 0
    transformed_dataset = {}
    all_songs_in_set = set()

    for artist_name, songs in group_data:
        if artist_name not in transformed_dataset:
            transformed_dataset[artist_name] = []

        artists_all_songs_list = []
        words = {}
        song_length = 0

        most_rep_num=0
        for index, rows in songs.iterrows():
            if rows["song"] not in all_songs_in_set:
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
                all_songs_in_set.add(song_name)
                song_length = total_words_in_song(clean_text_list)
                avg_rep_num = avg_rep_of_words_in_song(song_words)
                most_rep_num = most_rep_word_in_song(song_words)
                unique_words_len = unique_words_in_song(song_words)
                artists_all_songs_list.append({song_name:[song_length,most_rep_num,avg_rep_num,unique_words_len,list(clean_text_list)]})

                update(dataset_unique_wordslist, song_words)
        transformed_dataset[artist_name] = artists_all_songs_list

    dataset_features = extract_dataset_features(transformed_dataset)

    # Length of Dataset = len (Datasets Wordslist)
    length_of_dataset = len(dataset_complete_wordslist)
    unique_words_length_of_dataset = len(dataset_unique_wordslist)
    avg_len_of_song_in_dataset = round(length_of_dataset/dataset_total_num_of_songs)

    dataset_overview = {"Total Songs in DataSet":dataset_total_num_of_songs,"Total Words":length_of_dataset, "Unique Words":unique_words_length_of_dataset, "Avg Length Per Song":avg_len_of_song_in_dataset}

    print(f"Overview of Complete DataSet Values  : { dataset_overview}")
    print(f"Transformed Dataset extracted Features [ Len Avg, Most Rep Avg, Avg Rep, Unique Avg, Normalize Length] :{dataset_features}")

    # Creating Top Words List (1000 words)
    top_words = dict()
    for key, val in sorted(dataset_unique_wordslist.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)[:1000]:
                top_words[key] = val
    #print(f"Top 1000 words list {top_words}")

    # Assigning Weight to Top Words
    hashed_weight_table_length = dict()
    hashed_weight_table_unique = dict()
    top_1000_words_list = list()
    for key,value in top_words.items():
        record = list()
        record.append(key)
        record.append(value)
        key = key.encode("utf-8")
        hash_key = hashlib.md5(key)
        hash_key = hash_key.hexdigest()
        hashed_weight_table_length[hash_key] = top_words_wt_by_total_length(value, length_of_dataset)
        hashed_weight_table_unique[hash_key] = top_words_wt_by_unique_length(value, unique_words_length_of_dataset)
        top_1000_words_list.append(record)

    frame = pd.DataFrame(top_1000_words_list)
    frame.to_csv("input/top_words.csv")
    #transformed_dataset_list = [["Length","Most","Average","Unique","IndexLength","IndexMost","IndexAverage","IndexUnique","IndexNormalizedLength","IndexNormalizedUnique","FinalIndex","WeightLength","WeightUnique"]]
    transformed_dataset_list = list()
    transformed_dataset_list_normalized =  list()

    final_data = list()
    for song in all_songs_in_set:
        absolute_list = list()
        normalized_list = list()

        features_in_song = get_song_at(transformed_dataset, song)
     #   print(f"Each Song Features - Len, Most Rep, Avg Rep, Unique Len, Lyrics List :{features_in_song}")

        weight0 = length_wt(dataset_features[0], dataset_features[4], features_in_song[0])
        weight1 = most_rep_wt(dataset_features[1], features_in_song[1])
        weight2 = avg_rep_wt(dataset_features[2], features_in_song[2])
        weight3 = unique_word_wt(dataset_features[3], features_in_song[3])

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

        normalised_wt_by_length =   round(songs_words_wt_length/ features_in_song[0],2)
        normalised_wt_by_unique =   round(songs_words_wt_unique/ features_in_song[3],2)

        weight4 = normalised_wt_by_length
        weight5 = normalised_wt_by_unique

        final_data.append(round((weight0*0.25+weight1*0.12+weight2*0.12+weight3*0.15+weight4*0.18+weight5*0.18),2))

        absolute_list.append(features_in_song[0])
        absolute_list.append(features_in_song[1])
        absolute_list.append(features_in_song[2])
        absolute_list.append(features_in_song[3])
        absolute_list.append(round(songs_words_wt_length, 2))
        absolute_list.append(round(songs_words_wt_unique, 2))
        absolute_list.append(1)

        normalized_list.append(weight0)
        normalized_list.append(weight1)
        normalized_list.append(weight2)
        normalized_list.append(weight3)
        normalized_list.append(weight4)
        normalized_list.append(weight5)
        normalized_list.append(1)

        transformed_dataset_list.append(absolute_list)
        transformed_dataset_list_normalized.append(normalized_list)


    df = pd.DataFrame(transformed_dataset_list)
    df.columns = ["Length", "Most", "Average", "Unique", "WeightLength", "WeightUnique", "Target"]
    df.to_csv('input/billboard_abs_features_dataset.csv')

    dfn = pd.DataFrame(transformed_dataset_list_normalized)
    dfn.columns = ["NLength","NMost","NAverage","NUnique","NWeightLength","NWeightUnique","Target"]
    dfn.to_csv('input/billboard_norm_features_dataset.csv')

if __name__ == '__main__':
   main()