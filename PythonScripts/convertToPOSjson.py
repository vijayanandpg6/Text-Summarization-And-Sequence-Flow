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


resultstr=resultstr+"]}"   
temp1= str(resultstr).replace("'", '"')
print(temp1)

file2 = open(r"D:\\TextManipulationRepo\\ProcessFiles\\JSONSummarizedTextDocument.txt","w+") 
file2.write(temp1)
file2.close()


