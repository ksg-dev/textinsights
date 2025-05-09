# Copyright (c) 2025 ksg-dev. Licensed under the MIT License. See LICENSE for details.

import pytest 
from textinsights.analyzer import TextAnalyzer


class TestTextAnalyzer:
    """Test suite for the TextAnalyzer class."""

    def test_initialization(self):
        """Test that the analyzer initializes correctly."""

        sample_text = "This is a test sentence."
        analyzer = TextAnalyzer(sample_text)
        assert analyzer.text == sample_text
        assert analyzer.words == ["this", "is", "a", "test", "sentence"]

    def test_word_count(self):
        """Test the word_count method."""

        # Basic case
        analyzer = TextAnalyzer("Hello world, this is a test.")
        assert analyzer.word_count() == 6

        # Empty text
        analyzer_empty = TextAnalyzer("")
        assert analyzer_empty.word_count() == 0

        # Multiple spaces
        analyzer_spaces = TextAnalyzer("Word   with   extra   spaces")
        assert analyzer_spaces.word_count() == 4


    def test_unique_words(self):
        """Test the unique_words method."""

        # Text w repeated words
        analyzer = TextAnalyzer("test test test unique words words")
        unique = analyzer.unique_words()
        assert len(unique) == 3
        assert "test" in unique
        assert "unique" in unique
        assert "words" in unique

        # Case insensitivity
        analyzer_case = TextAnalyzer("Test TEST test")
        assert len(analyzer_case.unique_words*()) == 1


    def test_avg_word_length(self):
        """Test avg_word_length method."""

        # Basic case
        analyzer = TextAnalyzer("four nine")
        # I expect to have to change this assertion to 4, but leaving for now for testing
        assert analyzer.avg_word_length() == 4.5

        # Empty text
        analyzer_empty = TextAnalyzer("")
        assert analyzer_empty.avg_word_length() == 0

        # Text with punctuation
        analyzer_punct = TextAnalyzer("hello, world! This is a test.")
        # We'll need to modify implementation to handle punctuation properly
        # For now, just test that it returns a reasonable value
        avg_len = analyzer_punct.avg_word_length()
        assert 3.0 <= avg_len <= 6.0

