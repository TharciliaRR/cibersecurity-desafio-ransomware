# 🔐 Secure File Encryption Lab (Cybersecurity Portfolio Project)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Security](https://img.shields.io/badge/Cybersecurity-Learning-red.svg)
![Cryptography](https://img.shields.io/badge/Encryption-Symmetric-green.svg)
![Status](https://img.shields.io/badge/Status-Educational-lightgrey.svg)

---

## 📌 Executive Summary

This project simulates a **secure file encryption and decryption workflow** using Python, with the goal of demonstrating foundational concepts in **applied cryptography and defensive cybersecurity practices**.

Rather than focusing on malicious behavior, the project emphasizes:
- Data protection principles
- Secure key handling concepts
- Real-world encryption workflows used in security engineering

It is designed as a **portfolio-level cybersecurity lab**, aligned with entry-level SOC and security analyst skill development.

---

## 🎯 Security Objectives

- Demonstrate symmetric encryption in a controlled environment  
- Understand secure data lifecycle (encrypt → store → decrypt)  
- Practice secure file manipulation in Python  
- Reinforce ethical cybersecurity development principles  
- Simulate real-world defensive security scenarios  

---

## 🧠 Technical Concept

This project uses **symmetric encryption (Fernet - AES-based implementation)**.

### 🔄 Workflow Overview

```
[ Plain File ]
      ↓
[ Encryption (Fernet Key) ]
      ↓
[ Encrypted File (.enc) ]
      ↓
[ Secure Key Storage ]
      ↓
[ Decryption Process ]
      ↓
[ Restored Original File ]
```

---

## 🛠️ Technologies Used

- Python 3.x  
- :contentReference[oaicite:0]{index=0}  
- Fernet (symmetric encryption layer over AES)  
- Local file system simulation  

---

## 📁 Project Structure

```
📦 secure-file-encryption-lab
 ┣ 📜 encrypter.py        # File encryption script
 ┣ 📜 decrypter.py        # File decryption script
 ┣ 📜 arquivo.txt         # Sample input file
 ┣ 📜 arquivo.txt.enc    # Encrypted output file
 ┣ 📜 secret.key         # Encryption key (lab environment only)
 ┗ 📜 README.md
```

---

## 🔒 How It Works (Technical Breakdown)

### 1. Key Generation
A symmetric encryption key is generated using Fernet and stored locally.

### 2. Encryption Process
- File is read in binary mode  
- Content is encrypted using the generated key  
- Encrypted output is saved as `.enc`

### 3. Decryption Process
- Key is loaded from secure file  
- Encrypted file is decrypted  
- Original content is restored  

---

## ⚙️ Installation & Execution

### Install dependency
```bash
pip install cryptography
```

### Run encryption
```bash
python encrypter.py
```

### Run decryption
```bash
python decrypter.py
```

---

## 🛡️ Security Considerations (Important)

This project is intentionally simplified for educational purposes:

- ❗ Key storage is local only (not production-safe)
- ❗ No secure key management system (KMS) implemented
- ❗ No network transmission involved
- ❗ No persistence or malicious behavior

In real-world systems, secure implementations would include:
- Hardware Security Modules (HSM)
- Cloud Key Management Services (AWS KMS, Azure Key Vault)
- Role-based access control (RBAC)
- Audit logging

---

## 📊 Threat Modeling Perspective (SOC Mindset)

From a defensive security standpoint, this type of encryption system helps mitigate:

- Data exfiltration risks  
- Unauthorized file access  
- Insider threats  
- Endpoint compromise impact  

---

## 🧭 Learning Outcomes

This project demonstrates practical understanding of:

- Symmetric cryptography fundamentals  
- Secure coding principles in Python  
- File system security concepts  
- Cybersecurity ethics and responsible disclosure mindset  
- Defensive security thinking (SOC-oriented perspective)  

---

## 🧠 Professional Context

This project is aligned with skills expected in:

- SOC Analyst (Tier 1)  
- Cybersecurity Analyst (Junior)  
- Blue Team Security Roles  
- GRC / Security Awareness Roles  

---

## 👨‍💻 Author

**Tharcilia Rollemberg**  
Cybersecurity Student | SOC & Defensive Security Focus  

- GitHub: https://github.com/TharciliaRR 
- LinkedIn: https://linkedin.com/in/tharciliarollemberg 

---

## 🚀 Final Statement

This project represents a step toward building a solid foundation in cybersecurity engineering, focusing on **defensive security, cryptography, and ethical development practices**.

It reflects not only technical execution but also **security awareness, risk understanding, and professional documentation skills** — essential traits for modern cybersecurity roles.

---
