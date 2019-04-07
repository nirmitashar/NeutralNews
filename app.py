from flask import Flask, render_template, request
import os
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import urllib.request as urllib2
from bs4 import BeautifulSoup
import pickle
from flask import jsonify
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/topicapi", methods=["GET","POST"])
def topicapi():
    req = str(request.get_data())
    print(req[2:-1])
    #change api key if it runs out
    newsapi = NewsApiClient(api_key='9e56db8fef8946e59cc0545db2d90fa4')
    
    all_articles = newsapi.get_everything(q=req[2:-1],
                                          language='en',
                                          sort_by='relevancy')

    clf = load("glow.joblib")
    count_vec = pickle.load( open( "countvec.pk", "rb" ) )
    tfidf = pickle.load( open( "tfidf.pk", "rb" ) )


    print("The request: " + req)


    length = 0
    count = 0
    liberal = []
    conservative = []

    #while (length < len(all_articles['articles'])):
    while (count < 6 and length < len(all_articles['articles'])):
         description =  all_articles['articles'][length]['title'] + '. ' + all_articles['articles'][length]['description']
         #print(description)
         description = [description]
         counttrans = count_vec.transform(description)
         #print(counttrans)
         tfidftrans  = tfidf.transform(counttrans)
         y = clf.predict(tfidftrans)
         print(type(y))
         if (y == [0]):

             print("y is " + str(y))
             if (len(conservative) < 3):
                conservative.append(length)

         elif (y == [1]):
             print("y is " + str(y))
             if (len(liberal) < 3):
                liberal.append(length)
         #print(all_articles['articles'][length])
         #print(length)
         length = length + 1
         count = len(liberal) + len(conservative)

    urls = []
    images = []
    titles = []
    r = []
    for i in range(0,3):
      r.append(all_articles['articles'][liberal[i]]['url'])
      r.append(all_articles['articles'][liberal[i]]['urlToImage'])
      r.append(all_articles['articles'][liberal[i]]['title'])
    
    for i in range(0,3):
      r.append(all_articles['articles'][conservative[i]]['url'])
      r.append(all_articles['articles'][conservative[i]]['urlToImage'])
      r.append(all_articles['articles'][conservative[i]]['title'])

 
    
    return jsonify(r)
    #while (length < len(all_articles['articles'])):
    #     print(all_articles['articles'][length])
    #     print(length)
    #     length = length + 1

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000)
