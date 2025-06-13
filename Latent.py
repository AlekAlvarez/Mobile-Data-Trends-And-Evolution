from sklearn.decomposition import LatentDirichletAllocation
import re
years=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
latent_data=open("latent_data.txt",'w')
for i in years:
    file=open("mobile_data_"+str(i%100)+".txt")
    file=file.readlines()
    data=[]
    for j in range(len(file)):
        if len(file[j])>15:
            line=file[j]
            line=re.sub(r'[^\w\s]', '', line)
            line = re.sub(r'\n', ' ', line) 
            line=line.lower()
            data.append(line)
    import gensim
    from gensim import corpora
    from gensim.models import LdaModel
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    Not_Topics=["mobile","earlier","vulnerability","allows","via","attacker","severity",'cpe','uri',"complexity"]
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
    lda = LdaModel(corpus, num_topics=20, id2word=dictionary, passes=15)
    topics = lda.print_topics(num_words=5)
    from collections import Counter

    topic_counts = Counter()

    for doc_bow in corpus:
        topic_distribution = lda.get_document_topics(doc_bow)
        # Find the topic with the highest probability in the doc
        dominant_topic = max(topic_distribution, key=lambda x: x[1])[0]
        topic_counts[dominant_topic] += 1
    total_docs = len(corpus)

    # Get topic keywords for reference
    topic_keywords = lda.print_topics(num_words=3)
    latent_data.write('\n'+str(i)+',')
    # Print sorted topic frequencies
    for topic_num, count in topic_counts.most_common():
        percentage = (count / total_docs) * 100
        latent_data.write(f"Topic {topic_num} ({percentage:.2f}% of docs): {topic_keywords[topic_num][1]},")
latent_data.close()
