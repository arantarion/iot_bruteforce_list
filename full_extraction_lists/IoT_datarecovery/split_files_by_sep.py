import sys

def split_file(filename):
    usernames = set()
    passwords = set()
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if ';' in line and not "none" in line:
                username, password = line.split(';', 1)
                usernames.add(username)
                passwords.add(password)

    with open('username.txt', 'w') as username_file:
        for username in usernames:
            username_file.write(username + '\n')

    with open('password.txt', 'w') as password_file:
        for password in passwords:
            password_file.write(password + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <filename>')
    else:
        filename = sys.argv[1]
        split_file(filename)
        print('Splitting complete. Check username.txt and password.txt files.')