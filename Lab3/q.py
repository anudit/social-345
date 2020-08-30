from random import uniform
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv
import os

def make_label_dict(labels):
    l = {}
    for i, label in enumerate(labels):
        l[i] = label
    return l


size = 10000

p = 0.01
while p<=1:
    print(f"Generating {p}")
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for r in range(len(matrix)):
        for c in range(r, len(matrix[r])):
            if(uniform(0, 1) <= p):
                matrix[r][c] = 1
                matrix[c][r] = 1

    with open(f"{p}-matrix.csv","w", newline='') as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerow([x for x in range(0, len(matrix)+1)])
        for index, row in enumerate(matrix):
            csvWriter.writerow([index+1] + row)

    input_data = pd.read_csv(f"{p}-matrix.csv", index_col=0)

    with open(f"{p}-matrix.csv", 'r') as f:
        d_reader = csv.DictReader(f)
        headers = d_reader.fieldnames

    labels=make_label_dict(headers)

    doplot = False
    if (doplot == True):
        print(f"Plotting {p}")
        G = nx.Graph(input_data.values)
        pos = nx.circular_layout(G)
        plt.figure(3,figsize=(120, 120))
        nx.draw(G, pos)
        # edge_labels = dict( ((u, v), d["weight"]) for u, v, d in G.edges(data=True) )
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # nx.draw(G,pos,node_size=200, labels=labels, with_labels=True)
        # plt.show()
        plt.savefig(f"{p}-plot.jpg" )
        # os.remove(f"{p}-matrix.csv")
    p += 0.1
