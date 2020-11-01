# Digits Cluster Analysis

# Ultimate result

It can be easily demonstrated that in this task one cannot get score more than 75% accuracy (approximately).

The simpliest algorithm is just for each object to calculate its manhattan distance with all digits from 0 to 9. Then just predict the digit with minimum distance.

This is implementated in folder **ultimate_result**.
The accuracy score acquired is **74.6**.

It is obvious that this score cannot be substantially improved.


# Lab 1

## Hierarchial cluster Analysis

This program is in folder **hierarchial_clusterization**.

Algorithm:
* Firstly, clusters are acquired from one of hierarchial clusterization methods.
* Then for each cluster major presented label is predicted.

The best option proved to be distance between
* clusters: 'ward' 
* points: 'euclidean'

The result acquired is **50%**.

Additionally, in linkage_centroid_manhattan my own hierarchial cluster algorithm is implemented. Distance between
* clusters: centroid
* points: manhattan

Though, result was **32.8%**.

# Lab 2

## K-means

It is implemented in **k-means** folder.

Algorithm:
* Firstly, clusters are acquired from k-means algorithm.
* Then for each cluster major presented label is predicted.

The result comes between **68%** and **75%** which is ultimate threshold.

Further, I consider adding Bagging to diminish dispersion.

