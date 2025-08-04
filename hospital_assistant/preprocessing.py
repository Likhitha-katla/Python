import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered = [w for w in tokens if w not in stopwords.words('english')]
    stemmed = [PorterStemmer().stem(word) for word in filtered]
    return " ".join(stemmed)
