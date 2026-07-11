# ANSI Escape Sequences for Terminal Colors
CLR_RESET  = "\033[0m"
CLR_CYAN   = "\033[36m"
CLR_GREEN  = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_RED    = "\033[31m"
CLR_BLUE   = "\033[34m"
CLR_MAG    = "\033[35m"

def encrypt_caesar(plaintext, shift):
    """
    PROCESS LOGIC: Caesar Cipher Encryption Module
    Applies the mathematical shift: E_n(x) = (x + n) % 26
    """
    encrypted = ""
    for char in plaintext:
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Handle Edge Cases: Numbers, spaces, and symbols stay the same
            encrypted += char
    return encrypted

def decrypt_caesar(ciphertext, shift):
    """
    PROCESS LOGIC: Caesar Cipher Decryption Module
    Applies the reverse shift: D_n(x) = (x - n) % 26
    """
    decrypted = ""
    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted += char
    return decrypted

def print_header(title):
    print(f"\n{CLR_BLUE}=" * 60)
    print(f"{CLR_CYAN}  {title.upper()}")
    print(f"{CLR_BLUE}=" * 60 + CLR_RESET)

def main():
    # Application Title Banner
    print(f"\n{CLR_CYAN}┌──────────────────────────────────────────────────────────┐")
    print(f"│      {CLR_GREEN}DECODELABS CRYPTOGRAPHIC ENGINE : PROJECT 2{CLR_CYAN}         │")
    print(f"└──────────────────────────────────────────────────────────┘{CLR_RESET}")

    # 1. OPERATION MENU
    print(f"\n{CLR_YELLOW}[ STEP 1 : CONFIGURING THE RUNTIME MODE ]{CLR_RESET}")
    print(f"  {CLR_CYAN}1.{CLR_RESET} Symmetric Encryption Engine Mode")
    print(f"  {CLR_CYAN}2.{CLR_RESET} Reverse Decryption Engineering Mode")
    op_choice = input(f"\n{CLR_GREEN}➔ Select execution path (1-2): {CLR_RESET}").strip()

    if op_choice not in ['1', '2']:
        print(f"\n{CLR_RED}[✕ ERROR] Invalid operation selection. Exiting system.{CLR_RESET}\n")
        return

    # 2. KEYSPACE & DATA CAPTURE
    print(f"\n{CLR_YELLOW}[ STEP 2 : CAPTURING DATA AND CIPHER SHIFT ]{CLR_RESET}")
    
    if op_choice == "1":
        message = input(f"{CLR_CYAN}📝 Enter plaintext message payload: {CLR_RESET}")
        try:
            key = int(input(f"{CLR_CYAN}🔢 Enter shift parameter value (integer): {CLR_RESET}"))
        except ValueError:
            print(f"\n{CLR_RED}[✕ ERROR] Shift parameters must be whole integers.{CLR_RESET}\n")
            return
            
        # Run Encryption Logic
        encrypted_message = encrypt_caesar(message, key)
        
        # Display Styled Results
        print_header("Processing via Mathematical Protection Module")
        print(f" {CLR_BLUE}•{CLR_RESET} Input Text :  {CLR_RESET}{message}")
        print(f" {CLR_BLUE}•{CLR_RESET} Key Shift  :  {CLR_MAG}{key}")
        print(f" {CLR_GREEN}✔ Ciphertext:  {CLR_YELLOW}{encrypted_message}{CLR_RESET}\n")
        
    elif op_choice == "2":
        message = input(f"{CLR_CYAN}🔒 Enter obfuscated Caesar text to decode: {CLR_RESET}")
        try:
            key = int(input(f"{CLR_CYAN}🔢 Enter validation shift verification key: {CLR_RESET}"))
        except ValueError:
            print(f"\n{CLR_RED}[✕ ERROR] Shift parameters must be whole integers.{CLR_RESET}\n")
            return
            
        # Run Decryption Logic
        decrypted_message = decrypt_caesar(message, key)
        
        # Display Styled Results
        print_header("Processing via Mathematical Protection Module")
        print(f" {CLR_BLUE}•{CLR_RESET} Input Text :  {CLR_YELLOW}{message}")
        print(f" {CLR_BLUE}•{CLR_RESET} Key Shift  :  {CLR_MAG}{key}")
        print(f" {CLR_GREEN}✔ Plaintext :  {CLR_GREEN}{decrypted_message}{CLR_RESET}\n")

if __name__ == "__main__":
    main()