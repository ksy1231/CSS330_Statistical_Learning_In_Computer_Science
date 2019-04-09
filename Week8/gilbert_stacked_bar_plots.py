#------------------------------------------------------------------------------
# Create stacked bar plots using the Gilbert data.
#
# By Johnny Lin
# February 2019
#
# Notes:
# * Written for Python 3.6.
# * Chunks of code are copied/adapted from:  https://matplotlib.org/gallery/
#   lines_bars_and_markers/bar_stacked.html (accessed February 19, 2019).
# * Data from and patterned after zyBook Participation Activity 4.1.4.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
import matplotlib.pyplot as plt


#- Data:  For death_count and no_death_count, the first element is Gilbert
#  and the second element is no Gilbert.

death_count = np.array([40,34])
no_death_count = np.array([217, 1350])

total_by_gilbert = death_count[0] + no_death_count[0]
total_by_not_gilbert = death_count[1] + no_death_count[1]

death_proportions = \
    death_count / np.array([total_by_gilbert, total_by_not_gilbert])
no_death_proportions = \
    no_death_count / np.array([total_by_gilbert, total_by_not_gilbert])
    

#- Parameters applicable to both plots:

width = 0.5
idx = np.arange(2)


#- Plot raw counts stacked bar plot:

fig = plt.figure(1)
p1 = plt.bar(idx, death_count, width)
p2 = plt.bar(idx, no_death_count, width, bottom=death_count)
plt.title("Gilbert Data Using Counts")
plt.ylabel("Number of Shifts")
plt.xticks(idx, ("Gilbert", "No Gilbert"))
plt.legend((p2[0], p1[0]), ("No death", "Death"))
plt.savefig('stacked_bar_counts_plot.png')


#- Plot proportions stacked bar plot:

fig = plt.figure(2)
p1 = plt.bar(idx, death_proportions, width)
p2 = plt.bar(idx, no_death_proportions, width, bottom=death_proportions)
plt.title("Gilbert Data Using Proportions")
plt.ylabel("Proportions")
plt.xticks(idx, ("Gilbert", "No Gilbert"))
plt.yticks([0, 0.25, 0.5, 0.75, 1.0])
plt.legend((p2[0], p1[0]), ("No death", "Death"))
plt.savefig('stacked_bar_prop_plot.png')


#===== end file =====