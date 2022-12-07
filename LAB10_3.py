import json
import os.path
import matplotlib.pyplot as plt
import numpy as np


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

try:
    with open('data.json') as f:
        json_text = f.read()
        data=json.loads(json_text)
    girls=0
    boys=0
    for i in range(len(data['items'])):
        if data['items'][i]['gender']=='male':
            boys=boys+data['items'][i]['height']
        if data['items'][i]['gender']=='female':
            girls=girls+data['items'][i]['height']
        graf=[boys,girls]
        labexl=np.array(list(['boys','girls']))

    plt.pie(graf,labels=labexl,autopct=lambda pct: func(pct, graf))
    plt.title('Sum of Boys and girls height in class')
    plt.show()
except:
    print('file wasn`t found')