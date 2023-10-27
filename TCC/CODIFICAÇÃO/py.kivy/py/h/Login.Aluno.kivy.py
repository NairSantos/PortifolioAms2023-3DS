from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle


class LearPlusApp(App):
      def build(self):
          # Defina a cor de fundo
          Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

          
          
          # Layout principal
          layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
          layout.pos_hint = {'top': 0.67}  # Define o topo do layout na parte superior da tela
          
          
           # Título (no topo do layout)
          title_label = Label(text="[color=000000]Login[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=150,
                              markup=True)
          layout.add_widget(title_label)
          
          # Layout superior para os botões "Voltar" e "Login"
          top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
          back_button = Button(text="Voltar",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe/voltar.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
          top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior direito
          image = Image(source="",
                size_hint=(None, None),
                size=(55, 55))
          anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=260)
          anchor_layout.add_widget(image)
          top_button_layout.add_widget(anchor_layout)

          layout.add_widget(top_button_layout)
          
          # Campos de entrada
          input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})
        
          # Nome
          name_label2 = Label(text="[color=000000]NOME:[/color]", 
                               font_size=14, 
                               size_hint_x=None, 
                               width=150,
                               markup=True)
          input_layout.add_widget(name_label2)

          name_input = TextInput(hint_text="Email", background_color=(0.5, 0.7, 1, 1))
          input_layout.add_widget(name_input)
          
        # Email
          input_label2 = Label(text="[color=000000]EMAIL:[/color]", 
                               font_size=14, 
                               size_hint_x=None, 
                               width=150,
                               markup=True)
          input_layout.add_widget(input_label2)

          email_input = TextInput(hint_text="Email", background_color=(0.5, 0.7, 1, 1))
          input_layout.add_widget(email_input)

          # Widget em branco para aumentar o espaço
          layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário
        # Senha
          input_label3 = Label(text="[color=000000]SENHA:[/color]", 
                               font_size=14, 
                               size_hint_x=None, 
                               width=150,
                               markup=True)
          input_layout.add_widget(input_label3)

          password_input = TextInput(hint_text="Senha", 
                                     background_color=(0.5, 0.7, 1, 1))
          input_layout.add_widget(password_input)

          layout.add_widget(input_layout)

         # Botão "REALIZAR LOGIN"
          btn5 = Button(text="REALIZAR LOGIN", 
                        background_color=(0.5, 0.7, 1, 1), 
                        size_hint=(None, None), 
                        size=(270, 45))
          btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
          layout.add_widget(btn5)
        

          return layout
          
if __name__ == '__main__':
      LearPlusApp().run()