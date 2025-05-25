from collections import defaultdict

class node():
    def __init__(self, ten, Cha=None):
        self.ten = ten
        self.Cha = Cha
    def display(self):
        print(self.ten)


data = defaultdict(list)
data['A'] = ['D','N','K']
data['D'] = ['G']
data['N'] = ['S','P']
data['K'] = ['Z']
data['S'] = ['T','C']
data['Z'] = ['B','M']
for leaf in ['T','C','P','G','B','M']:
    data[leaf] = []


def ktra(tam, ds):
    for v in ds:
        if v.ten == tam.ten:
            return True
    return False


def duongdi(n):
    duong = []
    while n is not None:
        duong.append(n.ten)
        n = n.Cha
    print(' -> '.join(duong[::-1]))


def DFS(To, Tg):
    mo = []
    dong = []
    mo.append(To)

    while mo:
        n = mo.pop()
        if n.ten == Tg.ten:
            print('Tìm kiếm thành công bằng DFS, đường đi là:')
            duongdi(n)
            return
        dong.append(n)
        for v in reversed(data[n.ten]):
            tam = node(v)
            if not ktra(tam, mo) and not ktra(tam, dong):
                tam.Cha = n
                mo.append(tam)

    print('Tìm kiếm không thành công.')


DFS(node('A'), node('M'))
