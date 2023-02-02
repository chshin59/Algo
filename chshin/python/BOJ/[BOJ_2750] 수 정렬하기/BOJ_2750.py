N = int(input())

numbers = []

for _ in range(N):
  numbers.append(int(input()))

for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if numbers[i] > numbers[j]:
      numbers[i], numbers[j] = numbers[j], numbers[i]

for _ in numbers:
  print(_)