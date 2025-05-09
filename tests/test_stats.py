# Copyright (c) 2025 ksg-dev. Licensed under the MIT License.
# See LICENSE for details.

import pytest
from collections import Counter
from textinsights.stats import word_frequency, sentiment_score


class TestWordFrequency:
    """Test suite for the word_frequency function."""

    @pytest.fixture
    def sample_text(self):
        """Fixture providing sample text for word frequency testing."""
        return "apple banana apple orange banana apple"

    @pytest.fixture
    def complex_text(self):
        """Fixture providing more complex text with puntuation and cases."""
        return """The quick brown fox jumps over the lazy dog.
        The quick brown fox is quick indeed! Fox fox FOX."""

    @pytest.fixture(params=[
        "apple",
        "apple apple",
        "apple banana apple",
        ""
    ])
    def various_texts(self, request):
        """Parametrized fixture providing different text examples."""
        return request.param

    def test_basic_frequency(self, sample_text):
        """Test basic word frequency counting using fixture."""

        freq = word_frequency(sample_text)
        assert isinstance(freq, Counter)
        assert freq["apple"] == 3
        assert freq["banana"] == 2
        assert freq["orange"] == 1

    @pytest.mark.parametrize("text,expected_counts", [
        ])

    
    
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
        # Only 'awesome' is counted
        assert custom_score == 1.0
        # Should be different from default
        assert default_score != custom_score
