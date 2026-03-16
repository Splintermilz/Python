# L'objectif est de craquer le mot de passe "target".

# Parcourez le fichier "wordlist.txt" et pour chaque mdp de la liste,
# comparez son hash avec la cible.


import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

target = "00dfb72e6375b0206c10c62e34e783c5c58787d982d2cd54eec4bccd033bc5b9"

with open("wordlist.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()      # Lit toutes les lignes d'un coup → retourne une liste
    for line in lines:
        password = line.strip()
        if hash_password(password) == target:
            print(f"Mot de passe trouvé : {password}")
            break
    else:
        print("Mot de passe non trouvé dans la wordlist.")