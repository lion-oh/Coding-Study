import numpy as np

def solution(answer):

    # array에서 각 인덱스별 대소비교 시, 배열의 shape이 맞아야 1:1로 비교를 함.
    supo_1 = np.array([[1,2,3,4,5] for x in range(2000)]).flatten()
    supo_2 = np.array([[2,1,2,3,2,4,2,5] for x in range(1250)]).flatten()
    supo_3 = np.array([[3,3,1,1,2,2,4,4,5,5] for x in range(1000)]).flatten()

    ans = answer

    idx = len(ans)

    score = []

    score.append(np.sum(ans == supo_1[:idx]))
    score.append(np.sum(ans == supo_2[:idx]))
    score.append(np.sum(ans == supo_3[:idx]))

    result = max(score)
    return [i+1 for i, j in enumerate(score) if j == result]


