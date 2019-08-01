import sys
sys.stdin = open("bus.txt", "r")


def solution(K, N, stops):
    answer = prev = 0
    status = K
    for i in range(len(stops) - 1):
        status -= stops[i] - prev
        if status < 0:
            return 0  # 만약 0보다 작다면 충전량으로 현재 정류소까지 갈 수 없으므로 0 반환
        if stops[i + 1] - stops[i] > status:
            status = K
            answer += 1
        prev = stops[i]

    # for문에서 마지막 정류소를 계산하지 않았으므로 마지막 정류소까지 계산
    last = stops[-1]
    status -= last - prev
    if N - last > K:
        return 0
    elif N - last > status:
        answer += 1
    return answer


def main():
    T = int(input())
    for test_case in range(T):
        K, N, M = map(int, input().split())
        stops = list(map(int, input().split()))
        print("#{} {}".format(test_case + 1, solution(K, N, stops)))


if __name__ == '__main__':
    main()