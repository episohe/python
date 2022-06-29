# Chapter05-03
# 일급 합수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수 값, 상태(레퍼런스) 복사 후 저장 후에 접근(엑세스) 가능

# 클로저 사용
def closure_ex1():
    series = []

    # Free Variable
    # 클로저 영역

    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print('------------------------------------------------')

print(dir(avg_closure1))
print('------------------------------------------------')
print(dir(avg_closure1.__code__))
print('------------------------------------------------')
print(avg_closure1.__code__.co_freevars)

print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 클로저 사용 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()

print(avg_closure2(15))
print(avg_closure2(35))
print(avg_closure2(40))
