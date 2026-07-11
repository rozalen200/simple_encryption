# Cryptographic Engine - Caesar Cipher

A lightweight, zero-dependency data confidentiality utility built for **DecodeLabs Project 2**[cite: 2]. This terminal application implements the core Input-Process-Output (IPO) cycle to mathematically secure and restore raw data payloads via symmetric logic.

## Features
* **Dual Runtime Modes:** Seamless configuration toggles for standard Encryption and reverse Decryption Engineering.
* **Preservation Engine:** Advanced edge-case handling routes spacing, symbols, and numeric values safely around the mathematical matrix to prevent file corruption.
* **Robust Input Guardrails:** Embedded exception-handling frameworks protect system keyspace values from type mismatches.
* **Premium CLI UI:** A customized, high-contrast command-line dashboard utilizing native ANSI terminal escape color-mapping sequences.

## Architecture & Math
The processing layer relies on modular arithmetic to accurately manipulate string bit patterns without structural data leakage:

* **Encryption Module:** 
  $$E_n(x) = (x + n) \pmod{26}$$
* **Decryption Module:** 
  $$D_n(x) = (x - n) \pmod{26}$$

## Requirements
* Python 3.x
* A standard terminal running an ANSI-supported shell layer (Linux Bash, macOS Terminal, or modern Windows PowerShell)

## Deployment Execution
To launch the protection interface panel, fire up your local terminal window and execute:

```bash
python3 chipher_chif.py
