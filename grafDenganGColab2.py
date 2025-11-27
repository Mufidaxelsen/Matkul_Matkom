import networkx as nx
graf_berarah = nx.DiGraph()

graf_berarah.add_nodes_from(["A","B","C","D","E"])
graf_berarah.add_edges_from([("A","B"),("B","C"),("C","D"),("D","E"),("E","A")])
nx.draw(graf_berarah,with_labels=True)

derajat_masuk = graf_berarah.in_degree()
print("derajat masuk semua simpul =", derajat_masuk)

derajat_keluar = graf_berarah.out_degree()
print("derajat keluar semua simpul =", derajat_keluar)

derajat_masuk_C = graf_berarah.in_degree("C")
print("derajat keluar semua simpul C =", derajat_masuk_C)

derajat_keluar_C = graf_berarah.in_degree("C")
print("derajat keluar semua simpul C =", derajat_keluar_C)

total_derajat_graf_berarah = sum(d for n, d in graf_berarah.degree())
print(f"Total derajat graf berarah: {total_derajat_graf_berarah}")