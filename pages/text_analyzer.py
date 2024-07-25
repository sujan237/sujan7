import streamlit as st
import re

def calculate_statistics(text):
    words = text.split()
    word_count = len(words)
    unique_words = len(set(words))
    character_count = sum(len(word) for word in words)
    avg_word_length = character_count / word_count if word_count > 0 else 0
    
    return word_count, unique_words, character_count, avg_word_length

def analyze_text(text):
    # Calculate basic statistics
    word_count, unique_words, character_count, avg_word_length = calculate_statistics(text)
    
    # Count frequency of each word
    word_freq = {}
    for word in text.split():
        word = re.sub(r'[^\w\s]', '', word)  # Remove punctuation
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort words by frequency
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return word_count, unique_words, character_count, avg_word_length, sorted_word_freq

def main():
    st.title("Text Analyzer")
    
    # Text input area
    text = st.text_area("Enter your text here:")
    
    if st.button("Analyze"):
        if text:
            word_count, unique_words, character_count, avg_word_length, sorted_word_freq = analyze_text(text)
            
            st.header("Basic Statistics:")
            st.write(f"Word count: {word_count}")
            st.write(f"Unique words: {unique_words}")
            st.write(f"Character count: {character_count}")
            st.write(f"Avg. word length: {avg_word_length:.2f}")
            
            st.header("Word Frequency:")
            for word, freq in sorted_word_freq[:10]:  # Display top 10 most frequent words
                st.write(f"{word}: {freq}")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
