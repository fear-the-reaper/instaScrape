import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')


def sanitize_text(text: str) -> str | None:
    try:
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Tokenize text
        tokens = word_tokenize(text.lower())

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]

        # Lemmatize words
        lemmatizer = WordNetLemmatizer()
        lem_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

        lemmatized_text = " ".join(lem_tokens)

        return lemmatized_text
    except Exception as e:
        print(f'Error in sanitize_text: {e}')
        return None


def analyze_sentiment(text: str) -> str | None:
    # try-except block to handle any exceptions that might occur
    try:
        # sanitize the input text using the sanitize_text function
        cleaned_text = sanitize_text(text)
        
        # check if the cleaned_text is not None
        if cleaned_text is not None:
            # create a SentimentIntensityAnalyzer object
            sia = SentimentIntensityAnalyzer()
            
            # calculate the sentiment score using the polarity_scores method
            sentiment_score = sia.polarity_scores(cleaned_text)

            # return the sentiment based on the compound score
            if sentiment_score['compound'] > 0:
                return "positive"
            elif sentiment_score['compound'] < 0:
                return "negative"
            else:
                return "neutral"
        
        # if cleaned_text is None, return None
        return None
    
    # catch any exceptions that might occur and print the error message
    except Exception as e:
        print(f'Error in analyze_sentiment: {e}')
        return None



text = "I want to get this shirt"
senti = analyze_sentiment(text)
print(f"The sentiment is {senti}")