def split_file(filename):
    usernames = set()
    passwords = set()

    with open(filename, 'r') as file:
        for line in file:
            line = line.lstrip()
            try:
                username, password = line.split('  ', 1)
                usernames.add(username)
                passwords.add(password)
            except:
                print(line)

    with open('usernames.txt', 'w') as username_file:
        for username in usernames:
            username_file.write(username + '\n')

    with open('passwords.txt', 'w') as password_file:
        for password in passwords:
            password_file.write(password + '\n')

    print("Splitting complete. Check usernames.txt and passwords.txt files.")
    print(f"Wrote {len(usernames)} unique usernames")
    print(f"Wrote {len(passwords)} unqiue passwords")

if __name__ == '__main__':
    filename = "list-2019-01-29.txt"
    split_file(filename)
