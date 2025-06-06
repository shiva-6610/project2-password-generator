import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not (use_upper or use_lower or use_digits or use_special):
        return "Error: At least one character type must be selected."

    # Character pools
    upper = string.ascii_uppercase if use_upper else ''
    lower = string.ascii_lowercase if use_lower else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_chars = upper + lower + digits + special

    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_lower:
        password.append(random.choice(lower))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True))
