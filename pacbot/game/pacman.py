class PacMan:

    # will create enum for direction 1: top, 2: right, 3: bottom, 4:left
    def __init__(self, posx, posy):
        self.position = [posx, posy]
        pass

    def move(self, area, direction):
        next_poss = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
        new_pos = [self.position[0], self.position[1]]
        new_pos[0] += next_poss[direction][0]
        new_pos[1] += next_poss[direction][1]
        if (0 <= new_pos[0] < area.width and
                0 <= new_pos[1] < area.height and
                area.mtr[new_pos[1]][new_pos[0]] != 0):
            self.position[0] = new_pos[0]
            self.position[1] = new_pos[1]
