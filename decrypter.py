from cryptography.fernet import Fernet

# Carrega a chave de criptografia
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Abre o arquivo criptografado
with open("arquivo.txt.enc", "rb") as file:
    encrypted_data = file.read()

# Descriptografa o conteúdo
decrypted_data = cipher.decrypt(encrypted_data)

# Salva o arquivo restaurado
with open("arquivo_restaurado.txt", "wb") as file:
    file.write(decrypted_data)

print("✔ Arquivo descriptografado com sucesso!")
print("📄 Gerado: arquivo_restaurado.txt")
