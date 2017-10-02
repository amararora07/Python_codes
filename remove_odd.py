def purify(numbers):
  st=[]
  for num in numbers:
    if num % 2==0:
    	st.append(num)
  return st
print(purify([4,3,3,3]))
