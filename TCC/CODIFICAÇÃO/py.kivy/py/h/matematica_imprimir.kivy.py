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
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe/Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matematica[/color]",
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
        
        # Layout para voltar
        voltar_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        voltar_label = Label(text="[color=000000]Voltar[/color]",
                            font_size=12,
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 9.9},  # Posiciona no canto superior esquerdo
                            height=830,
                            pos=(10, 640),
                            markup=True)
        voltar_layout.add_widget(voltar_label)
        
        
        layout.add_widget(voltar_layout)
        

   # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
              size_hint=(None, None),
              size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        
        

        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=100, pos_hint={'x': 0})

        # Layout para Nome Completo
        name_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]Estão disponiveis duas sessões sobre\nmatemática para a impressão:\n1 sessão  - adição e subtração \n2ª sessão - multiplicação e divisão.[/color]",
                            font_size=20,
                            markup=True)
        name_layout.add_widget(name_label)
        
        
        layout.add_widget(name_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=(0.69, 0.87, 0.98, 1), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        


        return layout
        
if __name__ == '__main__':
    LearPlusApp().run()