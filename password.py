import random
import hashlib


mot_de_pass = input("entrer votre mots de passe: ")
def password(mdp):
   
    if len (mdp) < 8 :
        print("mots de passe courte, minimum 8 caractères")
    minuscule = False
    majuscule = False
    chiffre = False
    special = False
    for i in range(len(mdp)) :
        if mdp[i] >= "a" and mdp[i]<="z":
            minuscule = True 

        if mdp[i] >= "A" and mdp[i]<="Z":
            majuscule = True 

        if mdp[i] >= "0" and mdp[i]<="9":
            chiffre = True       
   
        if mdp[i] =="!" or mdp[i]== "@" or mdp[i]== "#" or mdp[i]== "$" or mdp[i]== "%" or mdp[i]== "^"or mdp[i]== '&' or mdp[i]== "*":
            special=True

    """if (minuscule, majuscule, chiffre, special) == True:
        print("mot de passe valide")"""
 
    if minuscule == False:
        print("le mot de passe doit comptenir au moins une lettre minuscule")

    elif majuscule == False:
        print("le mot de passe doit comptenir au moins une lettre majuscule")
        
    elif chiffre == False:
        print("le mot de passe doit comptenir au moins un cfhiffr")

    elif special == False:
        print("le mot de passe doit comptenir au moins un caractere special")

    else:
        if (minuscule, majuscule, chiffre, special):
            print("mot de passe valide")
            crypte = hashlib.sha256(mdp.encode()).hexdigest()
            print (crypte)

    
password(mot_de_pass)