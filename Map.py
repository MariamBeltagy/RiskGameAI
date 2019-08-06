# constants for better understanding
NP = 0  # empty territory
P1 = 1  # player 1
P2 = 2  # player 2


class Map:
    def __init__(self, number):
        self.map = []
        # EGYPT
        if number == 0:
            self.map.append(0)  # 0
            self.map.append((2, 3, 14, 21))  # 1
            self.map.append((3, 1))  # 2
            self.map.append((1, 2, 4, 9, 10, 14))  # 3
            self.map.append((3, 9, 5))  # 4
            # check 5 again
            self.map.append((4, 6, 9, 10, 11, 12))  # 5
            self.map.append((5,))  # 6
            self.map.append((13, 8))  # 7
            self.map.append((13, 17, 18))  # 8
            self.map.append((3, 4, 5, 10, 11))  # 9
            self.map.append((3, 9, 5, 11, 14))  # 10
            self.map.append((10, 9, 5, 12, 16, 14))  # 11
            self.map.append((5, 11, 13, 16, 17))  # 12
            self.map.append((12, 7, 8, 17))  # 13
            self.map.append((1, 3, 10, 11, 16, 15, 19, 20, 21))  # 14
            self.map.append((14, 19))  # 15
            self.map.append((14, 11, 12, 17, 23, 19))  # 16
            self.map.append((8, 13, 12, 16, 18, 23))  # 17
            self.map.append((8, 17))  # 18
            self.map.append((14, 15, 16, 20, 23))  # 19
            self.map.append((21, 14, 19, 23, 22))  # 20
            self.map.append((1, 14, 20, 22, 24, 25, 26, 27))  # 21
            self.map.append((20, 21, 23, 24))  # 22
            self.map.append((16, 17, 19, 20, 22, 24, 25, 26, 27))  # 23
            self.map.append((21, 22, 23, 25))  # 24
            self.map.append((21, 24, 23, 26, 27))  # 25
            self.map.append((25,))  # 26
            self.map.append((21, 25, 23))  # 27

        # USA
        if number == 1:
            print("kill me please")
