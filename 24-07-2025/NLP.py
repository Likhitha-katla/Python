import nltk
from nltk.tokenize import sent_tokenize,word_tokenize,wordpunct_tokenize,TreebankWordTokenizer

nltk.download('punkt')

corpus = """Python is awesome. It is used in data science, AI, and web development.It's a both"""

sentences = sent_tokenize(corpus)
print(sentences)
words = word_tokenize(corpus)
print(words)
wordpunct = wordpunct_tokenize(corpus)
print(wordpunct)
token_tree = TreebankWordTokenizer()
token = token_tree.tokenize(corpus)
print(token)

#====================stemming=============================
from nltk.stem import PorterStemmer
list1 = ["eat","eaten","congratulations","histry","finally",'fairly','sportingly']
stemming = PorterStemmer()
for word in list1:
    print(word,"----->",stemming.stem(word))

#==============RegExp==================
from nltk import RegexpStemmer
regexp = RegexpStemmer('ing$|s$|e$|able$')
print(regexp.stem("eating"))
print(regexp.stem("plays"))

#==============snowballstemmer==================
from nltk import SnowballStemmer
snowball = SnowballStemmer('english')
for word in list1:
    print(word,"----->",snowball.stem(word))

#=============Lemmatizer===========
from nltk import WordNetLemmatizer
# nltk.download('wordnet')
lemma = WordNetLemmatizer()
for word in list1:
    print(word,"----->",lemma.lemmatize(word,pos="v"))

#==========STOPWORDS============
from nltk.corpus import stopwords
nltk.download('stopwords')
# print(stopwords.words('english'))

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
paragraph = """Python is a high-level, versatile programming language known for its readability and ease of use, making it suitable for both beginners and experienced developers. It's widely used in web development, software development, data science, machine learning, and more. Python's simple syntax and extensive library support contribute to its popularity and broad adoption across various industries."""
porterstem = PorterStemmer()
sente = sent_tokenize(paragraph)
# print(sente)
for i in range(len(sente)):
    # print(sente[i])
    words = word_tokenize(sente[i])
    # print(words)
    newwords = [porterstem.stem(j) for j in words if j not in set(stopwords.words("english")) ]
    # print(newwords)
    sente[i] = ' '.join(newwords)
    print(sente[i])

