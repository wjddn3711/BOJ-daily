# 컨테이너 간의 스왑만 가능하다
# 컨테이너 안의 공의 개수는 swap을 하더라도 불변하다
# 각 공의 종류별로의 합과 컨테이너안의 공의 수가 동일하여야 한다 (보다 쉽게 비교하기 위해 sorting 한다)


def organizingContainers(container):
    # Write your code here
    n = len(container)
    balls_count = [0] * n
    container_count = [0] * n

    for i in range(n):
        for j in range(n):
            balls_count[j] += container[i][j]
            container_count[i] += container[i][j]

    if sorted(balls_count) == sorted(container_count):
        return "possible"
    return "impossible"
