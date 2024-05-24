from email_validator import validate_email, EmailNotValidError
import random
import string
import requests
import re



def password_generata() -> str:
    """Genera una password casuale in base alla lunghezza inserita dall'utente.

    Args: Nessuno.
    Returns: Una password generata casualmente.
    """
    try:
        while True:
            length = int(input("Inserisci la lunghezza desiderata per la password: "))
            print("\n")
            if length < 8 or length > 20:
                print("La lunghezza deve essere almeno di 8 caratteri e al massimo di 20 caratteri.")
                print("\n")
                continue    

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
        print("\n")
        return password_generata()

password_generata = password_generata()
print(f"Password generata: {password_generata}")
print("\n")

def verifica_email() -> str:
    """Questa funzione convalida un indirizzo email fornito dall’utente.


    Args: nessuno.
    return: indirizzo email valido.
    """
    while True:
        try:
            indirizzo_email = input("Inserisci un indirizzo email: ")
            print("\n")
            validato = validate_email(indirizzo_email)
            print(f"L'indirizzo email '{indirizzo_email}' è valido.")
            print("\n")
            
            return indirizzo_email
        except EmailNotValidError as e:
            
            print("Inserisci un indirizzo email valido.")
            print("\n")
email_inserita = verifica_email()


def verifica_sito() -> str:
    """Verifica se un sito web inserito dall'utente esiste.

    Returns:
        str: Il sito web esistente o una stringa vuota se non esiste.
    """
    while True:
        sito_collegato = input("Inserisci il sito collegato alle credenziali (es. google.com): ")
        print("\n")

        if re.match(r"^[a-zA-Z0-9.-]+$", sito_collegato):
            try:
                response = requests.get(f"https://{sito_collegato}")
                if response.status_code == 200:
                    print(f"Il sito {sito_collegato} esiste!")
                    print("\n")
                    return sito_collegato
            except requests.ConnectionError:
                print("Dominio mancante o sito inesistente!")
                print("\n")
        else:
            print("Inserisci un sito valido (solo caratteri dell'alfabeto, punti e trattini).")
            print("\n")

sito_inserito = verifica_sito()



def crea_dizionario(email_inserita: str, password_generata: str,sito_inserito:str) -> dict:
    print("\n")
    """Questa funzione crea un dizionario contenente l’email dell’utente, la password e il sito web associato.

    Args: password,email,sito.
    return: Dizionario contenente le 3 chiavi.
    """
    sito_inserito = f"{sito_inserito} "+" (esistente)"
    dizionario = {
        "password": password_generata,
        "email": email_inserita,
        "sito": sito_inserito
    }
    return dizionario



dati_dict = crea_dizionario(email_inserita, password_generata,sito_inserito)
print("\n" * 80)


print(f"Password email e sito associati:")
print("\n")
for chiave, valore in dati_dict.items():
    if chiave == "password":
        print(f"\033[91m{chiave}-->\033[0m{valore}")
    elif chiave == "email":
        print(f"\033[93m{chiave}-->\033[0m{valore}")
    else:
        print(f"\033[94m{chiave}-->\033[0m{valore}")
    print("\n" )
