from cryptography.fernet import Fernet

# =========================
# CONTEÚDO ORIGINAL
# =========================
original_text = """Este é um arquivo de teste.
Conteúdo sensível simulado para fins educacionais.
Projeto de criptografia em Python."""

# =========================
# 1. GERAR CHAVE
# =========================
key = Fernet.generate_key()
cipher = Fernet(key)

with open("secret.key", "wb") as key_file:
    key_file.write(key)

# =========================
# 2. CRIAR ARQUIVO ORIGINAL
# =========================
with open("arquivo.txt", "w", encoding="utf-8") as file:
    file.write(original_text)

# =========================
# 3. CRIPTOGRAFAR
# =========================
encrypted_data = cipher.encrypt(original_text.encode())

with open("arquivo.txt.enc", "wb") as file:
    file.write(encrypted_data)

# =========================
# 4. DESCRIPTOGRAFAR (TESTE)
# =========================
decrypted_data = cipher.decrypt(encrypted_data)

with open("arquivo_restaurado.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_data.decode())

print("✔ Laboratório gerado com sucesso!")
print("📁 Arquivos criados:")
print("- arquivo.txt")
print("- arquivo.txt.enc")
print("- arquivo_restaurado.txt")
print("- secret.key")
