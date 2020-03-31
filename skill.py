from os import system
from mechanics import *
from effect_descriptions import effect_descs
from mechanic_descriptions import mechanic_descs


def is_float(num):
    return True if num.count('.') <= 1 and num.replace('.', '').isdigit() else False


class SkillList:

    def __init__(self):
        self.conditions = []
        self.skills = []
        self.target_conditions = []

    @staticmethod
    def show_skill_attributes(skill):
        print(f'\n  正在编辑技能 {skill.__class__.__name__}{f" - {skill.comment}" if skill.comment else ""}\
                \n  当前技能参数列表如下: ')
        for i in range(len(skill.attrs)):
            attr = skill.attrs[i]
            print(f'  {i}. {attr[0][0]}: {attr[1]}' + (f' - {attr[0][2]}' if attr[0][2] else ''))

    @staticmethod
    def show_descriptions(descs):
        print('\n  可选技能列表如下: ')
        for i in range(len(descs)):
            print(f'  {i}. {descs[i][0]} - {descs[i][1]}')

    def show_skills(self):
        print('\n  当前技能组结构如下: ')
        for i in range(len(self.skills)):
            skill = self.skills[i]
            print(f'  {i}. {skill.__class__.__name__}' + (f' - {skill.comment}' if skill.comment else ''))

    def main(self):
        while True:
            system('cls')
            print('\n  NeverMindSkillList v1.0\n  Author: Zyyans')
            func = input('\n  1. 添加技能\n  2. 删除技能\n  3. 编辑技能参数\
                          \n  请选择您需要的功能.\n  输入 back 以返回上一步.\n  >> ')
            while True:
                if func in ['2', '3'] and not self.skills:
                    func = input('  技能列表为空, 请选择其他功能.\n  >> ')
                elif func not in ['1', '2', '3', 'back']:
                    func = input('  输入无效, 请重新输入.\n  >> ')
                else:
                    break

            if func == '1':
                self.skill_add()
            elif func == '2':
                self.skill_remove()
            elif func == '3':
                self.skill_edit()
            elif func.lower() == 'back':
                return

    def skill_add(self):
        while True:
            system('cls')
            kind = input(
                '\n  1. 方法类(默认)\n  2. 特效类\n  请选择您想要添加的技能的类型.\n  输入 back 以返回上一步.\n  >> ')
            while kind.lower() not in ['', '1', '2', 'back']:
                kind = input('  输入无效, 请重新输入.\n  >> ')

            if (kind in ['', '1'] and self.skill_add_mechanic()) or (
                    kind == '2' and self.skill_add_effect()) or (
                    kind == 'back'):
                return

    def skill_add_mechanic(self):
        while True:
            system('cls')
            key = input('\n  请输入您想要添加的技能的名称首字母.\n  输入 back 以返回上一步.\n  >> ').lower()
            while True:
                if key == 'back':
                    return False
                elif len(key) != 1 or ord(key) not in range(97, 123):
                    key = input('  输入无效, 请重新输入.\n  >> ').lower()
                elif key not in mechanic_descs.keys():
                    key = input('  没有以该字母为名称首字母的技能, 请重新输入.\n  >> ').lower()
                else:
                    break

            if self.skill_add_mechanic_(key):
                return True

    def skill_add_mechanic_(self, key):
        system("cls")
        descs = mechanic_descs[key]
        self.show_descriptions(descs)
        num = input('\n  请输入您想要添加的技能的序号.\n  输入 back 以返回上一步.\n  >> ')
        while True:
            if num.lower() == 'back':
                return False
            elif not num.isdigit() or int(num) not in range(len(descs)):
                num = input('  输入无效, 请重新输入.\n  >> ')
            else:
                break

        name = descs[int(num)][0]
        skill = eval(f'{name}()')
        skill.comment = input(
            f'\n  技能 {name} 已添加.\n  若需要添加说明文字, 请在下方输入.\n  若不需要, 请直接按下回车键.\n  >> ')
        self.skills.append(skill)
        return True

    def skill_add_effect(self):
        system('cls')
        self.show_descriptions(effect_descs)
        num = input('\n  请输入您想要添加的技能的序号.\n  输入 back 以返回上一步.\n  >> ')
        while True:
            if num.lower() == 'back':
                return False
            elif not num.isdigit() or int(num) not in range(len(effect_descs)):
                num = input('  输入无效, 请重新输入.\n  >> ')
            else:
                break

        name = effect_descs[int(num)][0]
        skill = eval(f'{name}()')
        skill.comment = input(
            f'\n  技能 {name} 已添加.\n  若需要添加说明文字, 请在下方输入.\n  若不需要, 请直接按下回车键.\n  >> ')
        self.skills.append(skill)
        return True

    def skill_remove(self):
        system('cls')
        self.show_skills()
        num = input('\n  请输入您想要删除的技能的序号.\n  输入 back 以返回上一步.\n  >> ')
        while True:
            if num.lower() == 'back':
                return False
            elif not num.isdigit() or int(num) not in range(len(self.skills)):
                num = input('  输入无效, 请重新输入.\n  >> ')
            else:
                break

        name = self.skills[int(num)].__class__.__name__
        del self.skills[int(num)]
        input(f'\n  技能 {name} 已删除.\n  按回车键以继续.')
        return True

    def skill_edit(self):
        while True:
            system('cls')
            self.show_skills()
            num = input('\n  请输入您想要编辑的技能的序号.\n  直接按下回车键以按顺序编辑所有技能的参数.\
                         \n  输入 back 以返回上一步.\n  >> ')
            while True:
                if not num:
                    for skill in self.skills:
                        print('asdasdasdasdasd')
                        if not self.skill_edit_(skill):
                            break
                    break
                elif num.lower() == 'back':
                    return False
                elif not num.isdigit() or int(num) not in range(len(self.skills)):
                    num = input('  输入无效, 请重新输入.\n  >> ')
                else:
                    self.skill_edit_(self.skills[int(num)])
                    break

    def skill_edit_(self, skill):
        while True:
            system('cls')
            self.show_skill_attributes(skill)
            mode = input(
                '\n  1. 按顺序编辑全部参数(默认)\n  2. 选择参数进行编辑\
                 \n  请选择您想要的编辑模式.\n  输入 back 以返回上一步.\n  >> ')
            while mode.lower() not in ['', '1', '2', 'back']:
                mode = input('  输入无效, 请重新输入.\n  >> ')

            if mode in ['', '1'] and self.skill_edit_all(skill):
                return
            elif mode == '2' and not self.skill_edit_one(skill):
                return
            else:
                return False

    def skill_edit_all(self, skill):
        for i in range(len(skill.attrs)):
            system('cls')
            val = self.skill_edit_attribute(skill.attrs[i][0])
            if val == 'pass':
                continue
            elif not val:
                return False
            else:
                skill.attrs[i][1] = val
        return True

    def skill_edit_one(self, skill):
        while True:
            system('cls')
            self.show_skill_attributes(skill)
            i = input('\n  请输入您想要编辑的参数的编号.\n  输入 back 以返回上一步.\n  >> ')
            while True:
                if i.lower() == 'back':
                    return True
                elif not i.isdigit() or int(i) not in range(len(skill.attrs)):
                    i = input('  输入无效, 请重新输入.\n  >> ')
                else:
                    break

            system('cls')
            val = self.skill_edit_attribute(skill.attrs[int(i)][0])
            if val and val != 'pass':
                skill.attrs[int(i)][1] = val
                continue

    @staticmethod
    def skill_edit_attribute(desc):
        limit_key = desc[4]
        limit = {'int': '整数', 'str': '字符串', 'float': '数字', 'bool': 'True 或 False(无视大小写)'}[desc[4]]
        print(f'\n  当前参数: {desc[0]}\n  参数描述: {desc[2]}\n  默认值: {desc[3]}\n  参数限制:{limit}')
        val = input('\n  请输入您想要的参数值.\n  直接按下回车以跳过.\n  输入 back 以返回上一步.\n  >> ')
        while True:
            if not val:
                return 'pass'
            elif val == 'back':
                return False
            elif limit_key == 'int' and not val.isdigit():
                val = input('  输入无效, 请重新输入.\n  >> ')
            elif limit_key == 'float' and not is_float(val):
                val = input('  输入无效, 请重新输入.\n  >> ')
            elif limit_key == 'bool' and val.lower() not in ['true', 'false']:
                val = input('  输入无效, 请重新输入.\n  >> ')
            else:
                return val


asd = SkillList()
while True:
    asd.main()
