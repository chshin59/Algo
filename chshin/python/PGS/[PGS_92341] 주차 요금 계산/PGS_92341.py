from math import ceil


def solution(fees, records):
    numbers = set()
    for idx in range(len(records)):
        records[idx] = records[idx].split()
        numbers.add(records[idx][1])

    numbers = sorted(numbers)

    d1 = dict(zip(numbers, [0] * len(numbers)))
    d2 = dict(zip(numbers, [0] * len(numbers)))



    # 자동차 번호 별 이용시간 합계 계산
    for record in records:
        time, num, inout = record
        if inout == "IN":
            d1[num] = time
        else:
            h2, m2 = map(int, time.split(":"))
            h1, m1 = map(int, d1[num].split(":"))
            d2[num] += (60 * h2 + m2) - (60 * h1 + m1)
            d1[num] = 0


    # 출차 내역이 없는 경우 23:59에 출차
    for key, value in d1.items():
        if value:
            h2, m2 = 23, 59
            h1, m1 = map(int, value.split(":"))
            d2[key] += (60 * h2 + m2) - (60 * h1 + m1)


    # 최종요금계산
    answer = list(d2.values())
    for idx in range(len(answer)):
        # 기본요금
        if answer[idx] <= fees[0]:
            answer[idx] = fees[1]
        # 추가요금
        else:
            # answer[idx] = fees[1] + ceil((answer[idx] - fees[0]) / fees[2]) * fees[3]
            answer[idx] = fees[1] - (-(answer[idx] - fees[0]) // fees[2]) * fees[3]
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]
print(solution(fees, records))
