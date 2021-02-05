import numpy as np

def solution(n, lost, reserve):
    """

    :param n: 전체 학생 수
    :param lost: 도난당한 학생 idx
    :param reserve: 여벌의 체육복을 갖는 학생 idx
    :return: 체육수업을 들을 수 있는 학생의 수 최댓값
    """
    answer = np.ones(n)
    lost_idx = np.array(lost)
    res_idx = np.array(reserve)

    answer[lost_idx-1] -= 1
    answer[res_idx-1] += 1

    for i in range(len(answer)):
        try:
            if answer[i] - answer[i + 1] == 2:
                answer[i + 1] += 1
                answer[i] -= 1
            elif answer[i] - answer[i + 1] == -2:
                answer[i] += 1
                answer[i + 1] -= 1

        except:
            pass

    answer = np.where(answer >= 2, 1, answer)

    return int(np.sum(answer))

print(solution(5, lost=[2,4], reserve=[1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))





