# 사용자가 사전 설정을 위해 조작하는 변수들
points = 5
roads = [
    (0, 1, 1),    # 0 → 1 (거리 1)
    (1, 4, 1),    # 1 → 4 (거리 1)  ← finish_point
    (0, 2, 10),   # 0 → 2 (거리 10)
    (2, 3, 10),   # 2 → 3 (거리 10)
]
start_point = 0
finish_point = 4

"""
위 예시는, 전체 노드를 모두 방문하는지, 아니면 finish_point 노드에 방문 후 프로그램을 끝내는지에 따라
다른 결과가 나온다. 
"""

# 아래부터 Dijkstra 알고리즘
max_int = 100000
visited_points = []
distances = [max_int for _ in range(points)]
distances[start_point] = 0
paths = [[0] for _ in range(points)]


def visit(point):
    connected_roads = [i for i in roads if i[0] == point] # 연결되어 있는 도로
    self_distance = distances[point]
    
    for road in connected_roads:
        road_finish_point = road[1]
        road_length = road[2]

        if distances[road_finish_point] > self_distance + road_length: # 현재 distances에 있는 거리가 더 길면
            distances[road_finish_point] = self_distance + road_length # 갱신
            paths[road_finish_point] = paths[point] + [road_finish_point]

    visited_points.append(point)


def choose_point_to_visit():
    chosen_point = 0
    chosen_point_distance = max_int

    for i in range(points):
        if distances[i] < chosen_point_distance and not i in visited_points: # 방문되지 않은 지점 중 현재 거리가 가장 짧은 것 선정
            chosen_point = i
            chosen_point_distance = distances[i]
        
    return chosen_point


visit(start_point)


n = 0
# print("전부")
# while len(visited_points) < points:
while not finish_point in visited_points:
    visit(choose_point_to_visit())

    if n >= 100:
        print("무한 반복 방지를 위해 자동 반복문 탈출 (1)")
        break
    n += 1


print("--- 각 지점별 최단거리 ---")
for i in range(points):
    print(f"지점 {i} 최단거리: {distances[i]}")
    print(f"경로: {paths[i]}")