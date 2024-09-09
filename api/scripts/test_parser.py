from bs4 import BeautifulSoup

html_content = "<html><body><h1>Title</h1><p>This is a paragraph.</p></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting all paragraph texts
for p in soup.find_all('p'):
    print(p.text)