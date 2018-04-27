import json
import numpy as np

import matplotlib as matplotlib
import matplotlib.pyplot as plt
import plotsettings as plotsettings

#from pprint import pprint

publishable = plotsettings.Set('Cell')
publishable.set_figsize(1.5, 1.0, aspect_ratio = 0.95)
matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
matplotlib.rc('text', usetex=False)

ax = plt.subplot(111)
with open('journal-publications.json') as data_file:
    data = json.load(data_file)
    x   = data[0]
    pub = np.array(x['articles'])
    pubyear = pub[:, 0]
    pubcount= pub[:, 1] * 0
    
    for ind in range(0, len(data)):
        x = data[ind]
        pub = np.array(x['articles'])
        journal=x['name']
        pubcount += pub[:, 1]
        ax.plot(pub[:, 0], pub[:, 1], lw=2, label=journal)
    #ax.set_ylim([0, 200])

plt.grid(True)
plt.xlabel('year')
plt.ylabel('number of publications')
plt.legend(loc='upper left', shadow=False, fontsize='x-small')
plt.savefig('total_publication.png', bbox_inches='tight', dpi=300)
plt.close()

publishable.set_figsize(1.0, 1.0, aspect_ratio = 0.95)

keywords = ["forthefirsttime", "novel", "excellent", "robust", "unique", "unprecedented", "promising", "remarkable", "encouraging", "enormous"]

for keyword in keywords:
    print keyword
    #with open('journal-publications.json') as data_file:
    #    data_total = json.load(data_file)
    
    with open(keyword+'journal-publications-keywords.json') as data_file:
        data = json.load(data_file)

#    x   = data[0]
#    pub = np.array(x['articles'])
#    pubyear = pub[:, 0]
#    pubcount= pub[:, 1] * 0

    ax = plt.subplot(111)

    for ind in range(0, len(data)):
        x = data[ind]
        pub = np.array(x['articles'])
        journal=x['name']
        #pubcount += pub[:, 1]
        #pprint(pub)
        ax.plot(pub[:, 0], pub[:, 1], lw=2, label=journal)
#ax.set_ylim([0, 200])
    plt.grid(True)
    plt.xlabel('year')
    plt.ylabel('number of publications')
    plt.legend(loc='upper left', shadow=False, fontsize='x-small')
    plt.savefig(keyword+'publication.pdf', bbox_inches='tight')
    plt.close()

#plt.show()
#print pub[:, 0], pub[:, 1]
#print len(data)
