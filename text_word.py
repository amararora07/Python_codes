def censor(text, word):
  print text
  print word
  text=text.split()
  x=len(text)
  y=len(word)
  for i in range(x):
    if text[i]==word:
      text[i]="*"*y
  for i in text:
    st=" ".join(text)
  return st                 #to replace word in a text with *
print(censor("I am Amar Arora", "am"))
