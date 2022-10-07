# user enter the year he want to investigate
print('the year you wnat to investigate =')
year = int(input())
# case 1 if the reminder of devision is 0, then the year is a leab year
if (year % 400 == 0) and (year % 100 == 0):
    print('the is leap year')
# case 2 if the reminder of the devision is =0,then the year is a leab year
elif (year % 4 == 0) and (year % 100 == 0):
    print('the year is a leap year')
# otherwise the year is not a leab year
else:
    print('the year is not a leap year')
# ---------------------------------------------------------------------------------------------------2

# Enter the length of the person
print('plz enter your length')
length = int(input())
# case1   if the length is more than or equal (170cm),then the the person is tall
if (length > 170) or (length == 170):
    print('the person is tall')
# case2    if the length is less than (170cm) and more than (160cm),then the person is normal
elif (length < 170) and (length > 160):
    print('the person is normal')
# case3    if the length is less than (150cm),then the person is short
elif (length < 150):
    print('the person is short')
# otherwise there is a wrong in length
else:
    print('there is a wrong')
