import scrapy


class IsnaSpider(scrapy.Spider):
    name = 'Isna'
    allowed_domains = ['www.isna.ir']
    start_urls = ['http://www.isna.ir/']

    def parse(self, response):
        pass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

stops = ['در', 'به', 'از', 'این', 'که', 'با','های','می','است', 'را'] 


vectorizer = TfidfVectorizer(stop_words=stops)
X = vectorizer.fit_transform(all_strings)

true_k = 4
model.fit(X)
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)


print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

