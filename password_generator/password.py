# Get password length from user (must be >= 8)
# Ask customization preferences (yes/no)
# Generate password based on user preferences
# Show strength indicator based on length + character variety

import secrets
import string

def main():

    print("\n✨ Welcome to the Secure Password Generator ✨\n")

   # Check if the length is valid (at least 8), otherwise ask again
    while True:
        try:
            len_of_password = int(input("Enter the Length for the password: "))
            if (len_of_password < 8):
                print("The length for the password *must* be more than 8 characters...")
            else:
                break
        except ValueError:
            print("Please enter a valid number...")

    # customization options for the password
    # yes_or_no function - to check if the value enter by user is valid or not
    use_upper = yes_or_no("Include uppercase letters? (y/n): ")
    use_lower = yes_or_no("Include lowercase letters? (y/n): ")
    use_digits = yes_or_no("Include digits? (y/n): ")
    use_special = yes_or_no("Include special characters? (y/n): ")

    # if user does not set any value to 'y'
    if not (use_upper or use_lower or use_digits or use_special):
        print("At least one character set must be selected. Defaulting to all.")
        use_upper = use_lower = use_digits = use_special = True
    
    # to generate the password
    password= generate_password(len_of_password,use_upper,use_lower,use_digits,use_special)
    print(f"\n🔑 Your generated password is:\n{password}")

    # checking for if the password is strong or not 
    print(checking_password_strength(len_of_password,use_upper,use_lower,use_digits,use_special))

    # Asking user if they want to generate another password
    again = yes_or_no("Do you want to generate another password? (y/n) ")
    if again:
        main()
    else:
        print("Thank you for using the password generator! 🔒")



def generate_password(length,upper,lower,digit,special):
    characters = []

    # adding characters based on the user preference
    if upper:
        characters.extend(string.ascii_uppercase)
    if lower:
        characters.extend(string.ascii_lowercase)
    if digit:
        characters.extend(string.digits)
    if special:
        characters.extend(string.punctuation)

    return ''.join(secrets.choice(characters) for _ in range(length))


# checking password strength
def checking_password_strength(length,upper,lower,digit,special):
    # counting how many value user set to "y"
    criteria_count = sum([upper,lower,digit,special])

    # based on that and length printing strength indicator
    if length >= 12 and criteria_count == 4:
        return "✅ The password is strong."
    elif length >= 10 and criteria_count >= 3:
        return "⚠️ The password is moderate."
    else:
        return "❌ The password is weak."


# to ensure the user only enter yes or no for customization process
def yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ["y","yes"]:
            return True
        elif answer in ["n","no","not"]:
            return False
        else:
            print("Please enter 'y' or 'n' (yes or no).")


if __name__ == "__main__":
    main()