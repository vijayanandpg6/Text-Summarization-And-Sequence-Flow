import bs4 as bs  
import urllib.request  
import re
import heapq 
import nltk

file = open("D:\TextManipulationRepo\ProcessFiles\InputTextDocument.txt","r")
contents= file.read()
file.close()

# scraped_data = urllib.request.urlopen('https://www.digit.in/features/apps/communication-patterns-for-the-internet-of-things-31292.html')  
# article = scraped_data.read()

# parsed_article = bs.BeautifulSoup(article,'lxml')

# paragraphs = parsed_article.find_all('p')

strContent = contents

# for p in paragraphs:  
#     strContent += p.text

# Removing Square Brackets and Extra Spaces
strContent = re.sub(r'\[[0-9]*\]', ' ', strContent)  
strContent = re.sub(r'\s+', ' ', strContent) 

# Removing special characters and digits
formatted_strContent = re.sub('[^a-zA-Z]', ' ', strContent )  
formatted_strContent = re.sub(r'\s+', ' ', formatted_strContent)  

sentence_list = nltk.sent_tokenize(strContent) 
print("\n\n")
print("Sentence list **************************************************")
print(sentence_list)
print("\n\n")

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_strContent):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

summary = ' '.join(summary_sentences)  
sum2=summary.replace(".",'.^')
print(sum2)  
file2 = open("D:\TextManipulationRepo\ProcessFiles\SummarizedTextDocument.txt","w+")
file2.write(sum2)
file2.close()