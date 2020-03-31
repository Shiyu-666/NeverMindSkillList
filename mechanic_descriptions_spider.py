from requests import get

from bs4 import BeautifulSoup

mechanic_url = 'https://www.mythicmobs.net/manual/doku.php/skills/mechanics/'
mechanic_soup = BeautifulSoup(get(mechanic_url + 'start').text, 'lxml')
mechanic_trs = mechanic_soup.find('div', {'class': 'table sectionedit3'}).find_all('tr')[1:]\
               + mechanic_soup.find('div', {'class': 'table sectionedit6'}).find_all('tr')[1:]

mechanic_descriptions = dict()
for mechanic_tr in mechanic_trs:
    if mechanic_tr.a.attrs['class'][0] == 'wikilink2':
        continue
    mechanic = mechanic_tr.a.text.replace(' ', '')
    description = mechanic_tr.find_all('td')[1].text.strip().replace("'", '').replace("“", '"').replace("”", '"')
    mechanic_descriptions[mechanic] = description

with open('mechanic_descriptions.py', 'w', encoding='utf-8') as txt:
    letter = 'a'
    count = 0
    txt.write("mechanic_descriptions = {\n    'a': (\n")
    for key in sorted(mechanic_descriptions):
        temp = key.lower()[0]
        if temp != letter:
            txt.write("    ),\n    '%s': (\n" % temp)
            letter = temp
        count += 1
        txt.write("        ('%s', '%s'),\n" % (key, mechanic_descriptions[key]))
    txt.write('    ),\n}\n')
