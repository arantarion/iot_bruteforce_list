import re

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_and_split_data(html_content):
    pattern = r'Default password: (.*?)(?=<br>)'
    matches = re.findall(pattern, html_content, re.IGNORECASE | re.DOTALL)
    usernames = set()
    passwords = set()
    for match in matches:
        parts = match.split(':')
        if len(parts) == 2:
            usernames.add(parts[0].strip())
            passwords.add(parts[1].strip())

    return usernames, passwords

file_path = 'defpass_all_entries.htm'
html_content = read_html_file(file_path)

usernames, passwords = extract_and_split_data(html_content)

print("Usernames:", usernames)
print("Passwords:", passwords)