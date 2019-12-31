class cell():
    def __init__(self, x, y, g_cost = 1, h_cost = 1):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.passable = True
        self.parent = None
        self.checked = False

    def set_passable(self, passable):
        self.passable = passable

    def f_cost(self):
        return self.g_cost + self.h_cost;
