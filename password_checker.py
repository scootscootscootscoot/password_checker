import re

def check_password_strength(password):
    # Define criteria
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    common_passwords = ['password', '123456', 'qwerty', 'letmein']

    # Initialize feedback
    feedback = []

    # Check length
    if len(password) < min_length:
        feedback.append(f"Password must be at least {min_length} characters long.")
    
    # Check character types
    if not has_upper:
        feedback.append("Password must contain at least one uppercase letter.")
    if not has_lower:
        feedback.append("Password must contain at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password must contain at least one digit.")
    if not has_special:
        feedback.append("Password must contain at least one special character (e.g., !@#$%^&*).")

    # Check for common passwords
    if password.lower() in common_passwords:
        feedback.append("Password is too common and easily guessable.")

    # Determine strength
    if not feedback:  # No issues found
        return "Strong password!", feedback
    elif len(feedback) <= 2:  # Minor issues
        return "Moderate password.", feedback
    else:  # Major issues
        return "Weak password.", feedback

def main():
    print("Password Strength Checker")
    print("Enter a password to test (or 'quit' to exit):")
    
    while True:
        password = input("> ")
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        strength, issues = check_password_strength(password)
        print(f"Result: {strength}")
        if issues:
            print("Issues found:")
            for issue in issues:
                print(f"- {issue}")
        print()

if __name__ == "__main__":
    main()
