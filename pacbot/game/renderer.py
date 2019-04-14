# this is not a good design
class Renderer:
    def __init__(self, scene):
        self.scene = scene
        pass

    def render_area(self, area):
        mtr = area.mtr
        x_diff = self.scene.width/len(mtr[0])
        y_diff = self.scene.height/len(mtr)
        for i in range(len(mtr)):
            for j in range(len(mtr[i])):
                if mtr[i][j] != 1:
                    self.scene.render_rec((0, 0, 255), (j*x_diff, i*y_diff, x_diff, y_diff))


    def render_bait(self):
        return True

    def render_gost(self):
        return True

    def render_pac_man(self):
        return True
