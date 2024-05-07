from sklearn.datasets import fetch_20newsgroups
import numpy as np  # pip install numpy

cats = [
    'rec.motorcycles', 'rec.sport.baseball', 'comp.graphics',
    'comp.windows.x', 'talk.politics.mideast', 'sci.space',
    'sci.electronics', 'sci.med'
]

news_df = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'),
                             categories=cats, random_state=15)

print(type(news_df))
print(news_df.keys())
print(type(news_df.data), type(news_df.target_names), type(news_df.target))

for i, val in zip(np.unique(news_df.target), news_df.target_names):
    print("index ({}): topic {}".format(i, val))
