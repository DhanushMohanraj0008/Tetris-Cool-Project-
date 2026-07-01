from tetromino import tetromino,pos


class Lblock(tetromino):
    def __init__(self):
        super().__init__(id = 3)
        # self.cells = {
        #     0:[pos(0, 2), pos(1, 0), pos(1, 1), pos(1, 2)],        # this contains a positional bug 
        #     1:[pos(0, 1), pos(1, 0), pos(2, 0), pos(3, 0)], 
        #     2:[pos(1, 0), pos(1, 1), pos(1, 2), pos(2, 0)],
        #     3:[pos(0, 2), pos(1, 0), pos(1, 1), pos(1, 2)]
        # }
        self.cells = {
            0: [pos(0,1), pos(1,1), pos(2,1), pos(2,2)],
            1: [pos(1,0), pos(1,1), pos(1,2), pos(2,0)],
            2: [pos(0,0), pos(0,1), pos(1,1), pos(2,1)],
            3: [pos(0,2), pos(1,0), pos(1,1), pos(1,2)]
}
        self.move(0, 3)
class Jblock(tetromino):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0:[pos(0, 0), pos(1, 0), pos(1, 1), pos(1, 2)],
            1:[pos(0, 1), pos(0, 2), pos(1, 1), pos(2, 1)], 
            2:[pos(1, 0), pos(1, 1), pos(1, 2), pos(2, 2)],
            3:[pos(0, 1), pos(1, 1), pos(2, 0), pos(2, 1)]
        }
        self.move(0, 3)
class Oblock(tetromino):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0:[pos(0, 0), pos(0, 1), pos(1, 0), pos(1, 1)], 
            1:[pos(0, 0), pos(0, 1), pos(1, 0), pos(1, 1)], 
            2:[pos(0, 0), pos(0, 1), pos(1, 0), pos(1, 1)],
            3:[pos(0, 0), pos(0, 1), pos(1, 0), pos(1, 1)]
        }
        self.move(0, 4) # (0, 4)
class Iblock(tetromino):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0:[pos(1, 0), pos(1, 1), pos(1, 2), pos(1, 3)],
            1:[pos(0, 2), pos(1, 2), pos(2, 2), pos(3, 2)], 
            2:[pos(2, 0), pos(2, 1), pos(2, 2), pos(2, 3)],
            3:[pos(0, 1), pos(1, 1), pos(2, 1), pos(3, 1)]
        }
        self.move(-1,3)
class Sblock(tetromino):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0:[pos(0, 1), pos(0, 2), pos(1, 0), pos(1, 1)],
            1:[pos(0, 1), pos(1, 1), pos(1, 2), pos(2, 2)], 
            2:[pos(1, 1), pos(1, 2), pos(2, 0), pos(2, 1)],
            3:[pos(0, 0), pos(1, 0), pos(1, 1), pos(2, 1)]
        }
        self.move(0,3)
class Tblock(tetromino):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0:[pos(0, 1), pos(1, 0), pos(1, 1), pos(1, 2)],
            1:[pos(0, 1), pos(1, 1), pos(1, 2), pos(2, 1)], 
            2:[pos(1, 0), pos(1, 1), pos(1, 2), pos(2, 1)],
            3:[pos(0, 1), pos(1, 0), pos(1, 1), pos(2, 1)]
        }
        self.move(0,3)
class Zblock(tetromino):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0:[pos(0, 0), pos(0, 1), pos(1, 1), pos(1, 2)],
            1:[pos(0, 2), pos(1, 1), pos(1, 2), pos(2, 1)], 
            2:[pos(1, 0), pos(1, 1), pos(2, 1), pos(2, 2)],
            3:[pos(0, 1), pos(1, 0), pos(1, 1), pos(2, 0)]
        }
        self.move(0,3)



