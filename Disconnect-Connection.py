import pandas as pd
import networkx as nx
import xlsxwriter

data = pd.read_csv(r'result2.csv')
graph = nx.from_pandas_edgelist(data, 'auth1', 'auth2', edge_attr='num')

wb = xlsxwriter.Workbook('Disconnect-connection.xlsx')
ws = wb.add_worksheet()

ws.write(0, 0, 'auth1')
ws.write(0, 1, 'auth2')

r = 1

p = nx.shortest_path(graph)

nodes = list(p.keys())

for d in p.items():
    currentKey = d[0]

    for i in nodes:
        ConnectionType = ''

        if d[1].get(i, -1) != -1 :
            path = d[1][i]

            if len(path) > 2:
                ConnectionType = 'Indirect'
            elif len(path) == 2:
                ConnectionType = 'Direct'

##            print('paths from node {} to node {}'.format(currentKey, i))
##            print(path)
##            print(ConnectionType)

        else:
##            print('There is no path between {} and {}'.format(currentKey, i))
            ConnectionType = 'Disconnect'
##            print(ConnectionType)

            ws.write(r, 0, currentKey)
            ws.write(r, 1, i)

            r += 1

wb.close()
