import numpy as np

# def solution(people, limit):
#     """
#
#     :param people: 무인도에 갇힌 사람의 몸무게
#     :param limit: 구명보트 무게 제한
#     :return: 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
#     """
#     origin_p = sorted(people)
#     next_p = np.array(origin_p)
#     limit = limit
#
#     cnt = 0
#
#     idx, = np.where(np.array(next_p) <= limit/2)
#
#     if (len(idx) == 1):
#         for i in range(len(next_p)):
#             try:
#                 if next_p[i] + next_p[i+1] <= limit:
#                     cnt += 1
#                     origin_p.remove(next_p[i])
#             except:
#                 pass
#
#         # print(origin_p)
#         cnt += len(origin_p)
#         return cnt
#
#     elif (len(idx) >= 2) & (len(idx) % 2 == 0):
#         cnt += len(idx) // 2
#         for i in list(idx):
#             origin_p.remove(next_p[i])
#
#         # print(origin_p)
#         cnt += len(origin_p)
#         return cnt
#
#     elif ( len(idx) >= 2) & (len(idx) % 2 == 1):
#         cnt += len(idx) // 2
#         for i in range(len(idx) - 1):
#             origin_p.remove(next_p[idx[i]])
#
#         next_p = origin_p
#         # print(next_p)
#         for i in range(len(next_p)):
#             try:
#                 if next_p[i] + next_p[i+1] <= limit:
#                     cnt += 1
#                     origin_p.remove(next_p[i])
#             except:
#                 pass
#
#         # print(origin_p)
#         cnt += len(origin_p)
#         return cnt
#
#     else:
#         return len(origin_p)



def solution(people, limit):
    """

    :param people: 무인도에 갇힌 사람의 몸무게
    :param limit: 구명보트 무게 제한
    :return: 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
    """
    origin_p = sorted(people)
    limit = limit

    cnt = 0
    idx = 0  # first

    while True:
        try:
            if origin_p[idx] + origin_p[idx+1] <= limit:
                cnt += 1
                origin_p.remove(origin_p[idx])
                origin_p.remove(origin_p[idx])
            else:
                cnt += 2
                origin_p.remove(origin_p[idx])
                origin_p.remove(origin_p[idx])
        except:
            pass

        if len(origin_p) == 1:
            cnt += 1
            break
        elif len(origin_p) == 0:
            break
    return cnt


print(solution([40, 40, 60, 60, 100], 100))
30, 30, 70, 70

