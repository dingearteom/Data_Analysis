from preprocessing import df, Y
from header import *

print(df)

digit = [[0 for j in range(7)] for i in range(10)]

digit[0] = [1, 1, 1, 0, 1, 1, 1]
digit[1] = [0, 0, 1, 0, 0, 1, 0]
digit[2] = [1, 0, 1, 1, 1, 0, 1]
digit[3] = [1, 0, 1, 1, 0, 1, 1]
digit[4] = [0, 1, 1, 1, 0, 1, 0]
digit[5] = [1, 1, 0, 1, 0, 1, 1]
digit[6] = [1, 1, 0, 1, 1, 1, 1]
digit[7] = [1, 0, 1, 0, 0, 1, 0]
digit[8] = [1, 1, 1, 1, 1, 1, 1]
digit[9] = [1, 1, 1, 1, 0, 1, 1]

Y_predict = [-1 for i in range(df.shape[0])]

for i in range(df.shape[0]):
    dist = [0 for j in range(10)]
    for j in range(10):
        dist[j] = cityblock(df.iloc[i, :], digit[j])
    m = 100
    ans = -1
    for j in range(10):
        if (dist[j] < m):
            m = dist[j]
            ans = j
    Y_predict[i] = ans

print(accuracy_score(list(Y), Y_predict))


