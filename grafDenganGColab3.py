import networkx as nx
graf_berbobot = nx.Graph()

graf_berbobot.add_edge("A", "B", bobot=5)
graf_berbobot.add_edge("A", "C", bobot=10)
graf_berbobot.add_edge("B", "C", bobot=15) 
graf_berbobot.add_edge("B", "D", bobot=20) 
graf_berbobot.add_edge("C","E", bobot=25)

pos = nx.spring_layout (graf_berbobot) 
nx.draw(graf_berbobot,pos, with_labels=True)
labels=nx.get_edge_attributes (graf_berbobot, "bobot") 
nx.draw_networkx_edge_labels (graf_berbobot,pos,edge_labels=labels)