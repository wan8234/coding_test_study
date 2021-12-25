import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
money = int(input())

min_cost = min(prices)
min_num = prices.index(min_cost)

if N == 1:
	print(0)
	sys.exit()
	
num = money // min_cost
pick = [min_num for i in range(num)]
cost = num * min_cost

def comb(remains, digit):
	for i in range(digit, -1, -1):
		if pick[i] != N - 1:
			for j in range(N - 1, pick[i], -1):
				current = prices[j] - prices[pick[i]]
				if current <= remains:
					pick[i] = j
					comb(remains - current, digit - 1)
					return
	if not any(pick):
		if not pick:
			print(0)
			sys.exit()
		pick.pop()
		comb(remains + prices[0], digit - 1)

comb(money - cost, num - 1)

result = 0
for i in range(len(pick)):
	result += (10 ** i) * pick[i]

print(result)