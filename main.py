teksts = input("Ievadi tekstu: ")
def reverseText(text):
  if len(text)>1:
    sar1 = []
    for burts in text:
      sar1.append(burts)
    sar1.reverse()
    text = ""
    for elements in sar1:
      text += elements
    text = text.upper()
    print(text)
  else:
    text = "Parāk īss teksts!"
    print(text)
  return text
reverseText(teksts)