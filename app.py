print("Mayo Club:")
count=int(input("how many people:"))
number=0
counter=0
list=""
for i in range(count):
  counter+=1
  a=input("name:")
  b=input("last name:")
  print(f"person:{counter}")
  print(f"full name:{a} {b}")
  print()
  list+=f"{counter}.full name:{a} {b}"
  if counter!=count:
     list+="\n"
print(f"List of person:\n{list}\npeople:{counter}")

