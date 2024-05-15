import hashlib
from itertools import product
import string
import time

def read_user_hashes(filename):
    
    try:
        user_hashes = {}
        
        with open(filename, 'r') as file:
            
            for line in file:
                
                if ',' in line:
                    user, hash_value = line.strip().split(',')
                    user_hashes[hash_value] = user
                    
                else:
                    
                    print("Formato incorreto, o esperado é 'username,hash'")
                    
        print(f"Lendo {len(user_hashes)} hashes de usuários")
        
        return user_hashes
    
    except FileNotFoundError:
        
        print(f"File not found :( {filename}")
        return {}

def brute_force_sha256(user_hashes, max_length=5):
    
    if not user_hashes:
        
        print("Não há hashes de usuários para quebrar!")
        return {}
        
    characters = string.ascii_lowercase + string.digits
    found_passwords = {}
    start_time = time.time()

    for length in range(1, max_length + 1):
        
        for attempt in product(characters, repeat=length):
            
            password = ''.join(attempt)
            hashed_attempt = hashlib.sha256(password.encode()).hexdigest()
            
            if hashed_attempt in user_hashes:
                
                elapsed_time = time.time() - start_time
                username = user_hashes[hashed_attempt]
                found_passwords[username] = (password, elapsed_time)
                
                print(f"Senha para {username} encontrado: {password} -> {hashed_attempt} em {elapsed_time:.2f} segundos..")
                
                del user_hashes[hashed_attempt]
                
                if not user_hashes:
                    return found_passwords
                
    print("Senhas não quebradas")
    
    return found_passwords

user_hashes = read_user_hashes('usuarios.txt')

if user_hashes:
    results = brute_force_sha256(user_hashes, max_length=4)
else:
    print("Não há dados válidos para processar")
