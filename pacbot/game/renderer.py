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
                if mtr[i][j] == 0:
                    self.scene.render_rec((0, 0, 255), (j * self.x_diff, i * self.y_diff, self.x_diff, self.y_diff))
                if mtr[i][j] == 2:
                    self.scene.render_rec((255, 255, 255), (j * self.x_diff + 10, i * self.y_diff + 10, self.x_diff / 10, self.y_diff / 10))
                if mtr[i][j] == 3:
                    self.scene.render_rec((255, 255, 255), (j * self.x_diff + 5, i * self.y_diff + 5, self.x_diff / 2, self.y_diff / 2))


    def render_bait(self):
        pass

    def render_gost(self):
        pass

    def render_pac_man(self, pacman):
        pos = pacman.position
        self.scene.render_rec((0, 255, 0), (pos[0] * self.x_diff, pos[1] * self.y_diff, self.x_diff, self.y_diff))
