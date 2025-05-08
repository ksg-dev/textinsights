"""Statistical utilities for text analysis."""

from collections import Counter

def word_frequency(text):
    """Calculate frequency distribution of words.
    
    Args:
        text (str): Input text

    Returns:
        Counter: Word frequency counts
    
    """
    words = text.lower().split()
    return Counter(words)


def sentiment_score(text, positive_words=None, negative_words=None):
    """Simple sentiment analysis based on word lists.
    
    Args:
        text (str): Input text
        positive_words (list): List of positive words
        negative_words (list): List of negative words

    Returns:
        float: Sentiment score between -1 and 1
    
    """
    if positive_words is None:
        positive_words = ['good', 'great', 'excellent', 'happy', 'like', 'love']

    if negative_words is None:
        negative_words = ['bad', 'terrible', 'awful', 'sad', 'hate', 'dislike']

    words = text.lower().split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    total = positive_count + negative_count
    if total == 0:
        return 0
    
    return (positive_count - negative_count) / total