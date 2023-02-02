import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
cards = list(map(int, input().split()))

black_jack = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if black_jack < cards[i] + cards[j] + cards[k] <= M:
                black_jack = cards[i] + cards[j] + cards[k]

print(black_jack)