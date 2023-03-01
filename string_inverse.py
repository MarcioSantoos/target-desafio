text = input()
k = len(text) - 1

itext = []
for i in range(len(text)):
  itext.append(text[k-i])

for k in range(len(itext)):
  print(itext[k], end='')