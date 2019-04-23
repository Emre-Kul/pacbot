from pacbot.game.maze import Maze


class Actor:

    def __init__(self, x, y, color, maze: Maze):
        self.position = [x, y]
        self.direction = 0
        self.maze = maze
        self.color = color

        self.moving = False
        self.next_direction = 0
        self.moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def set_position(self, x, y):
        self.position = [x, y]

    def change_direction(self, direction):
        self.next_direction = direction

    def possible_directions(self):
        directions = []
        for i in range(len(self.moves)):
            movement = self.maze.is_avaliable([self.moves[i][0], self.moves[i][1]])
            if movement['avaliable']:
                directions.append(i)
        return directions

    def get_direction_from_next_pos(self, next_pos):
        for idx, move in enumerate(self.moves):
            if self.position[0] + move[0] == next_pos[0] and self.position[1] + move[1] == next_pos[1]:
                return idx
        return -1

    def move(self):
        next_direction_move = self.maze.is_avaliable(Actor.sum_pos(self.position, self.moves[self.next_direction]))
        direction_move = self.maze.is_avaliable(Actor.sum_pos(self.position, self.moves[self.direction]))
        self.moving = True
        if next_direction_move['avaliable']:
            self.direction = self.next_direction
            self.position = next_direction_move['new_pos']
        elif direction_move['avaliable']:
            self.position = direction_move['new_pos']
        else:
            self.moving = False
            self.direction = self.next_direction

    @staticmethod
    def sum_pos(pos1, pos2):
        return [pos1[0] + pos2[0], pos1[1] + pos2[1]]
