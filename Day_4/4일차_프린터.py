import numpy as np
import collections

def solution(prior, location):
    data = np.array(prior)
    cnt =0
    max_num = np.max(prior)
    location_num = data[location]

    if location_num == max_num:
        cnt += 1.
        return cnt

    idx, = np.where(data > location_num)
    for i in idx:
        if i == idx[-1]:
            max_idx = i

            if np.sum(location_num == prior) > 1.:
                idx, = np.where(prior == location_num)
                new_loc = np.argmin(np.abs(idx - location))  # 몇번째인지
                cnt += (len(data) - max_idx) + (np.abs(0 - new_loc))

            else:
                data.pop(i)
                cnt += 1.

        data.pop(i)
        cnt += 1.

     # 본인 출력 카운트
    return cnt

print(solution([1,1,9,1,1,1], 0))





