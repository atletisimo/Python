Совршен број е број кој е еднаков на збирот на своите вистински делители, односно делителите што се помали од самиот број.
Примери:
6 → делители: 1, 2, 3 → 1 + 2 + 3 = 6 ✅

28 → делители: 1, 2, 4, 7, 14 → 1 + 2 + 4 + 7 + 14 = 28 ✅

10 → делители: 1, 2, 5 → 1 + 2 + 5 = 8 ❌ (не е совршен)

def is_perfect(n):
 sum_deliteli=0
 for i in range(1,n):
     if n%i==0:
      sum_deliteli=sum_deliteli+i
 return sum_deliteli==n # kje vrati true/false dali zbitoy na deliteli e ednakov na samiot toj broj


n=int(input("Vnesi broj: "))
if(is_perfect(n)):
    print(f"{n} e perfecten broj") #f пред наводниците значи “formatted string literal” — овозможува да вметнеш променливи директно во текстот со {}.
  #  print(n, "e perfecten broj")
else:
    print(f"{n} ne e perfecten broj")
#   print(n, "ne e perfecten broj")
