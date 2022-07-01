def tribonacci(limit):
    prev_prev = 0
    prev = 0
    cur = 1
    count = 0

    while count < limit:
        result = prev_prev
        prev_prev, prev, cur = prev, cur, prev_prev + prev + cur
        count += 1
        yield result


for i in tribonacci(6):
    print(i)
