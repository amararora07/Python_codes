def reverse(text):
  st=[]
  ts=[]
  x=len(text)
  while x>0:
    st.append(text[x-1])
    x-=1
  for i in st:
    ts="".join(st)
    
  return ts

print(reverse("amar"))
