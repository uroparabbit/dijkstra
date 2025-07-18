print("다익스트라 알고리즘")

# 사용자가 사전 설정을 위해 조작하는 변수들
points = 19 # 지점 개수 (ex: points = 5이면 0, 1, 2, 3, 4라는 이름의 지점 존재)
roads = [
    (0, 1, 481.5),
    (1, 2, 146.8), (1, 3, 176.1),
    (2, 3, 45.4), (2, 4, 125.4),
    (3, 4, 195.8),
    (4, 5, 232.6),
    (5, 6, 318.1), (5, 7, 520),
    (6, 7, 250.1), (6, 8, 296.3),
    (7, 9, 257.4),
    (8, 9, 253.6), (8, 10, 112.9), (8, 13, 1200),
    (9, 11, 202.9),
    (10, 11, 225), (10, 12, 168),
    (11, 15, 185.8),
    (12, 13, 116.8), (12, 14, 140),
    (14, 15, 126.8), (14, 16, 69.8),
    (15, 17, 78.4),
    (16, 17, 81.9),
    (17, 18, 309)
] # (출발점, 도착점, 거리) 순으로 기재
start_point = 0 # 내비게이션 출발 지점
finish_point = 18 # 내비게이션 도착 지점

# 길 쌍방향 설정
for i in range(len(roads)):
    roads.append((roads[i][1], roads[i][0], roads[i][2]))


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
while len(visited_points) < points:
# while not finish_point in visited_points:
    visit(choose_point_to_visit())

    if n >= 100:
        print("무한 반복 방지를 위해 자동 반복문 탈출 (1)")
        break
    n += 1


print("--- 각 지점별 최단거리 ---")
for i in range(points):
    print(f"지점 {i} 최단거리: {distances[i]}")
    print(f"경로: {paths[i]}")