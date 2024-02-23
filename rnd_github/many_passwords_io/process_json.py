import json

def extract_values(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    usernames = [entry.get("Username") for entry in data]
    passwords = [entry.get("Password") for entry in data]
    unique_usernames = list(set(usernames))
    unique_passwords = list(set(passwords))

    with open("usernames.txt", 'w') as username_file:
        for username in unique_usernames:
            username_file.write(username + '\n')

    with open("passwords.txt", 'w') as password_file:
        for password in unique_passwords:
            password_file.write(password + '\n')

    print("Extraction complete. Check usernames.txt and passwords.txt files.")


if __name__ == '__main__':
    json_file = "passwords.json"
    extract_values(json_file)