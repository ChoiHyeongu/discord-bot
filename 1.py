year=int(input('년도를 입력해주세요. : '))
print("윤년" if year%400 == 0 or (year%4 == 0 and year % 100 != 0) else "아님")
