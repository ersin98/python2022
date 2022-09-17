sayi1= 20
sayi2=20
sayi3=20
#en küçüğü bulma
if sayi2<sayi3 and sayi2<sayi1:
  print("En küçük=",sayi2)
elif sayi1<sayi2 and sayi1<sayi3:
  print("En küçük=",sayi1)
elif sayi3<sayi1 and sayi3<sayi2:
  print("En küçük=",sayi3)
else:
  print("Sayılar eşit! Sayı=",sayi2)
#en büyüğü bulma
if sayi2>sayi3 and sayi2>sayi1:
  print("En büyük=",sayi2)
elif sayi1>sayi2 and sayi1>sayi3:
  print("En büyük=",sayi1)
elif sayi3>sayi1 and sayi3>sayi2:
  print("En büyük=",sayi3)
else:
  print("")