# Copyright (c) 2025 ksg-dev. Licensed under the MIT License. See LICENSE for details.

import pytest 
from collections import Counter
from textinsights.stats import word_frequency, sentiment_score


class TestWordFrequency:
    """Test suite for the word_frequency function."""

    def test_basic_frequency(self):
        """Test basic word frequency counting."""

        text = "apple banana apple orange banana apple"
        freq = word_frequency(text)
        assert isinstance(freq, Counter)
        assert freq["apple"] == 3
        assert freq["banana"] == 2
        assert freq["orange"] == 1


    def test_case_insensitivity(self):
        """Test that word frequency is case-insensitive."""

        text = "Apple apple APPLE aPpLe"
        freq = word_frequency(text)
        assert freq["apple"] == 4


    def test_empty_text(self):
        """Test that empty text returns empty Counter."""

        freq = word_frequency("")
        assert isinstance(freq, Counter)
        assert len(freq) == 0


class TestSentimentScore:
    """Test suite for the sentiment_score function."""

    def test_positive_sentiment(self):
        """Test text with positive sentiment."""

        text = "good excellent happy love"
        score = sentiment_score(text)
        assert score == 1.0


    def test_negative_sentiment(self):
        """Test text with negative sentiment."""

        text = "bad terrible awful sad hate"
        score = sentiment_score(text)
        assert score == -1.0

    
    def test_mixed_sentiment(self):
        """Test text with mixed sentiment."""

        text = "good bad good bad"
        score = sentiment_score(text)
        assert score == 0.0


    def test_neutral_sentiment(self):
        "Test text with no sentiment words."

        text = "this is a neutral sentence"
        score = sentiment_score(text)
        assert score == 0.0


    def test_custom_words_list(self):
        """Test with custom positive and negative word lists."""

        text = "excellent terrible awesome"

        # Default lists would include both positive and negative words
        default_score = sentiment_score(text)

        # Custom list that only recognizes 'awesome' as positive
        custom_pos = ["awesome"]
        # Doesn't include 'terrible'
        custom_neg = ["bad"]
        custom_score = sentiment_score(text, custom_pos, custom_neg)

        assert custom_score == 1.0 # Only 'awesome' is counted
        assert default_score != custom_score  # Should be different from default

