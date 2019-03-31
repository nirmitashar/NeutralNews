from flask import Flask, render_template, request
import os
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import urllib.request as urllib2
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import pickle
from flask import jsonify


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/topicapi", methods=["GET","POST"])
def topicapi():
    req = str(request.get_data())
    #change api key if it runs out
    newsapi = NewsApiClient(api_key='9e56db8fef8946e59cc0545db2d90fa4')
    # /v2/top-headlines

#    top_headlines = newsapi.get_top_headlines(q='politics', language='en',
            #                                    category='general')
    # /v2/everything
    all_articles = newsapi.get_everything(q='dog',
                                          language='en',
                                          sort_by='relevancy')

    clf = load("glow.joblib")
    count_vec = pickle.load( open( "countvec.pk", "rb" ) )
    tfidf = pickle.load( open( "tfidf.pk", "rb" ) )


    print("The request: " + req)

    if (req == "b'politics'"):
        print("we are in general")
        all_articles = newsapi.get_everything(q='politics',
                                              language='en',
                                              sort_by='relevancy')
    elif (req == "b'healthcare'"):
        print("we are in healthcare")

        all_articles = newsapi.get_everything(q='healthcare',
                                              language='en',
                                              sort_by='relevancy')
    elif (req == "b'gun control'"):
        print("we are in guncontrol")

        all_articles = newsapi.get_everything(q='gun control',
                                              language='en',
                                              sort_by='relevancy')
    elif (req=="b'immigration'"):
        print("we are in immigration")

        all_articles = newsapi.get_everything(q='immigration',
                                              language='en',
                                              sort_by='relevancy')

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
         x = clf.predict(tfidftrans)
         print(x)
         if (x == 0):
             if (len(conservative) < 3):
                conservative.append(length)
         elif (x == 1):
             if (len(liberal) < 3):
                liberal.append(length)
         #print(all_articles['articles'][length])
         #print(length)
         length = length + 1
         count = len(liberal) + len(conservative)


    url1 = all_articles['articles'][liberal[0]]['url']
    image1 = all_articles['articles'][liberal[0]]['urlToImage']
    title1 = all_articles['articles'][liberal[0]]['title']

    url2 = all_articles['articles'][liberal[1]]['url']
    image2 = all_articles['articles'][liberal[1]]['urlToImage']
    title2 = all_articles['articles'][liberal[1]]['title']

    url3 = all_articles['articles'][liberal[2]]['url']
    image3 = all_articles['articles'][liberal[2]]['urlToImage']
    title3 = all_articles['articles'][liberal[2]]['title']

    url4 = all_articles['articles'][conservative[0]]['url']
    image4 = all_articles['articles'][conservative[0]]['urlToImage']
    title4 = all_articles['articles'][conservative[0]]['title']

    url5 = all_articles['articles'][conservative[1]]['url']
    image5 = all_articles['articles'][conservative[1]]['urlToImage']
    title5 = all_articles['articles'][conservative[1]]['title']

    url6 = all_articles['articles'][conservative[2]]['url']
    image6 = all_articles['articles'][conservative[2]]['urlToImage']
    title6 = all_articles['articles'][conservative[2]]['title']

    #print(all_articles['articles'][0])
    #print(all_articles['articles'][0]['author'])
    #x =  len(all_articles['articles'])
    #print(x)
    #print( len(all_articles))
    r = [url1, image1, title1, url2, image2, title2,url3, image3, title3, url4, image4, title4, url5, image5, title5, url6, image6, title6]

    return jsonify(r)
    #while (length < len(all_articles['articles'])):
    #     print(all_articles['articles'][length])
    #     print(length)
    #     length = length + 1

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000)
