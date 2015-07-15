
from graph import RandomGraphCreator
from map import Map

if __name__ == "__main__":
	n = 5

	rgc = RandomGraphCreator(debug=True)

	g = rgc.create(n_nodes=n)

	g.print_adjacency()

	g.print_edges()

	g.print_nodes()

	m = Map()

	m.import_from_graph(graph=g)

	m.print_rooms()

	m.print_map()
