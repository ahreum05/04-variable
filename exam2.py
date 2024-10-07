# str() : 데이터를 문자열로 변경
# int() : 숫자로 된 문자열을 정수로 변경
# float() : 숫자로 된 문자열을 실수로 변경 
a = 5
b = 7.7
c = True
print(a, b, c)
print(type(a), type(b), type(c))
print('-' * 20)-

a = str(a)
b = str(b)
c = str(c)
print(a, b, c)
print(type(a), type(b), type(c))
print('-' * 20)

a = int(a)
b = float(b)
print(a, b)
print(type(a), type(b))
print('-' * 20)