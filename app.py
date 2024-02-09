import random
import string
from faker import Faker

def generate_random_number(start, end):
    return random.randint(start, end)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_word_from_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = [word.strip() for word in file.readlines()]
    return random.choice(dictionary)

def generate_random_id_set(start, end, count):
    return set(random.sample(range(start, end + 1), count))

def generate_random_emails(count):
    def generate_random_email():
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail.com', 'yahoo.com', 'example.com'])
        return f'{username}@{domain}'

    return [generate_random_email() for _ in range(count)]

def generate_random_colombian_address():
    fake = Faker('es_CO')
    return fake.address()

if __name__ == "__main__":
    # Ejemplos de uso
    print("Número Aleatorio:", generate_random_number(1, 100))
    print("Cadena Aleatoria:", generate_random_string(8))
    #print("Palabra Aleatoria del Diccionario:", generate_random_word_from_dictionary('dictionary.txt'))
    print("Conjunto Aleatorio de IDs:", generate_random_id_set(1000, 2000, 5))
    print("Emails Aleatorios:", generate_random_emails(5))
    print("Dirección Colombiana Aleatoria:", generate_random_colombian_address())
