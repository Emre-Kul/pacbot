# this is not a good design
class Renderer:
    def __init__(self, scene, area):
        self.area = area
        self.scene = scene
        self.x_diff = self.scene.width/self.area.width
        self.y_diff = self.scene.height/self.area.height
        pass

    def render_area(self):
        mtr = self.area.mtr
        for i in range(len(mtr)):
            for j in range(len(mtr[i])):
                if mtr[i][j] != 1:
                    self.scene.render_rec((0, 0, 255), (j * self.x_diff, i * self.y_diff, self.x_diff, self.y_diff))


    def render_bait(self):
        pass

    def render_gost(self):
        pass

    def render_pac_man(self, pacman):
        pos = pacman.position
        self.scene.render_rec((0, 255, 0), (pos[0] * self.x_diff, pos[1] * self.y_diff, self.x_diff, self.y_diff))
