__author__ = 'jamie'


class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def __str__(self):
        s = ""
        for i in self.D[0]:
            for j in self.D[1]:
                if (i, j) in self.f.keys():
                    s += "[{0}, {1}] = {2}".format(i, j, self.f[i, j]) + "\n"
                else:
                    s += "[{0}, {1}] = 0".format(i, j) + "\n"
        return s

