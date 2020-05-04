(Group Members: Amit Sharma, Ambika Na, Deepa Vyasabhat, Jaspreet Singh)


# Project Name

Lyrics Analyser

# Abstract
The project is based on natural language processing over the existing lyrical dataset of over 5000+ popular songs and then using machine learning algorithms to generate a prediction model for guessing popularity of new songs based on keywords extracted from the lyrical dataset. The prediction model will be based upon the data extracted from already hit songs and will try to estimate the popularity of new songs based upon song’s length, repetition of words, usage of pop culture keywords. 

We have utilized an open source dataset from Kaggle website, consisting of 5000+ popular hit songs from various genres and timescale. The data consists of many variables like performing artist, genre, total word length, year of release. Through, natural language processing we are extracting key features to prepare our dataset which will be used by machine learning algorithms. Some of the key features in our cleaned dataset are "most often used words", "average length" etc. 
We have used knn algorithm, random forest, linear regression, logistic regression to generate a prediction model which will conclude whether a provided lyrics could be popular or not. 

We have developed a website for aspiring song writers. They can register to our system and can view their past searched lyrics. We are also providing visualisation to users based on the cleaned dataset which will help users in deciding which words to include while writing lyrics. It will also help them in gaining insights into behavior and structure of popular songs.  


This tool can be used in the music industry by artists associated with it ranging from lyricists, singers and music directors. 




# Architecture Diagram
<img src="Architecture/architecture.png" height="625">

Link of architecture diagram:
https://github.com/SJSUSpring2020-CMPE272/Lyrics-Analyser/blob/master/Architecture/architecture.png

# Technology Stack

Frontend: React, AntDesign CSS 

Backend: NodeJS, express, mongoDB, Python

Deployement: Dockers/containers running on Amazon EC2 instances Load balanced with network ELB. 

Dataset: open source dataset from Kaggle website, consisting of 5000+ popular hit songs 

