names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 35]

zipped = zip(names, ages)

for name, age in zipped:
  print(f"{name} is {age} years old.")