def remove_duplicates(numbers):
  st=[]
  for i in numbers:
    if i not in st:
      st.append(i)
      
  return st
print(remove_duplicates([4,5,5,4]))
