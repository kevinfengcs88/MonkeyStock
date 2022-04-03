import numpy as np
import pandas as pd
import nltk
import sklearn

cols = ['polarity','id','date','flag','user','text']
set_encoding = "ISO-8859-1"

df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding=set_encoding, names=cols)
#df.sample(10)

np.sum(df.isnull().any(axis=1))

data=df[['text','polarity']]
data.sample(10)

data['polarity'] = data['polarity'].replace(4,1)

data_pos = data[data['polarity'] == 1].iloc[:int(20000)]
data_neg = data[data['polarity'] == 0].iloc[:int(20000)]
dataset = pd.concat([data_pos, data_neg])
dataset['text']=dataset['text'].str.lower()
dataset['text'].tail()
#dataset.sample(20)



from nltk.corpus import stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))
#print(stopwords.words('english'))

def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

dataset['text'] = dataset['text'].apply(lambda text: cleaning_stopwords(text))
dataset['text'].tail()

import string
english_punctuations = string.punctuation
print(english_punctuations)

#Removing punctuation
def cleaning_punctuations(text):
    translator = str.maketrans('', '', english_punctuations)
    return text.translate(translator)
dataset['text']= dataset['text'].apply(lambda x: cleaning_punctuations(x))
dataset['text'].tail()

#Removing URLs
import re
dataset['text'] = dataset['text'].astype(str)
def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)

dataset['text'] = dataset['text'].apply(lambda x: cleaning_URLs(x))
dataset['text'].head()

#Removing numbers
def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)
dataset['text'] = dataset['text'].apply(lambda x: cleaning_numbers(x))
dataset['text'].head()

#Tokenizing
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

tokenizer = RegexpTokenizer(r'\w+')
dataset['text'] = dataset['text'].apply(tokenizer.tokenize)
dataset['text'].head()


#Stemming
st = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data
dataset['text']= dataset['text'].apply(lambda x: stemming_on_text(x))
dataset['text'].head()

#Lemmatizer
lm = nltk.WordNetLemmatizer()
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data
dataset['text'] = dataset['text'].apply(lambda x: lemmatizer_on_text(x))
dataset['text'].head()

#Separating input feature and label
X=data.text
y=data.polarity

from sklearn.model_selection import train_test_split

#Splitting data into Train and Test subset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.05, random_state = 935)

#Fit tf-dif vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
vectoriser.fit(X_train)

#Transform tf-dif vectorizer
X_train = vectoriser.transform(X_train)
X_test  = vectoriser.transform(X_test)


from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

def model_Evaluate(model):
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    print(classification_report(y_test, y_pred))
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)


def bernoulliModel():
    BNBmodel = BernoulliNB()
    BNBmodel.fit(X_train, y_train)
    #model_Evaluate(BNBmodel)
    y_pred1 = BNBmodel.predict(X_test)
    return BNBmodel


def SVCmodel():
    SVCmodel = LinearSVC()
    SVCmodel.fit(X_train, y_train)
    #model_Evaluate(SVCmodel)
    y_pred2 = SVCmodel.predict(X_test)
    return SVCmodel


def LRmodel():
    LRmodel = LogisticRegression(C = 2, max_iter = 1000, n_jobs=-1)
    LRmodel.fit(X_train, y_train)
    #model_Evaluate(LRmodel)
    y_pred3 = LRmodel.predict(X_test)
    return LRmodel

