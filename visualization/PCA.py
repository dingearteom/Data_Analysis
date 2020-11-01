from preprocessing import df, Y
from header import *

pca = PCA(n_components=2)

df = pd.DataFrame(pca.fit_transform(df))
print(df)

#rendering

plt.figure(figsize=(15, 15))

df['cluster'] = list(Y)

plt.scatter(x=[df[0]], y=[df[1]], c=[df['cluster']])
plt.savefig('visualization/PCA.png')
