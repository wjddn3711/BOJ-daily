
import heapq
import sys

input = sys.stdin.readline

N = int(input())
"""
1. 왼쪽 힙과 오른쪽 힙의 길이가 같으면 (요소 * -1) 을 왼쪽 힙에 삽입한다.
1-1. 그렇지 않으면 오른쪽 힙에 삽입한다.
2. 왼쪽 힙과 오른쪽 힙에 요소가 존재하고, 왼쪽 힙의 (첫번째 요소* -1) 가 오른쪽 첫번째 요소보다 클 때
2-1. 왼쪽 힙의 첫번째 요소와 오른쪽 힙의 첫번째 요소를 바꿔준다. ( -1을 곱해준 뒤 바꿔준다. )
3. 왼쪽 힙의 (첫번째 요소 * -1)를 출력한다.
"""

min_h = []
max_h = []

# sorting을 통하였을때 시간초과가 발생하였음

for _ in range(N):
    number = int(input())
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, -number)
    else:
        heapq.heappush(min_h, number)
    if min_h and max_h:
        # 최소 힙에서의 최대값이 최대 힙에서의 최소값보다 작을 경우
        if min_h[0] < -max_h[0]:
            max_val  = -heapq.heappop(max_h)
            min_val = -heapq.heappop(min_h)

            heapq.heappush(min_h, max_val)
            heapq.heappush(max_h, min_val)
    print(-max_h[0])