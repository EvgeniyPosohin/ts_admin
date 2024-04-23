import flet as ft
from data import support as sup

class TxtField(ft.TextField):
    """вспомогательный класс для создания одинаковых полей"""
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.border_color = "blue"
        self.border_radius = 15
        self.border_width = 2
        self.width = 400
        self.height = 35


class Chips(ft.Chip):
    """кдасс для объявления ролей"""
    def __init__(self, label, page: ft.Page):
        super().__init__(label)
        self.label = ft.Container(content=ft.Text(label),
                                  width=70, height=20)
        self.bgcolor = "grey"
        self.check_color = "black"
        self.selected = False
        self.padding = ft.padding.symmetric(5, 50)
        self.disabled_color = "grey"
        self.on_select = self.click
        self.selected_color = "#18a153"
        self.page = page
        self.width = 200

    def click(self, e):
        print(self.selected)
        self.page.update()


class UserInfo(ft.TextField):
    """для ввода фио и почты"""
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.border_color = "white"
        self.border_radius = 10
        self.border_width = 2
        # self.width = 400
        # self.height = 400
        self.multiline = True


class PaddingContainer(ft.Container):
    """создание блока для зонирования элементов"""
    def __init__(self, **kwargs):
        super().__init__()
        self.padding = ft.padding.only(**kwargs)


def main(page: ft.Page):
    # Настройка страницы
    page.title = "TS загрузка пользователей"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 40
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = "center"
    page.bgcolor = "#c0c2c4"

    # контейнер с названием страницы
    appTitle = ft.Row(
        controls=[
            ft.Text("TS Uploader", style=ft.TextStyle(color="black", size=26,
                                                      shadow=ft.BoxShadow(color="blue")),
                    ),
        ], alignment="center"
    )

    # пустые контейнеры для определения границ
    bord_left = PaddingContainer(left=20)
    bord_ctr = PaddingContainer(left=10)
    bord_top = ft.Container(padding=ft.padding.only(top=20))

    # Поля для ввода текста
    container_1 = ft.border.all(5, ft.colors.BLUE_100)
    org_id = TxtField("organization_id")
    add_org_id = TxtField("Доп.Организация")
    user_password = TxtField("Password")
    user_password.value = "123456"
    item_1 = ft.Column([ft.Container(content=org_id, border=container_1, border_radius=20),
                       ft.Container(content=add_org_id, border=container_1, border_radius=20),
                        ft.Container(content=user_password, border=container_1, border_radius=20)])

    # ЧЕК-кнопки с ролями для пользователй
    chek_items = {i: Chips(sup.roles[i], page) for i in range(9)}
    item_2 = ft.Column(controls=list(chek_items.values()), spacing=5,
                        wrap=True, height=110, )

    # задаем контейнеры для размещения
    cont_1 = ft.Container(content=item_1, alignment=ft.alignment.top_left)
    cont_2 = ft.Container(content=item_2, alignment=ft.alignment.top_left)

    # ввод пользователей для редактирования
    user_info = UserInfo("введите ФИО и почту")
    input_block = ft.Container(content=user_info, width=400, height=400,
                               bgcolor="white", border_radius=10,
                               padding=ft.padding.all(8),
                               )
    user_edit = UserInfo("")
    output_block = ft.Container(content=user_edit, width=400, height=400,
                                bgcolor="white", border_radius=10,
                                padding=ft.padding.all(8),
                                )

    # функции для кнопок
    def click_convert(e):
        user_edit.value = "Hello"
        page.update()

    #кнопка для преобразования
    btn_convert = ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=click_convert, data=0, icon_size=40)
    # кнопка для добавления суффикса
    btn = ft.IconButton(icon=ft.icons.ADD_COMMENT, on_click=click_convert, data=0, icon_size=40,
                        style=ft.ButtonStyle(color={ft.MaterialState.FOCUSED: "green"}, ))
    btn_column = ft.Column(controls=[btn, btn_convert])
    # кнопка для отправки
    btn_transfer = ft.ElevatedButton(text="Отправить")

    # Добавление всех элементов на страницу
    element_one = ft.Row([bord_left, cont_1, bord_left, cont_2, ],)
    element_two = ft.Row([bord_left, input_block, bord_ctr, btn_column,
                          bord_ctr, output_block,bord_ctr, btn_transfer])
    page.add(appTitle, bord_top, element_one, bord_top, element_two)


ft.app(target=main)