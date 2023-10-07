n = int (input("Veuillez saisir la valeur de n : "))
s=0
for i in range(1 ,n+1) :
    s=s+1/ i
print("La somme est : ", format(s,".2f"))