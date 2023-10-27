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



class pci(App):
    def build(self):
        # Defina a cor de fundo
        Window.clearcolor = (240/255, 240/255, 240/255, 1)  # Cor cinza claro (R, G, B, alpha)

        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras \nCruzadas[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc-imagem.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]Estão disponiveis três\nníveis de palavras\ncruzadas para a\nimpressão: nível fácil\n(1 a 5 palavras), nível\nmédio (de 5 a 10\npalavras), e o nível\ndifícil (contendo mais\nde 10 palavras).[/color]",
                            font_size=20,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=490)
        anchor_layout.add_widget(name_label)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        


        return layout
        
if __name__ == '__main__':
    pci().run()