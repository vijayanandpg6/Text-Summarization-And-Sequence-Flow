import nltk
import pandas as pd
import string
import re
import numpy as np
import json.decoder
import sys
# from matplotlib import  as plt


# Downloading Stopwords,wordnet from internet to use it later
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')



#using panda read function
file = open("D:\TextManipulationRepo\ProcessFiles\SummarizedTextDocument.txt","r")
contents= file.read()
print(contents)
from io import StringIO
TESTDATA = StringIO(contents.replace("^","-"))

data = pd.read_csv(TESTDATA,sep=";",lineterminator='-',names=['body_text','label'])
# print(file.read())
#data = pd.read_csv('M10033.tsv', sep=',',lineterminator='-', names=['body_text'])
print(data.head())

#removing punctuation to process text
def remove_punct(text):
    text_nopunct = "".join([x for x in text if x not in string.punctuation])
    return text_nopunct

data['body_text_clean'] = data['body_text'].apply(lambda x: remove_punct(x))

#print(data.head()) 

#tokenization

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens
#print("\n")
#print("\n")
data['body_text_tokenized'] = data['body_text_clean'].apply(lambda x:tokenize(x.lower()))
#print(data.head())

# # Remove stopwords
stopword = nltk.corpus.stopwords.words('english')
#print(stopword)

#Function to remove stopwords
def remove_stopwords(tokenized_list):
    text =[word for word in tokenized_list if word not in stopword]
    return text
#print("\n")
#print("\n")
data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda x: remove_stopwords(x))
#print(data.head())


#  Lemmatizer
wn = nltk.WordNetLemmatizer()

def lemmatizing(tokenized_text):
    text =[wn.lemmatize(word) for word in tokenized_text]
    return text
data['body_text_lemmatized'] = data['body_text_nostop'].apply(lambda x: lemmatizing(x))
#print("\n")
#print("\n")
#print(data.head())


result=[]
lst=[]
from nltk import word_tokenize
for index,row in data.iterrows():
    result.append(row['body_text_clean'])
    wordToken=word_tokenize(row['body_text_clean'])
    lst.append(nltk.pos_tag(wordToken))

resultstr='{ "values" :['
i=0
datalength=len(data.index)
for index,row in data.iterrows():
    resultstr=resultstr+"{ 'text' :"+'"'+result[i]+'"'+" , "
    tempstr=str(lst[i]).replace(",",":").replace("): (",",").replace("[(","").replace(")]","")
    resultstr=resultstr+tempstr+"}";
    if i!=(datalength-1):
        resultstr=resultstr+",";
    i=i+1

resultstr=resultstr+"]}"   
temp1= str(resultstr).replace("'", '"')
print(temp1)

file2 = open(r"D:\\TextManipulationRepo\\ProcessFiles\\JSONSummarizedTextDocument.txt","w+") 
file2.write(temp1)
file2.close()


