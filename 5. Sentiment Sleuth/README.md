### Problem Statement: Sentiment Analysis of Tweets

#### Objective:
Your task is to build a sentiment analysis model that classifies tweets as **positive**, **negative**, or **neutral** based on the sentiment conveyed in the text. The model should be trained using the provided labeled dataset and should generalize well to predict the sentiment of new, unseen tweets.

#### Dataset Details:
The dataset contains the following columns:

1. **polarity** (Target variable): 
   - **0**: Negative sentiment
   - **2**: Neutral sentiment
   - **4**: Positive sentiment
2. **id**: A unique identifier for each tweet.
3. **date**: The timestamp when the tweet was posted.
4. **query**: The query or search term used to retrieve the tweet.
5. **user**: The user who posted the tweet.
6. **text**: The content of the tweet.

#### Evaluation:
The model will be evaluated based on accuracy, precision, recall, and F1 score. Your notebook should be clear and well-documented, with detailed explanations of the methodology used. Justify your choices of evaluation metrics and ensure that the code is easily understandable.