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


resultstr=resultstr+"]}"   
temp1= str(resultstr).replace("'", '"')
print(temp1)

file2 = open(r"D:\\TextManipulationRepo\\ProcessFiles\\JSONSummarizedTextDocument.txt","w+") 
file2.write(temp1)
file2.close()


