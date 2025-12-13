print("Mayo Club:")
count=int(input("how many people:"))
counter=0
list=""
for i in range(count):
  counter+=1
  a=input("name:")
  b=input("last name:")
  print(f"name:{a}")
  print(f"last name:{b}")
  list+=f"full name:{a}" "{b}"
print(list)
print("people:{counter}")
