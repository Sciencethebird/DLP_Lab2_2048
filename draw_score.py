import matplotlib.pyplot as plt
import numpy

f = open("score_history.txt")

scores = f.readlines()

score_list = []
for score in scores:
    score_list.append(int(score))

plt.plot(score_list)
plt.xlabel("epoch")
plt.ylabel("score")
plt.show()