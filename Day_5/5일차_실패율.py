import numpy as np

def solution(N, stages):
    stages = np.array(stages)
    fail = []
    answer = []

    for i in range(N):
        if np.max(stages) < i+1:
            fail.append(0)
            continue
        failure = np.sum(np.where(stages == i + 1, True, False)) / np.sum(np.where(stages >= i + 1, True, False))
        fail.append(failure)

    for i in range(len(fail)):
        idx = np.argmax(fail)
        answer.append(idx + 1.)
        fail[idx] = - 1.0

    return answer