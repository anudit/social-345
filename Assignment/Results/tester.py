import networkx as codebase
import matplotlib.pyplot as plt
import csv

def store(el, name):
    with open(name, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in el:
            writer.writerow(row)

# 145/1258

# G = codebase.erdos_renyi_graph(145,0.02)
# data = [[e[0],e[1]] for e in G.edges]
# store(data, 'er15s.csv')

G2 = codebase.barabasi_albert_graph(n=1258, m=10)
data = [[e[0],e[1]] for e in G2.edges]
store(data, 'ba15.csv')
