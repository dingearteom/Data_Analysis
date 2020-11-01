from header import *
from preprocessing import df, Y
from class_map import class_map

models = [KMeans(n_clusters=k).fit(df) for k in range(1, 21)]
dist = [models[i].inertia_ for i in range(20)]


plt.plot(range(1, 21), dist, marker='o')
plt.xlabel('X')
plt.ylabel('Sum_of_distances')
plt.savefig('K-means/elbow.png')

clf = KMeans(n_clusters=10)
clf.fit(df)

df['ans'] = class_map(Y, list(clf.predict(df)))

print(accuracy_score(list(Y), df['ans']))
