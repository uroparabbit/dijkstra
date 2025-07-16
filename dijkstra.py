# 사용자가 사전 설정을 위해 조작하는 변수들
points = 5 # 지점 개수 (ex: points = 5이면 0, 1, 2, 3, 4라는 이름의 지점 존재)
roads = [
    # (0, 1, 1),
    # (1, 4, 6),
    # (0, 4, 3),
    # (0, 2, 2),
    # (2, 3, 4),
    # (3, 4, 2)
    (0, 1, 2),
    (0, 2, 5),
    (0, 4, 20),
    (1, 3, 2),
    (1, 2, 1),
    (2, 3, 1),
    (2, 4, 5),
    (3, 4, 1),
] # [출발점, 도착점, 거리] 순으로 기재
start_point = 0 # 내비게이션 출발 지점
finish_point = 4 # 내비게이션 도착 지점



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


visit(0)


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