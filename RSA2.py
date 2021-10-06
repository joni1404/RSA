


Buchstaben = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def e_auswahl(phi):
    teiler = []
    e_kandidaten = []
    for i in range(2,(int(phi**0.5)//1)+1):
        if phi%i == 0:
            teiler.append(i)

    for j in range(2,phi):
        e_kandidaten.append(j)
        for i in teiler:
            if j%i == 0:
                e_kandidaten.remove(j)
                break
    return e_kandidaten                
def wort_zu_zahl(word):
    
    num = []
    word = word.upper()
    for letter in word:
           
        a = str(Buchstaben.index(letter))
        if int(a) < 10:
            a = "0"+a
            
        num.append(int(a))
       
    return num
def encryption(code,e,n):
    num = []
    for i in code :
        
        
         
        
        
        num.append((i**e)%n)
    return num
def decryption(cipher,d,n):
    fin = []
    for i in cipher:
        

        
        x =((int(i)**int(d))%int(n))
        fin.append(x)
        
        
        
    return fin
def zahl_zu_wort (num):




    fin = ""
    for i in num:
        kek = Buchstaben[i]
        
        
        fin+=kek
    return fin



print("--Schlüssel erstellen--")
q = int(input("Primzahl 1 (q): "))
p = int(input("Primzahl 2 (p): "))
q = 11
p = 17
n = p*q
phi = (p-1)*(q-1)
e_kan = e_auswahl(phi)
if input("Wollen Sie ein eigenes e wählen? ") == "ja":
    print(e_kan[1:10])
    e = int(input("Wählen Sie eine der Möglichkeiten "))
else:
    e = e_kan[0]
    for i in e_kan:
        if (1+phi)/i %1 == 0:
            e = i
            break
e = 7          


d = (phi+1)/e
print(12*"-")
print("privat key: ", q,p, "d: "+str(d),sep='\n')
print(12*"-")
print("public key: ", "n: "+str(n),"e: "+str(e),sep='\n')
wort = input("Welches Wort wollen Sie verschlüsseln: ")

wort_ascii = (wort_zu_zahl(wort))
print(12*"-")
print("Wort in ascii: " ,wort_ascii)
print(12*"-")



word_encrypted = encryption(wort_ascii,e,n)
print("Wort verschlüsselt: " ,word_encrypted)
print(12*"-")

word_decrypted = decryption(word_encrypted,d,n)
print("Entschlüsseltes Wort: ",zahl_zu_wort(word_decrypted))

