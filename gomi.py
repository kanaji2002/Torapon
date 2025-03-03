import networkx as nx

def find_shortest_path(graph, start, goal):
    """
    Dijkstra法を使って最短経路を求める
    :param graph: NetworkXのグラフ
    :param start: 開始地点
    :param goal: 目的地
    :return: 最短経路リストと距離
    """
    try:
        path = nx.shortest_path(graph, source=start, target=goal, weight='weight', method='dijkstra')
        distance = nx.shortest_path_length(graph, source=start, target=goal, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, float('inf')

# サンプルグラフの作成
G = nx.Graph()
edges = [
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5), ('B', 'D', 10),
    ('C', 'D', 3), ('D', 'E', 8), ('E', 'A', 7)
]
G.add_weighted_edges_from(edges)

# ユーザーの入力
start = input("現在地を入力してください: ")
goal = input("目的地を入力してください: ")

# 最短経路の計算
path, distance = find_shortest_path(G, start, goal)

if path:
    print(f"最短経路: {' → '.join(path)}")
    print(f"合計距離: {distance}")
else:
    print("経路が見つかりません。")
