    #Initialize an empty array to store entries (name, age)
    #define validation functions (valid name, valid age)
    #ask the user to input name and age
    #if the input is valid, store it in the array, otherwise show an error message
    #after each valid entries, ask if the user wants to add another entry
    #continue the loop until the user says "No"
    #when finished, find and display the oldest person in the entry


def main():
    entries = [] #List to store tuples of (name, age)
    
    #check if name contains only alphabetic characters
def is_name_valid(name: str) -> bool:
    return name.isalpha()

    #check if the inpput age is a digit and between 0 and 122
def is_age_valid(age: str) -> bool:
    return age.isdigit() and 0 <= int(age) <= 122

    #find the person with the maximum/older age
def get_oldest_person(entries: list) -> tuple:
    oldest = max(entries, key=lambda entry: entry[1])
    return oldest

#input and validate name
while True:
    name = input("Enter student name: ")
    if not is_name_valid(name):
        print("Invalid name. Please enter alphabetic characters only.")
        continue 