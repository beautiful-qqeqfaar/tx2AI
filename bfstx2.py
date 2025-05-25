from collections import deque

doThi = {
    'A': ['D', 'N', 'K'],
    'D': ['G'],
    'N': ['S', 'P'],
    'K': ['Z'],
    'G': [],
    'S': ['T', 'C'],
    'P': [],
    'Z': ['B', 'M'],
    'T': [],
    'C': [],
    'B': [],
    'M': []
}

def tim_duong_di_bfs(dothi, bat_dau, ket_thuc):
    queue = deque()
    queue.append([bat_dau])
    daQua = set()

    while queue:
        duong_di = queue.popleft()
        node = duong_di[-1]

        if node == ket_thuc:
            return duong_di

        if node not in daQua:
            daQua.add(node)

            for ke in dothi[node]:
                duong_moi = list(duong_di)
                duong_moi.append(ke)
                queue.append(duong_moi)

    return None


start_node = 'A'
end_node = 'P'

duong_di = tim_duong_di_bfs(doThi, start_node, end_node)

if duong_di:
    print("from", start_node, "to", end_node, "la: ", " -> ".join(duong_di))
else:
    print("XXX: ", start_node, "to", end_node)
