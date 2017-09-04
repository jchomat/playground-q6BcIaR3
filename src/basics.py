print("*** If Else ***")
day = "False"

if day == "True":
  print("Hello, World!")
else:
  print("Good Night, World!")

print("*** Iterators ***")

my_days = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']

my_iter = iter(my_days)

while True:
  try:
    print(next(my_iter))
  except StopIteration:
    break