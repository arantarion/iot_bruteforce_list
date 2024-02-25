import pandas as pd

df = pd.read_json('defpass_database.json')

df.to_csv("defpass_database.csv", sep=",")

def_login = list(set(list(df['Default password'])))

with open("defpass_default_login_credentials.txt", "w") as f:
    for line in def_login:
        f.write(str(line) + "\n")

