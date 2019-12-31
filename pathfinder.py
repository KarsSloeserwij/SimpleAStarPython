import math
class Astar():

	def __init__(self, board):
		self.board = board
		pass

	def get_distance(self, a, b):
		return abs(a.x - b.x) + abs(a.y - b.y)

	def retrace_path(self, start, end):
		print("FOUND PATH")
		path = []

		currentState = end;

		while(currentState != start):
			path.append(currentState);
			currentState = currentState.parent;
			#print("Removing Parent: " + path[path.size() - 1].name);
			path[len(path) - 1].parent = None;

		path.reverse()
		print(path)
		return path;



		pass;

	def find_path(self, start, end):
		open_set = []
		closed_set = []

		open_set.append(start);

		while len(open_set) > 0:
			current_node = open_set[0]


			for i in range(len(open_set)):
				if(open_set[i].f_cost() <= current_node.f_cost() or open_set[i].h_cost < current_node.h_cost):
					current_node = open_set[i]

			open_set.remove(current_node);
			closed_set.append(current_node);
			print(current_node.x, current_node.y)
			print(end.x, end.y)

			#current_node.checked = True

			if current_node == end:
				return self.retrace_path(start, end)

			for neighbour in self.board.get_cell_neighbours(current_node.x , current_node.y):
				if(neighbour in closed_set):
					continue;
				new_movement_cost = current_node.g_cost + self.get_distance(current_node, neighbour);
				if new_movement_cost < neighbour.g_cost or neighbour not in open_set:
					neighbour.g_cost = new_movement_cost;
					neighbour.h_cost = self.get_distance(neighbour, end);
					neighbour.parent = current_node;
					if ( neighbour not in open_set):
						open_set.append(neighbour);
