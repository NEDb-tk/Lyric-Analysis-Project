import collections
import pandas as pd
import matplotlib.pyplot as plt

with open ('C:/Scripts/Python/Jesus/file.txt', 'r', encoding='utf-8') as infile:
	a = infile.read()
	#string = re.sub("\(.*?\)","", data)
	#string = re.sub("\[.*?\]", "", string)

# Stopwords
stopwords = set(line.strip() for line in open('C:/Scripts/Python/Jesus/stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)# Close the file
infile.close()# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')
plt.title('2017-2020')
plt.show()