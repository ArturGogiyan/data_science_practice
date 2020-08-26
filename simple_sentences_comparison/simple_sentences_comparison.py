import re
import numpy as np
from scipy.spatial import distance

file1 = open('sentences.txt', 'r')
lines = file1.readlines()
file1.close()
lines = [line.lower() for line in lines]
unique_words = {}
for line in lines:
    words = re.split('[^a-z]', line)
    for word in words:
        if (word not in unique_words) and (len(word) > 0):
            unique_words[word] = len(unique_words)
length = len(unique_words)
matrix = np.zeros((len(lines), len(unique_words)))
i = 0
for line in lines:
    words = re.split('[^a-z]', line)
    for word in words:
        if len(word) > 0:
            word_id = unique_words[word]
            matrix[i, word_id] += 1
    i += 1
cosine_distances = np.zeros((len(lines), 2))
for i in range(1, len(lines)):
    cosine_distances[i] = [i, distance.cosine(matrix[0], matrix[i])]
cosine_distances = sorted(cosine_distances, key=lambda x: x[1])
file1 = open('result.txt', 'w')
file1.write(str(int(round(cosine_distances[1][0]))) + " " + str(int(round(cosine_distances[2][0]))))


