import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

base_url = "https://router-network.com"  
url = "https://router-network.com/brands"  
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

btn_classes = soup.find_all(class_="btn btn-outline-info")

links = []
for btn_class in btn_classes:
    links.append(btn_class['href'])


with open("links.txt", "w") as file:
    for item in links:
        file.write(base_url + item + "\n")
                   

ips = []
usernames = []
passwords = []

for link in tqdm(links):

    curr_url = base_url + link
    resp = requests.get(curr_url)
    soup_obj = BeautifulSoup(resp.content, 'html.parser')
    dl_elements = soup_obj.find_all("dl", class_="row mb-0 pr-3 flex-nowrap")

    for dl in dl_elements:
        dt = dl.find("dt", class_="col-6 col-md-4 text-truncate mx-n2 mx-md-0")
        dd = dl.find("dd", class_="col mb-0 mx-n1 mx-md-0")
        if dt and dd:
            dt_text = dt.text.strip()
            dd_text = dd.text.strip()
            
            if "Username" in dt_text:
                usernames.append(dd_text)
            elif "Password" in dt_text:
                passwords.append(dd_text)
            elif "IP" in dt_text:
                ips.append(dd_text)
    
    time.sleep(1)

print('#'*80)
print("Statistics so far")
print(f"Number of usernames collected: {len(usernames)}")
print(f"Number of passwords collected: {len(passwords)}")
print(f"Number of IPs collected: {len(ips)}")
print('#'*80)

un_pw_pairs = []
for un, pw in zip(usernames, passwords):
    tmp = f"{un} ; {pw}"
    un_pw_pairs.append(tmp)

with open("output_pairs.txt", "w") as file:
    for item in un_pw_pairs:
        file.write(item + "\n")

usernames_unique = list(set(usernames))
passwords_unique = list(set(passwords))
ips_unique = list(set(ips))

print('#'*80)
print("Unique items")
print(f"Number of unique usernames collected: {len(usernames_unique)}")
print(f"Number of unique passwords collected: {len(passwords_unique)}")
print(f"Number of unique IPs collected: {len(ips_unique)}")
print('#'*80)

with open("unique_usernames.txt", "w") as file:
    for item in usernames_unique:
        file.write(item + "\n")

with open("unique_passwords.txt", "w") as file:
    for item in passwords_unique:
        file.write(item + "\n")

with open("ips_unique.txt", "w") as file:
    for item in ips_unique:
        file.write(item + "\n")