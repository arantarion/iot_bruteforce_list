import itertools  

with open("unique_passwords.txt", "r") as f:
    passwords = f.readlines()

passwords = [password.replace("\n", "") for password in passwords]
passwords.append("")


with open("unique_usernames.txt", "r") as f:
    usernames = f.readlines()

usernames = [un.replace("\n", "") for un in usernames]
usernames.append("")

permuatations = list(itertools.product(usernames, passwords))
#d = list(itertools.product(passwords, usernames))

#all_permutations = c + d 

out_list = []
for item in permuatations:
    tmp = f"{item[0]} ; {item[1]}"
    out_list.append(tmp)

with open("output_pairs.txt", "w") as file:
    for item in out_list:
        file.write(item + "\n")