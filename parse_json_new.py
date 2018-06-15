import json
import numpy as np

import matplotlib as matplotlib
import matplotlib.pyplot as plt
#import plotsettings as plotsettings

matplotlib.style.use('seaborn-paper')

#publishable = plotsettings.Set('Nature')
#publishable.set_figsize(1.0, 1.0, aspect_ratio = 0.95)
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
    pubyear = pubyear.flatten()
    pub_cumu_count= np.zeros(len(pub[:, 0]))
    
    for ind in range(0, len(dataall)):
        x = dataall[ind]
        pub = np.array(x['articles'])
        journal = x['name']
        pubcount= np.array(pub[:, 1])
        pubcount= pubcount.flatten()
        ax.fill_between(pubyear[(pubcount>0)], \
                        pub_cumu_count[(pubcount>0)]\
                        , pub_cumu_count[(pubcount>0)]+pubcount[(pubcount>0)], \
                        facecolor=new_colors[ind], alpha=0.75, \
                        edgecolor='none')
        pub_cumu_count += pubcount
        ax.plot(pubyear[(pubcount>0)],\
                pub_cumu_count[(pubcount>0)], lw=2, label=journal,\
                color=new_colors[ind], alpha=1)

ax.set_xlim([1947, 2017])
ax.set_ylim([0, 15000])
plt.xlabel('year')
plt.ylabel('number of publications')
plt.legend(loc='upper left', shadow=False, fontsize='small')
plt.savefig('total_publication.pdf', bbox_inches='tight')
plt.close()


keywords = ["for the first time", "unique", "robust", "novel", "excellent", "unprecedented", "promising", "remarkable", "encouraging", "enormous",
    "cutting-edge","state-of-the-art","preeminent"]

#publishable.set_figsize(1.6, 1.2, aspect_ratio = 0.95)

fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12)) = plt.subplots(3, 4)

ax1.xaxis.label.set_visible(False)

fig.subplots_adjust(hspace=0.3, wspace=0.2)

i = 0
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()

    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()

    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0

    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    ratio = ratio * 100
    if(journal != "NewA"):
        ax1.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax1.set_xlim([1947, 2017])
ax1.set_title(keyword, loc='left')


i = 1
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100

    if(journal != "NewA"):
        ax2.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax2.set_xlim([1947, 2017])
ax2.set_title(keyword, loc='left')


i = 2
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100
    if(journal != "NewA"):
        ax3.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax3.set_xlim([1947, 2017])
ax3.set_title(keyword, loc='left')

i = 3
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1

    ratio = ratio * 100

    if(journal != "NewA"):
        ax4.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax4.set_xlim([1947, 2017])
ax4.set_title(keyword, loc='left')


i = 4
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100

    if(journal != "NewA"):
        ax5.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax5.set_xlim([1947, 2017])
ax5.set_title(keyword, loc='left')


i = 5
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100

    if(journal != "NewA"):
        ax6.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax6.set_xlim([1947, 2017])
ax6.set_title(keyword, loc='left')


i = 6
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100
    
    if(journal != "NewA"):
        ax7.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax7.set_xlim([1947, 2017])
ax7.set_title(keyword, loc='left')

i = 7
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100

    if(journal != "NewA"):
        ax8.plot(medianyear, ratio,\
                 lw=1.5, label=journal, color=new_colors[ind])

ax8.set_xlim([1947, 2017])
ax8.set_title(keyword, loc='left')


i = 8
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    
    for years in range(1947, 2017, 5):
        index = (pubyear > years) & (pubyear <= years+5)
        medianyear[counts] = np.median(pubyear[index])
        if(np.sum(puballcount[index]) > 0):
            ratio[counts] = np.sum(pubcount[index])/(0.0+np.sum(puballcount[index]))
        counts = counts+1
    
    ratio = ratio * 100

#if(journal != "NewA"):
        #ax9.plot(medianyear, ratio,\
        #         lw=1.5, label=journal, color=new_colors[ind])

ax9.set_xlim([1947, 2017])
ax9.set_title(keyword, loc='left')


i = 9
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0
    

ax10.set_xlim([1947, 2017])
ax10.set_title(keyword, loc='left')


i = 10
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0


ax11.set_xlim([1947, 2017])
ax11.set_title(keyword, loc='left')


i = 11
keyword = keywords[i]
with open(keyword+'journal-publications-keywords.json') as data_file:
    data = json.load(data_file)

for ind in range(0, len(dataall)):
    x = dataall[ind]
    puball = np.array(x['articles'])
    journal=x['name']
    puballcount = puball[:, 1]
    puballcount = puballcount.flatten()
    
    for indj in range(0, len(data)):
        xs = data[indj]
        journals=xs['name']
        pub = np.array(xs['articles'])
        if(journals == journal):
            break

    pubyear = pub[:, 0]
    pubcount= pub[:, 1]
    pubyear = pubyear.flatten()
    pubcount= pubcount.flatten()
    
    medianyear = np.zeros(14)
    ratio = np.zeros(14)
    counts = 0


ax12.set_title(keyword, loc='left')

ax1.set_xticklabels([])
ax2.set_xticklabels([])
ax3.set_xticklabels([])
ax4.set_xticklabels([])
ax5.set_xticklabels([])
ax6.set_xticklabels([])
ax7.set_xticklabels([])
ax8.set_xticklabels([])

ax12.set_xlim([1947, 2017])

ax9.set_xticklabels( [' ', '1950', ' ', '1970', ' ', '1990', ' ', '2010'])
ax10.set_xticklabels([' ', '1950', ' ', '1970', ' ', '1990', ' ', '2010'])
ax11.set_xticklabels([' ', '1950', ' ', '1970', ' ', '1990', ' ', '2010'])
ax12.set_xticklabels([' ', '1950', ' ', '1970', ' ', '1990', ' ', '2010'])

ax1.set_ylim([0, 8])
ax2.set_ylim([0, 5])
ax3.set_ylim([0, 5])
ax4.set_ylim([0, 5])
ax5.set_ylim([0, 5])
ax6.set_ylim([0, 5])
ax7.set_ylim([0, 5])
ax8.set_ylim([0, 5])
ax9.set_ylim([0, 5])
ax10.set_ylim([0, 5])
ax11.set_ylim([0, 5])
ax12.set_ylim([0, 5])

ax1.set_ylabel(' ')
ax5.set_ylabel('relative frequency (%)')
ax9.set_ylabel(' ')

ax9.set_xlabel('year')
ax10.set_xlabel('year')
ax11.set_xlabel('year')
ax12.set_xlabel('year')

fig.set_size_inches(8, 6)
plt.savefig('keyword_publication.pdf', bbox_inches='tight')


