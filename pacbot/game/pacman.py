class PacMan:

    # will create enum for direction 1: top, 2: right, 3: bottom, 4:left
    def __init__(self, posx, posy):
        self.position = [posx, posy]
        self.direction = 0
        self.next_direction = 0
        pass
    # will refactor :D
    def move(self, area):
        np = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
        p = self.position
        d = self.direction
        nd = self.next_direction
        if self._can_move(area, [p[0] + np[nd][0], p[1] + np[nd][1]]):
            self.direction = self.next_direction
            self.position[0] = p[0] + np[nd][0]
            self.position[1] = p[1] + np[nd][1]
        elif self._can_move(area, [p[0] + np[d][0], p[1] + np[d][1]]):
            self.position[0] = p[0] + np[d][0]
            self.position[1] = p[1] + np[d][1]
        if self.position[0] < 0:
            self.position[0] = area.width - 1
        if self.position[0] >= area.width:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = area.height - 1
        if self.position[1] >= area.height:
            self.position[1] = 0

    def change_direction(self, direction):
        self.next_direction = direction

    def _can_move(self, area, pos):
        if pos[0] < 0:
            pos[0] = area.width - 1
        if pos[0] >= area.width:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = area.height - 1
        if pos[1] >= area.height:
            pos[1] = 0
        return 0 != area.mtr[pos[1]][pos[0]]
        pass
