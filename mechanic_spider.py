from requests import get
from bs4 import BeautifulSoup


soup = BeautifulSoup(get('https://www.mythicmobs.net/manual/doku.php/skills/mechanics/start').text, 'lxml')
trs = soup.find('div', {'class': 'table sectionedit3'}).find_all('tr')[1:] \
    + soup.find('div', {'class': 'table sectionedit6'}).find_all('tr')[1:]

string_front = "class %s(Mechanic):\n    def __init__(self):\n        Mechanic.__init__(self)\n        self.attrs = ["
attr = "\n            [('%s', '%s', '%s'), '%s'],"
string_back = "\n        ]\n        self.desc = '%s'\n        self.comment = ''\n        self.kind = 'mechanic'\n\n\n"

with open('mechanics_sub.py', 'w', encoding='utf-8') as py:
    py.write('from mechanics import Mechanic\n\n\n')

for tr in trs:
    if 'wikilink2' in tr.a.attrs['class']:  # 检测并跳过未完成技能.
        continue

    soup = BeautifulSoup(get('https://www.mythicmobs.net' + tr.a.attrs['href']).text, 'lxml')

    name = tr.a.text.replace(' ', '')

    temp = soup.find('p', {'style': ''})
    raw_desc = temp.find_next('p', {'style': ''}).text if temp.em else temp.text  # 避免选中版本信息而非技能描述.
    desc = ' '.join([string for string in raw_desc.split('\n') if string]).replace("'", '’')

    raw_form = soup.find('table', {'class': 'inline'})
    if not raw_form:  # 检测并跳过无参数技能.
        continue
    elif 'Attribute' not in raw_form.text:  # 避免选中更新信息表而非参数表.
        raw_form = raw_form.find_next('table', {'class': 'inline'})

    all_infos = []
    for row in raw_form.find_all('tr')[1:]:
        infos = []
        cols = row.find_all('td')
        for col in cols:
            # 避免参数信息包含注释文字.
            infos.append([item for item in col.contents if isinstance(item, str)][-1].strip() if col.contents else '')
        if len(cols) == 4:  # 删除缩写信息.
            del infos[1]
        all_infos.append(infos)

    with open('mechanics_sub.py', 'a', encoding='utf-8') as py:
        py.write(string_front % name)
        [py.write(attr % (infos[0], infos[1], infos[2], infos[2])) for infos in all_infos]
        py.write(string_back % desc)

    print(name)
