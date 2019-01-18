class PhylogicColorList():
    def __init__(self,as_hex=False,as_float=False):
        self.color_list = [[0,0,0],
                      [39, 140, 24], # 1
                      [103, 200, 243], # 2
                      [248, 139, 16], # 3
                      [16, 49, 41], # 4
                      [93, 119, 254], # 5
                      [152, 22, 26], # 6
                      [104, 236, 172], # 7
                      [249, 142, 135], # 8
                      [55, 18, 48], # 9
                      [83, 82, 22], # 10
                      [247, 36, 36], # 11
                      [0, 79, 114], # 12
                      [243, 65, 132], # 13
                      [60, 185, 179], # 14
                      [185, 177, 243],
                      [139, 34, 67],
                      [178, 41, 186],
                      [58, 146, 231],
                      [130, 159, 21],
                      [161, 91, 243],
                      [131, 61, 17],
                      [248, 75, 81],
                      [32, 75, 32],
                      [45, 109, 116],
                      [255, 169, 199],
                      [55, 179, 113],
                      [34, 42, 3],
                      [56, 121, 166],
                      [172, 60, 15],
                      [115, 76, 204],
                      [21, 61, 73],
                      [67, 21, 74],  # Additional colors, uglier and bad
                      [123, 88, 112],
                      [87, 106, 46],
                      [37, 66, 58],
                      [132, 79, 62],
                      [71, 58, 32],
                      [59, 104, 114],
                      [46, 107, 90],
                      [84, 68, 73],
                      [90, 97, 124],
                      [121, 66, 76],
                      [104, 93, 48],
                      [49, 67, 82],
                      [71, 95, 65],
                      [127, 85, 44], #even more additional colors, gray 
                                          [88,79,92],
                                          [220,212,194],
                                          [35,34,36],
                                          [200,220,224],
                                          [73,81,69],
                                          [224,199,206],
                                          [120,127,113],
                                          [142,148,166],
                                          [153,167,156],
                                          [162,139,145]]
        if as_hex:
            self.color_list = [self.rgb2hex(c) for c in self.color_list]
        if as_float:
            self.color_list = [list(map(lambda x: x/256.,c)) for c in self.color_list]
            
    def __len__(self):
        return len(self.color_list)
    def __iter__(self):
        return self.color_list
    def __getitem__(self,i):
        if i==0:
            raise ValueError("No cluster 0 please")
        elif i>=len(self.color_list):
            if self.as_hex:
                return rgb2hex([162,139,145])
            elif self.as_float:
                return [162./256,139./256,145./256]
            else:
                return [162,139,145] 
        return self.color_list[i]
    def validrgb(self,triple):
        if len(triple) != 3:
            return False
        for val in triple:
            if not isinstance(val,int):
                if val != 0.:
                    return False
            elif val not in list(range(256)):
                return False
        return True
    def rgb2hex(self,rgb_triple):
        r,g,b = rgb_triple
        if not self.validrgb(rgb_triple):
            raise ValueError("Not valid integer RGB triple: %s" % rgb_triple)
        else:
            return '#%02x%02x%02x' % tuple(rgb_triple)


