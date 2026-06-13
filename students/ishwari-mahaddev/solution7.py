score = int(input("Enter score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
  
  #problem2
def is_leap_year(year):
    if (year % 4== 0):
      return True
    else:
        return False
year = int(input("Enter year: "))

print(year, "->", is_leap_year(year))
print(is_leap_year(2020))

#problem3
def sum_to_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter a number: "))
print("Sum =", sum_to_n(n))

#problem4
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n*i)
