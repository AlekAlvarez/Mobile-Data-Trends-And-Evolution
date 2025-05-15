from sklearn.decomposition import LatentDirichletAllocation
import re
file=open("mobile_data.txt")
file=file.readlines()
data=[]
for i in range(1,len(file),5):
    line=file[i]
    line=re.sub(r'[^\w\s]', '', line)
    line = re.sub(r'\n', ' ', line) 
    line=line.lower()
    data.append(line)
    print(line)
print(len(data))
import gensim
from gensim import corpora
from gensim.models import LdaModel
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
Not_Topics=["mobile","earlier","vulnerability","allows","via","attacker"]
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text=text.split(" ")
    text = [word for word in text if word.isalpha() and word not in stop_words and word not in Not_Topics]
    return text
processed_docs = [preprocess_text(d) for d in data]
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
#number of topics is adjustable
#adjust it until topics gained make sense
lda = LdaModel(corpus, num_topics=6, id2word=dictionary, passes=15)
topics = lda.print_topics(num_words=3)
print(topics)
