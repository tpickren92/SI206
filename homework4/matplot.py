import numpy as np
import matplotlib.pyplot as plt
## men = fb; women = twitter

N = 5
menMeans = (200, 325, 130, 35, 427) # share/retweet count
# menStd = (2, 3, 4, 1, 2) #dont need

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='b')

womenMeans = (125, 232, 314, 120, 25)
# womenStd = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, womenMeans, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Shares/Retweets') #nice to have username added here
ax.set_title('Share/Retweet comparison')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Tweet 1', 'Tweet 2', 'Tweet 3', 'Tweet 4', 'Tweet 5')) #how to include time of creation?

ax.legend((rects1[0], rects2[0]), ('Facebook', 'Twitter')) #key text

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()