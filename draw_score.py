import matplotlib.pyplot as plt
import numpy
import time

fig, (ax1, ax2) = plt.subplots(2)

f = open("score_history.txt")
scores = f.readlines()
score_list = []
for score in scores:
    score_list.append(int(score))

f = open("mean_score_history.txt")
scores = f.readlines()
mean_score_list = []
for score in scores:
    mean_score_list.append(int(score))

f = open("win_rate_history.txt")
scores = f.readlines()
win_rate_list = []
for score in scores:
    win_rate_list.append(float(score))

ax1.plot(score_list)

ax1.plot(list(range(1000, len(mean_score_list)*1000 +1, 1000)), mean_score_list)
ax1.set_xlabel("epoch")
ax1.set_ylabel("score")

ax2.plot(list(range(1000, len(mean_score_list)*1000 +1, 1000)), win_rate_list)
ax2.set_xlabel("epoch")
ax2.set_ylabel("1000-win rate (%)")

plt.show()
