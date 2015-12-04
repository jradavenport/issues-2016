
import numpy as np
from collections import Counter
import flesch
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # plot styling

filename = 'files.lis'
files = np.loadtxt(filename, dtype='str')

Fscore = np.zeros_like(files, dtype='float')
Nwords = np.zeros_like(files, dtype='float')
Names = files.copy()
Party = files.copy()


for k in range(len(files)):
    txt = open(files[k]).read()
    summary = flesch.summarize(txt)
    Fscore[k] = summary[4]
    Nwords[k] = summary[1]
    Names[k] = files[k][files[k].find('-')+1 : files[k].find('.txt')].upper()

    pn = files[k][files[k].find('/')+1 : files[k].find('-')]
    if pn is 'r':
        clr = 'maroon'
    else:
        clr = 'navy'
    Party[k] = clr



ss = np.argsort(Nwords)

indx = np.arange(len(Party))

plt.figure(figsize=(15,8))
plt.bar(indx, Nwords[ss], color=Party[ss])
plt.xticks(indx + 0.35, Names[ss])
plt.ylabel('# of Words', fontsize=18)
# plt.show()
plt.savefig('fig1.png')


ss = np.argsort(Fscore)

plt.figure(figsize=(15,8))
plt.bar(indx, Fscore[ss], color=Party[ss])
plt.xticks(indx + 0.35, Names[ss])
plt.ylabel('Flesch-Kincaid Grade Level', fontsize=18)
# plt.show()
plt.savefig('fig2.png')
