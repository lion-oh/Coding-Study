from collections import deque

def solution(bridge_length, weight, truck_weights):
    idx = 0 # 시간
    truck1 = [] # 지나온 트럭
    truck2 = deque(truck_weights) # 대기중인 트럭
    bridge = deque([0], maxlen=bridge_length) # 다리 위 트럭

    while len(truck1) < len(truck_weights):
        idx += 1

        if bridge[0] != 0:
            truck1.append(bridge.popleft())

        if len(truck2) == 0:
            bridge.append(0)
            continue

        if sum(bridge) + truck2[0] <= weight:
            bridge.append(truck2.popleft())

        else:
            bridge.append(0)

    return idx



# from collections import deque
#
#
# def solution(bridge_length, weight, truck_weights):
#     idx = 0
#     stop = 0
#     truck2 = deque(truck_weights)
#     bridge = deque([0], maxlen=bridge_length)
#
#     while stop < len(truck_weights):
#         idx += 1
#
#         if bridge[0] != 0:
#             bridge.popleft()
#             stop += 1
#
#         if len(truck2) == 0:
#             bridge.append(0)
#             continue
#
#         if sum(bridge) + truck2[0] <= weight:
#             bridge.append(truck2.popleft())
#
#         else:
#             bridge.append(0)
#
#     return idx


# from collections import deque
#
#
# def solution(bridge_length, weight, truck_weights):
#     idx = 0
#     truck2 = deque(truck_weights)
#     bridge = deque([0], maxlen=bridge_length)
#
#     while True:
#         idx += 1
#
#         if len(truck2) == 0:
#             break
#
#         if bridge[0] != 0:
#             bridge.popleft()
#
#
#         if sum(bridge) + truck2[0] <= weight:
#             bridge.append(truck2.popleft())
#
#         else:
#             bridge.append(0)
#
#     print(bridge)
#     return idx
#
print(solution(100, 100, [10]))

