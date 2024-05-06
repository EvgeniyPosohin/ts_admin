import requests
import re
import json
import config
from Users import Users
import pprint as pp
from data.DATA import Data


class Admin(Data):
    def __init__(self, data: dict):
        super().__init__()
        self.__data = data
        self.__token = None
        self.admin_id = None
        self.org_id = None
        self.org_name = None
        self.login = None

    def get_login(self, value):
        """вытаскиваем из json список roles"""
        info = self.decoding()
        self.login = info['login'][value]

    def get_token(self) -> str:
        """получаем токен"""
        link_url = self.__data['url'] + '/login'
        params = {"username": self.__data[self.login],
                  "password": self.__data["password"]}
        response = requests.get(link_url, params=params)
        self.__token = response.json()["access_token"]
        return self.__token

    def get_headers(self):
        return {'accept': 'application/json',
                'x-authorization': self.__token}

    def get_admin_id(self) -> int:
        """получаем ИД учетки"""
        link_url = self.__data['url'] + '/users/me'
        headers = self.get_headers()
        response = requests.get(link_url, headers=headers)
        self.admin_id = response.json()["id"]
        self.org_id = response.json()["organization_id"]
        # print(f'{self.admin_id}, {self.org_id}')
        return response.status_code

    def get_user_info(self, email: str) -> str:
        """забираем id пользователя"""
        headers = self.get_headers()
        link_url = self.__data['url'] + '/users'
        params = {"email": email}
        response = requests.get(link_url, headers=headers, params=params)
        return response.json()[0]["id"]

    def set_user_data(self, id: str, data: dict):
        """меняем данные User, если он уже заведен"""
        headers = self.get_headers()
        link_url = self.__data['url'] + f'/users/{id}'
        response = requests.put(link_url, headers=headers, data=data)
        print(response.text)

    def generic_user(self, users: list):
        for i in range(len(users)):
            yield users[i]
    def create_users(self, users: list):
        """Добавляем пользователя"""
        print(users)
        print(type(users))
        link_url = self.__data['url'] + '/users'
        headers = self.get_headers()
        response = requests.post(link_url, headers=headers, data=users)
        return response.status_code


            # if response.json()["message"]["error"] == "Email already exists; ":
            #     id = self.get_user_info(data["email"])
            #     self.set_user_data(id, data)

    def import_users(self, users: list):
        """Импортируем сразу несколько пользователей
        для админа орг - НЕ СДЕЛАНО"""
        data = {"data": users}
        link_url = self.__data['url'] + '/users/import'
        headers = self.get_headers()
        response = requests.post(link_url, headers=headers, data=data)
        pp.pprint(response.json())


# if __name__ == "__main__":
#     admin = Admin(config.data)
#     print(admin.get_token())
#     print(admin.get_admin_id())
#     user = Users()
#     # user.change()
#     pp.pprint(user.mapping())
#     admin.import_users(user.mapping())
#     print(admin.create_users(user.mapping()))
#     # # print(admin.create_users(user.info))





