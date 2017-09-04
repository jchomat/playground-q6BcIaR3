# Welcome!

This Python template is my first try on python3

just wanna learn to deal with it : Basics

```python runnable

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

```

# Advanced usage

@[Luke, how many stars are there in these galaxies?]({"stubs": ["src/basics.py"], "command": "python3 src/basics.py"})

If you want a more complex example (external libraries, viewers...), use the [Advanced Python template](https://tech.io/select-repo/429)
