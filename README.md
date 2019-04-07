# NeutralNews
Hackathon project that classifies news articles as liberal or conservative in a news-feed format  

Model trained on labeled speeches from convote (Democrat or Republican): http://www.cs.cornell.edu/home/llee/data/convote.html  
  * Assumes Democrat is liberal; Republican is conservative 
  * Uses CountVectorizer and TfidfVectorizer to vectorize text 
  * Uses SVM for model
  * Uses pickle and joblib to save fitted model and vectorizer
 
Uses https://newsapi.org/ to receive news data (title, description) which is sent to the model to classify as liberal or conservative 

Uses Flask as web framework  
Uses Vue as JavaScript framework  
Uses https://getmdl.io/ for CSS  

Demo:   
http://sanguinesocialist.pythonanywhere.com/  
https://synthesized.herokuapp.com
