import json
import numpy as np

import matplotlib as matplotlib
import matplotlib.pyplot as plt
import plotsettings as plotsettings

matplotlib.style.use('seaborn-paper')

#publishable = plotsettings.Set('Cell')
#publishable.set_figsize(1.5, 1.0, aspect_ratio = 0.95)
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
#matplotlib.rc('text', usetex=False)

new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']

ax = plt.subplot(111)
pubcount = 0
with open('journal-publications-new.json') as data_file:
    dataall = json.load(data_file)
    x   = dataall[0]
    pub = np.array(x['articles'])
    pubyear = pub[:, 0]
    pubcount= pub[:, 1] * 0
    
    for ind in range(0, len(dataall)):
        x = dataall[ind]
        pub = np.array(x['articles'])
        journal=x['name']
        ax.fill_between(pub[:, 0], pubcount, pubcount+pub[:, 1], \
                        facecolor=new_colors[ind], alpha=0.75, \
                        edgecolor='none')
        pubcount += pub[:, 1]
        ax.plot(pub[:, 0], pubcount, lw=1.5, label=journal,\
                color=new_colors[ind], alpha=1)

ax.set_xlim([1947, 2017])
ax.set_ylim([0, 15000])
plt.xlabel('year')
plt.ylabel('number of publications')
plt.legend(loc='upper left', shadow=False, fontsize='small')
plt.savefig('total_publication.pdf', bbox_inches='tight')
plt.close()

#publishable.set_figsize(1.0, 1.0, aspect_ratio = 0.95)

keywords = ["for the first time", "novel", "excellent", "robust", "unique", "unprecedented", "promising", "remarkable", "encouraging", "enormous",
    "cutting-edge","state-of-the-art","preeminent"]

for keyword in keywords:
    
    with open(keyword+'journal-publications-keywords.json') as data_file:
        data = json.load(data_file)

    ax = plt.subplot(111)

    for ind in range(0, len(dataall)):
        x = dataall[ind]
        puball = np.array(x['articles'])
        journal=x['name']
        
        for indj in range(0, len(data)):
            xs = data[indj]
            journals=xs['name']
            pub = np.array(xs['articles'])
            if(journals == journal):
                break

        print journals, journal
        print keyword
        print
        
        pubyear = pub[:, 0]
        
        medianyear = np.zeros(14)
        ratio = np.zeros(14)
        counts = 0
        for years in range(1947, 2017, 5):
            index = (pubyear > years) & (pubyear <= years+5)
            medianyear[counts] = np.median(pubyear[index])
            ratio[counts] = np.sum(pub[index, 1])/(0.0+np.sum(puball[index, 1]))
            counts = counts+1
        ax.plot(medianyear[:], ratio[:], lw=2, label=journal, color=new_colors[ind])

    ax.set_xlim([1947, 2017])
    #ax.set_ylim([0.00, 0.10])
    plt.xlabel('year')
    plt.ylabel('number of publications')
    plt.legend(loc='upper left', shadow=False, fontsize='x-small')
    plt.savefig(keyword+'publication.pdf', bbox_inches='tight')
    plt.close()

