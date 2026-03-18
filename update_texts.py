
import os
import re

# Function to update texts
def update_texts(content):
    content = content.replace('>Data Centers<', '>Centros de Datos<')
    content = content.replace('>Login Portal<', '>Portal de Acceso<')
    content = content.replace('>Industrias<', '>Sectores<')
    content = content.replace('>Nosotros<', '>Quienes Somos<')
    return content

# Traverse the HTML files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = update_texts(content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Texts updated in {filename}")

print("Process completed.")
