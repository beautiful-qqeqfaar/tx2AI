def tim_duong_di_dfs(dothi, bat_dau, ket_thuc):
    stack = []
    stack.append([bat_dau])
    daQua = set()

    while stack:
        duong_di = stack.pop()
        node = duong_di[-1]

        if node == ket_thuc:
            return duong_di

        if node not in daQua:
            daQua.add(node)

            for ke in reversed(dothi[node]):
                duong_moi = list(duong_di)
                duong_moi.append(ke)
                stack.append(duong_moi)

    return None



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

start_node = 'A'
end_node = 'P'

duong_di = tim_duong_di_dfs(doThi, start_node, end_node)

if duong_di:
    print("from", start_node, "to", end_node, "la: ", " -> ".join(duong_di))
else:
    print("XXX: ", start_node, "to", end_node)
