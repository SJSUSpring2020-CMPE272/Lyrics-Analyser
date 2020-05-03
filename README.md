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

# Technology Stack
Frontend: React, AntDesign CSS 
Backend: NodeJS, express, mongoDB, Python
Deployement: Amazon EC2
Dataset: open source dataset from Kaggle website, consisting of 5000+ popular hit songs 


# ProjectGroup-11

(Group Members: Amit Sharma, Ambika Na, Deepa Vyasabhat, Jaspreet Singh)

# Project Architecture
<img src="Architecture/architecture.png" height="625">

# Project Idea-2

1. Project Title : Lyrics Analyser 
# Approved
 
2. Project idea description 
The project is based on natural language processing over the existing lyrical dataset of over 5000+ popular songs and then using machine learning algorithms to generate a prediction model for guessing popularity of new songs based on keywords extracted from the lyrical dataset. The prediction model will be based upon the data extracted from already hit songs and will try to estimate the popularity of new songs based upon song’s length, repetition of words, usage of pop culture keywords. 
 
  
3. The goal of the project ( Targeted User) 
This tool can be used in the music industry by artists associated with it ranging from lyricists, singers and music directors. 
 
 
4. Technology stack 
We will utilize an open source dataset from Kaggle website, consisting of 5000+ popular hit songs from various genres and timescale. The data consists of many variables like performing artist, genre, total word length, year of release. We will utilize Python as our primary language and associated sci-kit learning, matplotlib (numPy) module for massaging this dataset stored in MySQL database. 
 
We will run existing ML algorithms from the extracted dataset and try to figure out which algorithm provides the best results in a reasonable amount of time. 
 
Based upon the technical difficulties and time limits, we will try to develop front end for the program and host it on cloud services like AWS/GCP and attempt to display the comparisons of the different ML algorithms used along with some visualizations around the data itself. 
