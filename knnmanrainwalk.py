from math import sqrt
import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbors(data, predict, k=3):
    if k < len(data):
        warnings.warn('k is less than the total amount of voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1]/k
    return vote_result, confidence

print('using speed, time, dist, traffic rating, and bus density, the weather can be predicted')
cumacc = 0
ttimes = 25
for i in range(0,ttimes):
    df = pd.read_csv('GPS Trajectory/go_track_tracks.csv')
    df.replace('\"', '', inplace=True)
    df.drop(['id'], 1, inplace=True)
    df.drop(['id_android'], 1, inplace=True)
    df.drop(['car_or_bus'], 1, inplace=True)
    df.drop(['linha'], 1, inplace=True)
    #only using speed, time, dist, traffic rating, and bus density to predict the weather
    full_data = df.astype(float).values.tolist()
    random.shuffle(full_data)

    test_size = 0.2
    train_set = {1:[], 2:[]}#2-sunny, 1-raining 0-unknown
    test_set = {1:[], 2:[]}
    train_data = full_data[:-int(test_size*len(full_data))]
    test_data = full_data[-int(test_size*len(full_data)):]
    for i in train_data:
        if i[-1]!=0:
            train_set[i[-1]].append(i[:-1]) 
    for i in test_data:
        if i[-1]!=0:
            test_set[i[-1]].append(i[:-1])

    #print("ts:",len(test_set[2]),len(test_set[1]),"tr:",len(train_set[2]),len(train_set[1]))

    correct = 0
    total = 0
    for group in test_set:
        for data in test_set[group]:
            vote, conf = k_nearest_neighbors(train_set, data, k=5)
            total+=1
            if group == vote:
                correct+=1
    cumacc += correct/total
tacc = cumacc/ttimes 
print("with an total accuracy of:", tacc)
