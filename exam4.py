# index : 데이터의 위치값
#양수 0123456
#음수 7654321
s1 = 'abcdefg'
print(s1)
print('-' * 20)

# indexing (인덱싱)
# => 문자 1개 선택
# [번호]
print(s1[0])
print(s1[3])
print(s1[6])
print(s1[-3])
print('-' * 20)

# slicing (슬라이싱)
# => 문자 여러개 선택
# [start: end: step] : start~end-1 사이의 step값만큼 건너뛴 문자
print(s1[1:6:1])
print(s1[1:6:2])
print(s1[1:6:3])
print('-' * 20)

# [start: end] : start~end-1 사이의 step=1값만큼 건너뛴 문자
print(s1[1:6:1])
print(s1[1:6])
print('-' * 20)

# [start: ] : start~끝까지 step=1값만큼 건너뛴 문자
print(s1[1:])
print('-' * 20)

# [: end] : 0~end-1 사이의 step=1값만큼 건너뛴 문자
print(s1[:4])
print('-' * 20)

# [start: end: step=음수] 
# start~end-1 사이의 step값만큼 오른쪽에서 왼쪽으로 건너뛴 문자
print(s1)
print(s1[::-1])
print(s1[-1:-8:-1])  # step=-1일때, gfedcba 1개씩 건너서 선택
print('-' * 20)


