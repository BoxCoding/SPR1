import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
import re


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
url_symbol=re.compile('[^https?:\/\/.*[\r\n]*]')
STOPWORDS = set(stopwords.words('english'))


@staticmethod
def stem_words(text):
    text = text.split()
    stemmer = SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)
    return text


@staticmethod
def make_lower_case(text):
    return text.lower()


@staticmethod
def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text


@staticmethod
def normalize(s):
    """
    Given a text, cleans and normalizes it. Feel free to add your own stuff.
    """
    s = s.replace('&', ' and ')
    s = s.replace('@', ' at ')
    return s


@staticmethod
def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

@staticmethod
def replace_ftk(x):
    #print(x)
    if(re.findall(r'FTK',x)):
        result = re.sub(r'FTK','',x)
    else:
        result = x
    return (result)

@staticmethod
def replace_int(x):
    #print(x)
    if x !='nan':
        if(re.findall("[$&+,:;=?@#|'<>.^*()%!-]",x)):
            result = re.sub("[$&+,:;=?@#|'<>.^*()%!-]",'',x)
        else:
            result = x
    else:
        result =0
    return result

