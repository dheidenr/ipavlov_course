import calendar

year = 2017
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)

print(calendar.isleap(2017))
subject = "оптимизация"
author = "Donald Knuth"

string = rf"{subject}, {author} c:\\"
print(string)
print(int("-2"))

print(bool(0.0))

x = 0
y = 12
name = x or y
print(name)

print("привет"[:])
print(b"test")
# print(b"тест")
print(b"")