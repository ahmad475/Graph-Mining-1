import networkx as nx
import matplotlib.pyplot as plt

options = {

    'node_color': 'blue',

    'node_size': 1,

    'width': 0.1,

}
############################################################################################
###creating network 
g = nx.erdos_renyi_graph(1000, 0.021, seed=None, directed=False)
  
Gcc = sorted(nx.connected_components(g), key=len, reverse=True)
G0 = g.subgraph(Gcc[0])

nx.draw(G0,**options)
print(nx.info(G0))
print(nx.number_connected_components(G0))


plt.suptitle('er3')
plt.savefig("netwo.png")
plt.close()


############################################################################################
###degree distribution related
degrees = [G0.degree(n) for n in G0.nodes()]
plt.hist(degrees,density=True)

plt.suptitle('er3: Node degree distribution of the graph')
plt.xlabel('K')
plt.ylabel('P(K)')
plt.savefig("histo.png")
plt.close()


############################################################################################
###clustering coefficent related
l1=[]
for n in G0.nodes():
    tup = (G0.degree(n),nx.clustering(G0,nodes=n))
    l1.append(tup)
zip(*l1)
plt.scatter(*zip(*l1))

plt.suptitle('er3: Distribution of the local clustering coefficient')
plt.xlabel('K(degree)')
plt.ylabel('Clustering Coefficient')
plt.savefig("scatter.png")
plt.close()


############################################################################################
### shortest path length
iter1 = nx.all_pairs_shortest_path_length(G0,cutoff=None)
l1=dict(iter1)
plt.hist(l1[0].values()) 

plt.suptitle('er3: Distribution of the shortest path lengths')
plt.xlabel('Path Length')
plt.ylabel('Frequncy')
plt.savefig("barg.png")
plt.close()


############################################################################################
### Stats 
# III.	The global clustering coefficient of the graph(a number)(average clustering)
print("this is Global Clustering Coefficient:")
print(nx.average_clustering(G0))


# V.	The average shortest path length of the graph(a number)

print("This is average Shortest Path:")
print(nx.average_shortest_path_length(G0))


# VI.	The diameter of the graph(a number)
print("this is diameter:")
print(nx.diameter(G0))


############################################################################################