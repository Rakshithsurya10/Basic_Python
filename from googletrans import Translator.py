from googletrans import Translator
t=Translator()
a=input("Enter text u want to convert : ")
b=input("Enter target language: ")
res=t.translate(a,dest+b)
print(res.text)