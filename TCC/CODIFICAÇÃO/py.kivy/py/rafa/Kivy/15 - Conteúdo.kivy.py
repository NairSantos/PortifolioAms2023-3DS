from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout


class LearPlusApp(App):
    def build(self):
        # Defina a cor de fundo
        Window.clearcolor = (240/255, 240/255, 240/255, 1)  # Cor cinza claro (R, G, B, alpha)
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="img_wireframe/voltar.png",
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

        layout.add_widget(top_button_layout)
        
        #titulo Conteudo
        title_label = Label(text="[color=000000]Conteudo[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1250,
                            markup=True)
        layout.add_widget(title_label)
        
        conteudo_button = Button(text="",
                        font_size=0,
                        background_normal="img/quebra-cabeca.png",
                        size_hint=(None, None),
                        size=(100, 100),
                        pos=(50,420))
        layout.add_widget(conteudo_button)
        
        #titulo "Matematica"
        title_label = Label(text="[color=000000]Quebra-Cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            pos=(0,340),
                            markup=True)
        layout.add_widget(title_label)
        
        return layout
if __name__ == '__main__':
    LearPlusApp().run()