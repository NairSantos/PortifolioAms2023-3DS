from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Botão para abrir a tabela
        open_table_button = Button(text="Abrir Tabela", size_hint_y=None, height=100)
        open_table_button.bind(on_press=self.open_table)
        layout.add_widget(open_table_button)

        self.add_widget(layout)

    def open_table(self, instance):
        app = App.get_running_app()
        app.root.transition.direction = 'left'
        app.root.current = 'table'


class TabelaScreen(Screen):
    def __init__(self, **kwargs):
        super(TabelaScreen, self).__init__(**kwargs)

        data = [
            {"nome": "João", "email": "joao@example.com", "senha": "senha1", "autorizar": False},
            {"nome": "Maria", "email": "maria@example.com", "senha": "senha2", "autorizar": True},
            {"nome": "Pedro", "email": "pedro@example.com", "senha": "senha3", "autorizar": False},
        ]

        layout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="Nome"))
        layout.add_widget(Label(text="Email"))
        layout.add_widget(Label(text="Senha"))
        layout.add_widget(Label(text="Autorizar"))
        layout.add_widget(Label(text="Inativar"))
        layout.add_widget(Label(text="Atualizar"))

        for row in data:
            layout.add_widget(Label(text=row["nome"]))
            layout.add_widget(Label(text=row["email"]))
            layout.add_widget(Label(text=row["senha"]))
            checkbox = CheckBox(active=row["autorizar"])
            layout.add_widget(checkbox)
            inativar_button = Button(text="Inativar", size_hint=(None, None), size=(100, 30))
            layout.add_widget(inativar_button)
            atualizar_button = Button(text="Atualizar", size_hint=(None, None), size=(100, 30))
            layout.add_widget(atualizar_button)

        tabela_scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 100))
        tabela_scrollview.add_widget(layout)

        self.add_widget(tabela_scrollview)


class LearPlusApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name='main')
        table_screen = TabelaScreen(name='table')
        sm.add_widget(main_screen)
        sm.add_widget(table_screen)
        return sm


if __name__ == '__main__':
    LearPlusApp().run()
