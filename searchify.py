import re

terms_list = [' Ma!ch!n3_Learn!ng ', 'Cry#pt0graphy@2020', 'Quantum_Computing', ' Deep_Learn!ng', 'Pyth%on_Coding', '  Space_Exploration  ', ' V1rtu@l_R3al1ty', '@Blockchain_Technology! ']

def search_urls(terms):
  for x in terms:
    print('https://www.google.com/search?q=' + re.sub(r"[^a-zA-Z0-9]+", ' ', x).strip().replace(" ", "+"))

search_urls(terms_list)
