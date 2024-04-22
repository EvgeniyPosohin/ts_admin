import re
from data.DATA import Data


class Users(Data):
    """Подкласс для заполнения шаблона User"""
    def __init__(self):
        Data.__init__(self)
        self.password = 123456
        self.pattern = ["[\w\.-]+@[\w\.-]+", "[а-яёА-ЯЁ]+"]
        self.reader = []
        self.users = []

    def get_roles(self) -> list:
        """вытаскиваем из json список roles"""
        info = self.decoding()
        roles = info['roles']
        return roles

    def get_user_pattern(self) -> dict:
        """вытаскиваем из json шаблон user"""
        info = self.decoding()
        model = info['User']
        return model

    def get_tenant_id(self) -> dict:
        """вытаскиваем из json шаблон tenant"""
        info = self.decoding()
        tenant_ids = info['tenant_ids']
        return tenant_ids

    def mapping(self) -> list:
        """собираем users из патерна
         и возвращяем список"""
        list_users = []
        for data in self.reader:
            model = self.get_model(data)
            list_users.append(model)
        return list_users

    def get_model(self, data: list)-> dict:
        """собираем model для создания списка"""
        model = self.get_user_pattern()
        roles = self.get_roles()
        tenant_ids = self.get_tenant_id()
        mail = re.findall(self.pattern[0], data)
        fio = re.findall(self.pattern[1], data)
        model['email'] = mail[0]
        model['fname'] = fio[1]
        model['lname'] = fio[0]
        model['password'] = self.password
        model['roles'] = roles[0]
        model['tenant_ids'] = tenant_ids["OBLAKO Group"]
        return model

    def change(self):
        print("Вставьте пользователей:\n")
        self.reader = '\n'.join(iter(input, '')).split('\n')
        return self.reader

    def edit_user(self):
        pass