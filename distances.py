from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    "Sur le climat, il n’y a pas de plan B car il n’y a pas de planète B",
    "Climat: Mars n'est pas un plan B pour l'humanité",
    "Il n'y a pas de plan B, parce qu'il n'y a pas de planète B."]

vectorizer = CountVectorizer(analyzer ="char", ngram_range=(3,5))
X = vectorizer.fit_transform(corpus)

array = X.toarray()

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(array))
