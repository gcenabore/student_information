    #Initialize an empty array to store entries (name, age)
    #define validation functions (valid name, valid age)
    #ask the user to input name and age
    #if the input is valid, store it in the array, otherwise show an error message
    #after each valid entries, ask if the user wants to add another entry
    #continue the loop until the user says "No"
    #when finished, find and display the oldest person in the entry

def main():
    entries = []

def is_name_valid(name: str) -> bool:
    return name.isalpha()

def is_age_valid(age: str) -> bool:
    return age.isdigit() and 0 <= int(age) <= 122

def get_oldest_person(entries: list) -> tuple:
    oldest = max(entries, key=lambda entry: entry[1])
    return oldest

