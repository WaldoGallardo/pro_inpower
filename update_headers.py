import os
import re

# Get the header from the main file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    header_match = re.search(r'<header.*?</header>', content, re.DOTALL)
    if header_match:
        header = header_match.group(0)
    else:
        print("Header not found in main file.")
        exit()

# Traverse the HTML files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'index.html':
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the header
        new_content = re.sub(r'<header.*?</header>', header, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Header updated in {filename}")

print("Process completed.")
