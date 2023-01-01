import os
from transliterate import translit


path = os.path.join(os.getcwd(), "scripts")
for old_name in os.listdir(path):
    full_old_name = os.path.join(path, old_name)
    full_new_name = os.path.join(path, translit(old_name, 'ru', reversed=True).replace(" ", "_").lower())
    os.rename(full_old_name, full_new_name)
print(1)