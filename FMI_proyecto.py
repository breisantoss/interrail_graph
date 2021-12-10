import numpy as np
import networkx as nx 
import pandas as pd

## Importamos los datos y los convertimos en un DataFrame
df = pd.read_csv('tren.csv')
df.head(8)
TREN = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Distancia')

TREN.nodes()
TREN.edges()
TREN.order()

djk_path=nx.dijkstra_path(TREN, source='Vigo', target='Berna', weight=True)
djk_path
