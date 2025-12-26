d = {
    "Alice" : 87,
    "Carol" : 95,
    "Virat" : 101,
    "Rohit" : 100
}
name = input("Enter a student's name : ")
if name in d:
  print(f"{name} 's marks : {d[name]}")

else:
  print("Student not found.")