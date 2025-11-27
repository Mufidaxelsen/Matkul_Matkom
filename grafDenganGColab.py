import networkx as nx
graf = nx.Graph()

graf.add_node("A")
graf.add_node("B")
graf.add_node("C")
graf.add_node("D")
graf.add_node("E")


graf.add_edge("A","B")
graf.add_edge("A","C")
graf.add_edge("A","D")
graf.add_edge("D","C")

nx.draw(graf,with_labels=True)

derajat_semua_node = graf.degree()
print("derajat semua simpul =",derajat_semua_node)

derajat_node_E = graf.degree("E")
print("derajat simpul E =",derajat_node_E)

total_derajat = sum(d for n, d in derajat_semua_node)
print("total derajat =",total_derajat)