from pacbot.game.maze import Maze


class Player:

    def __init__(self, x, y, color, maze: Maze):
        self.position = [x, y]
        self.direction = 0
        self.maze = maze
        self.color = color

        self.moving = False
        self.next_direction = 0
        self.moves = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]

    def set_position(self, x, y):
        self.position = [x, y]

    def change_direction(self, direction):
        self.next_direction = direction

    def possible_directions(self):
        directions = []
        for i in range(len(self.moves)):
            if i == 0:
                continue
            movement = Player.can_move(self.maze, [self.moves[i][0], self.moves[i][1]])
            if movement['can_move']:
                directions.append(i)
        return directions

    def move(self):
        next_direction_move = Player.can_move(self.maze, Player.sum_pos(self.position, self.moves[self.next_direction]))
        direction_move = Player.can_move(self.maze, Player.sum_pos(self.position, self.moves[self.direction]))
        self.moving = True
        if next_direction_move['can_move']:
            self.direction = self.next_direction
            self.position = next_direction_move['new_pos']
        elif direction_move['can_move']:
            self.position = direction_move['new_pos']
        else:
            self.moving = False
            self.direction = self.next_direction

    @staticmethod
    def can_move(maze: Maze, pos):
        if pos[0] < 0:
            pos[0] = maze.width - 1
        if pos[0] >= maze.width:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = maze.height - 1
        if pos[1] >= maze.height:
            pos[1] = 0
        return {'can_move': 0 != maze.mtr[pos[1]][pos[0]], 'new_pos': pos}

    @staticmethod
    def sum_pos(pos1, pos2):
        return [pos1[0] + pos2[0], pos1[1] + pos2[1]]
