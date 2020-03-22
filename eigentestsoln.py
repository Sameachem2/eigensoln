import os
import nltk
from collections import Counter

    
"""Look for interesting_words 
as the output for this challenge, it is a dictionary with
a list for each key word as an item describing the number of occurences, the document the word is in and the sentences it forms
a part of.

"""
def main():
    nltk.download('punkt')
    nltk.download('stopwords')
    #Loop through documents 1 to 7. And find most interesting words with nltk.
    
    #interesting words Dictionaries of format: {word: [[word_count]}, {word: {[document_numbers]}}, {word:[sentences]}
    interesting_words = {}

    
    boring_common_words = [',','the','of','and','to','that','a','.','in','is','-','\'','I','for','\'\'','','this','it','she','our','we','all','have','was','as','our','you','be','let','can','with','it\'','not','from','will','my' ,'or','are','who','And', 'with','We','on','On','us','at','by','saw',"'s",'Let','let','\'ve','It']+nltk.corpus.stopwords.words("english")
    
    for i in range(1,7):
        
        with open(os.path.dirname(__file__)+"\EigenTaskExampleDocs\Test Docs\doc"+ str(i) +".txt",encoding="utf8") as f:
        
            data = str(f.read())
            #print("data is: ", data)
            #print(nltk.tokenize.word_tokenize(data))
            sentence_text = nltk.tokenize.sent_tokenize(data)
            #print("This is sentence text: ", sentence_text) #a list of sentences.
            #print("This is the first sentence: ", sentence_text[0])
            word_list = Counter(nltk.tokenize.word_tokenize(data))
            #print("word list is: ",word_list)
            #print(word_list.most_common(30))
            #interesting_words[word_list.most_common()][0] = []
            #interesting_words[word_list.most_common()][1] = []
            #interesting_words[word_list.most_common()][2] = []
            
            word_list2 = word_list.most_common()
            #print("Word list 2 is: ", word_list2)
            #for i in range(len(word_list2)):
            
            word_list3 = []
            for x in word_list2:
                if x[0] not in boring_common_words:
                    word_list3.append(x)
               
            
            for x in word_list3:
                x_sentences = []
                for p in sentence_text:
                    sentence_words = p.lower().split()
                    if (x[0].lower() in sentence_words) or (x[0].lower()+"." in sentence_words) or (x[0].lower()+"," in sentence_words) or (x[0].lower()+"?" in sentence_words) or (x[0].lower()+"!" in sentence_words) or (x[0].lower()+".\"" in sentence_words) or (x[0].lower()+"?\"" in sentence_words) or (x[0].lower()+"!\"" in sentence_words) or ("\'"+x[0].lower()+"\'" in sentence_words) or (x[0].lower()+",\'\'" in sentence_words):
                        x_sentences.append(p)
                
                
                
                #interesting words Dictionary of format: {word: [[word_count],[document_numbers],[sentences]]}
                
                
                #Record the number of occurences of a word, initialize dictionary if not already created.
                try:
                    interesting_words[x[0]][0] += x[1]
                except:
                    interesting_words[x[0]] = [[],[],[]]
                    interesting_words[x[0]][0] = x[1]
                    
                interesting_words[x[0]][1].append(i)

                
                #All the sentences the word is in.
                try:
                    interesting_words[x[0]][2].append(x_sentences)
                except:
                    interesting_words[x[0]][2].append(x_sentences)

            print("Interesting words: ", interesting_words)
            
    

if __name__ == "__main__":
	main()