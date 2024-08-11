import os
import re
 
folder_path = 'papers/'
output_file = 'output_links.txt'
 
matched_links = []
# pattern should be strings starting with `http` or `https`, and ending with `.pdf`
pattern = r'https?://[^\s]*\.pdf'

if __name__ == '__main__':
    # clear the output file
    if os.path.exists(output_file):
        os.remove(output_file) 
    with open("README.md", 'r', encoding='utf-8') as md_file:
        content = md_file.read()
        links = re.findall(pattern, content)
        matched_links.extend(links)
    with open(output_file, 'w', encoding='utf-8') as output:
        for link in matched_links:
            output.write(link + '\n')
    count = len(matched_links)
    print(f"Find {count} links in README.md")
    # download pdf files
    print(f"Downloading pdf files to {folder_path}")
    for link in matched_links:
        os.system(f"wget {link} -P {folder_path}")