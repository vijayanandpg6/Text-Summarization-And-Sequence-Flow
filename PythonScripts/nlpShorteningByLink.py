import bs4 as bs  
import urllib.request  
import re
import heapq 
import nltk
import sys

# file = open("D:\Archive\TextSummarization\TensorFlow-Summarization-master\TensorFlow-Summarization-master\data\\test.outFile4.txt","r")
# contents= file.read()
# file.close()
linkText = sys.argv[1]
scraped_data = urllib.request.urlopen(linkText) 
 
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')


for p in paragraphs:  
    strContent += p.text

# Removing Square Brackets and Extra Spaces
strContent = re.sub(r'\[[0-9]*\]', ' ', strContent)  
strContent = re.sub(r'\s+', ' ', strContent) 

# Removing special characters and digits
formatted_strContent = re.sub('[^a-zA-Z]', ' ', strContent )  
formatted_strContent = re.sub(r'\s+', ' ', formatted_strContent)  


stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
sum2=summary.replace(".",'.^')
print(sum2)  
file2 = open("D:\TextManipulationRepo\ProcessFiles\SummarizedTextDocument.txt","w+")
file2.write(sum2)
file2.close()