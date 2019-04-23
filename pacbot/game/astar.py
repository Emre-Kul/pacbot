# a* algorithm
import sys

from pacbot.game.maze import Maze


class AStar:
    def __init__(self, maze: Maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        pass

    def get_path(self):
        founded = False
        open_nodes = [{'pos': self.start, 'parent': -1, 'cost': 0}]
        closed_nodes = []
        while len(open_nodes) > 0 and not founded:
            current_idx = self._least_f_index(open_nodes)
            current = open_nodes[current_idx]
            closed_nodes.append(current)
            del open_nodes[current_idx]
            if current['pos'][0] == self.end[0] and current['pos'][1] == self.end[1]:
                founded = True
            for child in self.maze.get_avaliable_pos(current['pos']):
                if AStar._get_pos_index(closed_nodes, child) != -1:
                    continue
                search_open = AStar._get_pos_index(open_nodes, child)
                cost = self._get_f_cost(child)
                if search_open == -1:
                    open_nodes.append({'pos': child, 'parent': len(closed_nodes) - 1, 'cost': cost})
                elif open_nodes[search_open]['cost'] > cost:
                    open_nodes[search_open]['cost'] = cost
        return closed_nodes


    def _least_f_index(self, nodes):
        if len(nodes) <= 0:
            return -1
        min_index = 0
        min_f = nodes[0]['cost']
        for i, node in enumerate(nodes):
            f_cost = self._get_f_cost(node['pos'])
            if f_cost < min_f:
                min_f = f_cost
                min_index = i
        return min_index

    def _get_f_cost(self, pos):
        g_cost = abs(pos[0] - self.start[0]) + abs(pos[1] - self.start[1])
        h_cost = abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])
        return g_cost + h_cost

    @staticmethod
    def _get_pos_index(nodes, pos):
        for idx, node in enumerate(nodes):
            if node['pos'][0] == pos[0] and node['pos'][1] == pos[1]:
                return idx
        return -1

