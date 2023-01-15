import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np


df = pd.read_csv('data/visited_apps.csv')
print(df.shape)

developers = pickle.load(open('data/app_developers', 'rb'))
play_store_developers = len(developers)
play_store_apps = df.shape[0]

labels = ['Apps', 'Developers', ' Apps', ' Developers']

df = pd.read_csv('data/app-store/visited_apps.csv')
print(df.shape)

apple_store_apps = df.shape[0]
apple_store_developers = 719124

data = [[labels[0], play_store_apps, 'Play-Store'], [labels[1], play_store_developers, 'Play-Store'],
        [labels[2],apple_store_apps, 'IOS-Store'], [labels[3], apple_store_developers, 'IOS-Store']]
data = pd.DataFrame(data, columns = ['Object', 'Value', 'Type'])


colors = {'Play-Store':'#ff574a', 'IOS-Store':'#00d1c0'}
c = data['Type'].apply(lambda x: colors[x])


ax = plt.subplot(111) #specify a subplot

bars = ax.bar(data['Object'], data['Value'], color=c, width=0.4, edgecolor='#FCC201') #Plot data on subplot axis
ax.bar_label(bars, labels=['2.5166', data['Value'][1]/1000000, '1.2412', data['Value'][3]/1000000],fontsize=10)

for i, j in colors.items(): #Loop over color dictionary
    ax.bar(data['Object'], data['Value'],width=0,color=j,label=i) #Plot invisible bar graph but have the legends specified
plt.xlabel("Data Scrapped", labelpad=10, fontsize=12)
plt.ylabel("Total number (in millions)", labelpad=10, fontsize=12)


ax.legend()

plt.title("Unified App Scrapper Results",fontsize=14, pad=10)
plt.legend()

plt.show()

