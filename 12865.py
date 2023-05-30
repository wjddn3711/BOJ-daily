N, K = map(int,input().split())

# 최대 K 만큼의 무게만을 넣을 수 있는 배낭을 들고 다닐 수 있다
# 배낭에 넣을 수 있는 최댓값은?

# 핵심은 무게와 가치에 대한 관계를 떠올리는 것에 있다

# 무게: 0~K  / 가치: 무한, 먼저 0으로 초기화 해준다
dp = [[0]*(K+1) for _ in range(N+1)]

# input을 통해 무게와 값어치를 받아온다
for i in range(1,N+1):
    w,v = map(int, input().split())
    for j in range(1, K+1):
        # j는 현재 i개 중 더할 수 있는 무게
        if j < w :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

    