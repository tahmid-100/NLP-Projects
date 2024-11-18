from flask import Flask, render_template, request
import pandas as pd
import textdistance
import re
from collections import Counter

app = Flask(__name__)

# Load and preprocess words
words = []
with open('autocorrect book.txt', 'r', encoding='utf-8') as f:
    data = f.read().lower()
    words = re.findall(r'\w+', data)
    words += words  # Duplicate words to increase frequency

V = set(words)
words_freq_dict = Counter(words)
Total = sum(words_freq_dict.values())
probs = {k: words_freq_dict[k] / Total for k in words_freq_dict.keys()}

@app.route('/')
def index():
    return render_template('index.html', suggestions=None)

@app.route('/suggest', methods=['POST'])
def suggest():
    keyword = request.form.get('keyword', '').strip().lower()
    if not keyword:
        return render_template('index.html', suggestions=None)

    similarities = [1 - textdistance.Jaccard(qval=2).distance(v, keyword) for v in words_freq_dict.keys()]
    df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
    df.columns = ['Word', 'Prob']
    df['Similarity'] = similarities
    suggestions = df.sort_values(['Similarity', 'Prob'], ascending=False)[['Word', 'Similarity']]
    suggestions_list = suggestions.to_dict('records')  # Convert DataFrame to list of dictionaries
    return render_template('index.html', suggestions=suggestions_list)

if __name__ == '__main__':
    app.run(debug=True)
