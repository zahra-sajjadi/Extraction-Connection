from cmath import nan
from numpy import NaN
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import xlsxwriter


data = pd.read_excel(r'result2.xlsx')
graph = nx.from_pandas_edgelist(data, 'auth1', 'auth2', edge_attr='num')
nx.draw_networkx(graph)

# plt.show()
# print(nx.shortest_path(graph, source=1, target=2,weight=1))
p = nx.shortest_path(graph)
# print(p)


wb = xlsxwriter.Workbook('Direct-connection.xlsx')
sh = wb.add_worksheet()

sh.write(0, 0, 'auth1')
sh.write(0, 1, 'auth2')

row = 1

wb2 = xlsxwriter.Workbook('Indirect-connection.xlsx')
sh2 = wb2.add_worksheet()

sh2.write(0, 0, 'auth1')
sh2.write(0, 1, 'auth2')
row2=1

for d in p.items():
    ConnectionType = ''
    keys = d[1].keys()
   # print(d)

    for i in keys:
        currentKey = d[0] 
        path = d[1][i]
        if len(path) > 2:
            ConnectionType = 'Indirect'
            sh2.write(row2, 0, currentKey)
            sh2.write(row2, 1, i)
            row2 += 1
        elif len(path) == 2:
            ConnectionType = 'Direct'
            sh.write(row, 0, currentKey)
            sh.write(row, 1, i)
            row += 1
                   


##        print('paths from node {} to node {}'.format(currentKey, i))
######        print(path)
##        print(ConnectionType)


wb.close()  
wb2.close()      

