from IEHistory import IEHistory
import collections
import matplotlib.pyplot as plt
import numpy as np

url=[]
visitCount=[]
for i in range(len(IEHistory)):
    url.append(IEHistory[i][0])
    visitCount.append(int(IEHistory[i][1]))

def main():
    def Web_list(urls):
        visit_CoUnt = visitCount
        web_sig_url = []

        for i in range(len(urls)):
            if 'http' in urls[i]:
                slash = urls[i].split('/')
                if '' in slash:
                    blank = slash.index('')
                    del (slash[blank])
                    web_sig_url.append(slash[1])

        Website = []
        for i in range(len(web_sig_url)):
            dot = web_sig_url[i].split('.')
            if dot[0] != 'www' and len(dot) <= 2:
                dot_space = " " + dot[0]
                Website.append(dot_space * visit_CoUnt[i])
            elif dot[0] == 'm':
                dot_space = " " + dot[2]
                Website.append(dot_space * visit_CoUnt[i])
            elif dot[1] == 'helpstart' or dot[1] == 'msafflnk':
                dot_space = " " + dot[0]
                Website.append(dot_space * visit_CoUnt[i])
            elif dot[1] == 'cafe':
                dot_space = " " + dot[2]
                Website.append(dot_space * visit_CoUnt[i])
            else:
                dot_space = " " + dot[1]
                Website.append(dot_space * visit_CoUnt[i])
        url_data = Website
        count = "".join(url_data).split()

        Counter = collections.Counter(count)
        return (Counter)
    sort = sorted(Web_list(url).items(), key=lambda x: (x[1], x[0]))
    Counter=dict(sort)

    y = list(Counter.keys())
    visit_count= list(Counter.values())
    upY = []
    upvisit_count = []

    if len(visit_count)>15:
        for i in range(0,15):
            upY.append(y[i])
            upvisit_count.append(visit_count[i])
        max_visit = max(upvisit_count)

    else:
            for i in range(0,len(visit_count)):
                upY.append(y[i])
                upvisit_count.append(visit_count[i])

            max_visit = max(upvisit_count)

    models = ['Visit Count']
    yticks = upY
    data = {'Visit Count': upvisit_count}
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    colors = ['salmon']
    height = 0.2

    for i, model in enumerate(models):
        pos = compute_pos(yticks, height, i, models)
        bar = ax.barh(pos, data[model], height=height *2, label=model, color=colors[i])
        present_width(ax, bar)

    ax.set_xlim([0, max_visit+1])
    ax.xaxis.set_tick_params(labelsize=10)
    ax.set_xlabel('Visit Count', fontsize=14)

    ax.set_yticks(range(len(yticks)))
    ax.set_yticklabels(yticks, fontsize=8)
    ax.set_ylabel('Web Site', fontsize=14)

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True, ncol=1)

    ax.set_axisbelow(True)
    ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)

    plt.title('Internet Explorer 9 TOP'+str(len(upY)))
    plt.show()

def compute_pos(yticks, height, i, models):
    index = np.arange(len(yticks))
    n = len(models)
    correction = i - 0.5 * (n - 1)
    return index + height * correction

def present_width(ax, bar):
    for rect in bar:
        witdh = rect.get_width()
        posx = witdh * 1.01
        posy = rect.get_y() + rect.get_height() * 0.5
        ax.text(posx, posy, '%d' % witdh, rotation=0, ha='left', va='center')