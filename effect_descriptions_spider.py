from requests import get

from bs4 import BeautifulSoup

effect_url = 'https://www.mythicmobs.net/manual/doku.php/skills/effects/'
effect_soup = BeautifulSoup(get(effect_url + 'start').text, 'lxml')
effect_trs = effect_soup.find('div', {'class': 'table sectionedit4'}).find_all('tr')[1:] + \
           effect_soup.find('div', {'class': 'table sectionedit6'}).find_all('tr')[1:]

effect_descriptions = dict()
for effect_tr in effect_trs:
    if effect_tr.a.attrs['class'][0] == 'wikilink2':
        continue
    effect = effect_tr.a.text.replace(' ', '')
    description = effect_tr.find_all('td')[1].text.strip().replace("'", '').replace("“", '"').replace("”", '"')
    effect_descriptions[effect] = description

with open('effect_descriptions.py', 'w', encoding='utf-8') as txt:
    count = 0
    txt.write('effect_descriptions = (\n')
    for key in sorted(effect_descriptions):
        count += 1
        txt.write(f"    ('{key}', '{effect_descriptions[key]}'),\n")
    txt.write(')\n')
