#write a program that determine whether a year enter by the user is a leap year or not using if-elif-else statement.

def isleapyear(year):
 if(year%4==0 and year%100!=0) or year%400==0:
  return True
 else:
  return False 
   
year = 2019

if isleapyear(year):
  print("{} is a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))