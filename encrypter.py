from cryptography.fernet import Fernet

# Gera chave de criptografia
key = Fernet.generate_key()
cipher = Fernet(key)

# Salva a chave localmente (ambiente educacional)
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Abre o arquivo original
with open("arquivo.txt", "rb") as file:
    data = file.read()

# Criptografa o conteúdo
encrypted_data = cipher.encrypt(data)

# Salva o arquivo criptografado
with open("arquivo.txt.enc", "wb") as file:
    file.write(encrypted_data)

print("✔ Arquivo criptografado com sucesso!")
print("🔑 Chave salva em secret.key")
