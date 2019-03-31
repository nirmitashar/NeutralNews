from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='9e56db8fef8946e59cc0545db2d90fa4')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='politics', language='en',
                                            category='general')

# /v2/everything
x = "gun control"
all_articles = newsapi.get_everything(q= x,
                                      language='en',
                                      sort_by='relevancy')
print("x" == "x")
# /v2/sources

#print(all_articles['articles'][0])
#print(all_articles['articles'][0]['author'])
print( len(all_articles['articles']))
print( len(all_articles))

length = 0



while (length < len(all_articles['articles'])):
     print(all_articles['articles'][length])
     print(length)
     length = length + 1
