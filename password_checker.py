import string



class PasswordChecker:
    """This class will check the stength, checking the passwords
    length, character diversity, and ensuring it's uniqueness """
    
    def __init__ (self, password):
        self.password = password
        self.errors = []
        
    def validate_length(self):
        
        if len(self.password) < 6 or len(self.password) > 20:
            self.errors.append("Password must be between 6 and 20 characters.")
            return False
        
        else:
           return True
       
    def validate_characters(self):
        
        """This method will check all the character conditions for the password.
        If all conditions are m et password will be returned as True
        If conditions are not met password will be returnned as false and errors will be displayed for user
        """
        has_uppercase = False
        has_lowercase = False
        has_number = False
        has_special_character = False
        
        for char in self.password:
            if char.islower():
                has_lowercase = True
            
            if char.isupper():
                has_uppercase = True
            if char.isnumeric():
                has_number = True
            if char in string.punctuation:
                has_special_character = True
        
        all_conditions_met = True
        
        if not has_uppercase:
            self.errors.append("Password must contain at least one uppercase character")
            all_conditions_met = False
            
        if not has_lowercase:
            self.errors.append("Password must contain at least one lowercase letter character")
            all_conditions_met = False
            
        if not has_number:
            self.errors.append("Password must contain at least one numeric character")
            all_conditions_met = False
            
        if not has_special_character:
            self.errors.append("Password must contain at least one special character")
            all_conditions_met = False
            
        return all_conditions_met
        
    def compare_against_common_passwords(self):
        """Checks if the password is among commonly used ones from a text file"""
        try:
            with open('common_passwords.txt', 'r', encoding='latin-1') as file:
             common_passwords_list = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            self.errors.append("Could not find the file: common_passwords.txt")
            return False

        if self.password in common_passwords_list:
            self.errors.append("This password is too common")
            return False
        return True

        
        
        
    def all_requirements_met (self):
        
        """_summary_
        """
        
        method_one_result = self.validate_length()
        method_two_result = self.validate_characters()
        method_three_result = self.compare_against_common_passwords()
        
        
        
        if all ([method_one_result, method_two_result, method_three_result]) :
           
            print("Your password passes all requirements!")
            return True
        else:
            print(f"Your password is not approved. Issues include : \n")
            for i in self.errors:
                print(f"* - {i}")
            return False
        
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Parse password combination")
    parser.add_argument("-p","--password", type=str, required= True, help="Validating password")
    args = parser.parse_args()
    
    check = PasswordChecker(args.password)
    result = check.all_requirements_met()
    
    if result:
        exit(0)
    else:
        exit(1)
        
        
if __name__ == "__main__":
    main()