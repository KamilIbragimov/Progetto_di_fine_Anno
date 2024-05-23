from email_validator import validate_email, EmailNotValidError
import random
import string
import os
import requests
def password_generata() -> str:
    try:
        length = int(input("Inserisci la lunghezza desiderata per la password: "))
        if length < 8 or length>20:
            print("La lunghezza deve essere almeno di 8 caratteri e al massimo di 20 caratteri.")
            password_generata()
            return password_generata
        
        # Caratteri disponibili per la password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Aggiungi almeno un carattere maiuscolo, uno minuscolo, un numero e un carattere speciale
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        
        # Genera il resto della password casualmente
        remaining_length = length - 4
        password += ''.join(random.choice(characters) for _ in range(remaining_length))
        
        # Mescola la password per renderla più casuale
        lista_password = list(password)
        random.shuffle(lista_password)
        password = ''.join(lista_password)
        
        return password
    except ValueError:
        print("Errore: Inserisci un valore intero positivo per la lunghezza della password.")
        return ""

def verifica_email() -> str:
    while True:
        try:
            indirizzo_email = input("Inserisci un indirizzo email: ")
            validato = validate_email(indirizzo_email)
            print(f"L'indirizzo email '{indirizzo_email}' è valido.")
            return indirizzo_email
        except EmailNotValidError as e:
            
            print("Inserisci un indirizzo email valido.")


password_generata = password_generata()
email_inserita = verifica_email()





sito_collegato = input("Inserisci il sito collegato alle credenziali:  es google.com: ")
 


def crea_dizionario(email_inserita: str, password_generata: str,sito_collegato:str) -> dict:
    

   
    dizionario = {
        "password": password_generata,
        "email": email_inserita,
        "sito": sito_collegato
    }
    return dizionario


dati_dict = crea_dizionario(email_inserita, password_generata,sito_collegato)


os.system('clear')

print("Password email e sito associati:")

for chiave, valore in dati_dict.items():
    print(f"{chiave}-->{valore}")


