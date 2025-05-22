# Function

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet() 

# Function with parameters
def info(name, email, phone):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

info("Rajesh", "Vp4dM@example.com", "1234567890")

def life_in_weeks(age):
    left_week = age * 60
    print(f"i have {left_week} weeks left in my life")
    
life_in_weeks(60) 

# keyword arguments
def info(name, email, phone):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

info(name="Rajesh", email="Vp4dM@example.com", phone="1234567890")

# love calculater

def calculate_love_score(name1, name2):
    love_score = 0
    love_score += name1.lower().count("t")
    love_score += name1.lower().count("r")
    love_score += name1.lower().count("u")
    love_score += name1.lower().count("e")
    love_score += name1.lower().count("l")
    love_score += name1.lower().count("o")
    love_score += name1.lower().count("v")
    love_score += name1.lower().count("e")
    return love_score

print(calculate_love_score("Rajesh", "Mahesh"))


# ceaser cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-letters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift for decryption

# Example usage
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))

# Encrypt
encrypted = encrypt(message, shift_value)
print(f"Encrypted message: {encrypted}")

# Decrypt
decrypted = decrypt(encrypted, shift_value)
print(f"Decrypted message: {decrypted}")
