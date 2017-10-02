def anti_vowel(text): #"amar"
  st=[]
  x=len(text)
  for i in range(x):
    y=text[i]
    if y!='A' and y!='a' and y!='E' and y!='e' and y!='I' and y!='i' and y!='O' and y!='o' and y!='U' and y!='u':
      st.append(text[i])
  for i in st:
    st="".join(st)
  return st
print(anti_vowel("Amar"))
