# 🔎 Autocorrecting using NLP

Welcome to **Autocorrecting using NLP**, a smart system that suggests the most likely correct words for any input using natural language processing techniques and a custom-built vocabulary.

---

## 💡 Overview

This project implements an **intelligent autocorrect system** inspired by classic NLP approaches. By leveraging a vocabulary built from a book, it can suggest the most probable and similar words whenever the user inputs a potentially incorrect word.

---

## 📚 Dataset & Vocabulary

- **Source**: Vocabulary extracted from a book.
- **Approach**:
  - Parsed all unique words from the text.
  - Created a **Python dictionary** (`word_freq_dict`) mapping each word to its frequency count.
  - Calculated word probabilities to represent how common each word is in the corpus.

---

## ⚙️ Methodology

### 📄 Probability Calculation

The probability of each word was computed as:

```python
prob[word] = word_freq_dict[word] / Total_word_freq
