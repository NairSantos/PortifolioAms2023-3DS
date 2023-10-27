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
          layout.pos_hint = {'top': 0.4}  # Define o topo do layout na parte superior da tela
      
          # Layout superior para os botões "Voltar" e "Login"
          top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
          # Botão Voltar
          back_button = Button(text="",
                             font_size=20,
                             background_normal="img_wireframe/voltar.png",
                             size_hint=(None, None),
                             size=(60, 60))
          voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
          voltar_layout.add_widget(back_button)
          top_button_layout.add_widget(voltar_layout)

        # Título (no topo do layout)
          title_label = Label(text="[color=000000]LOGIN[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=850,
                              markup=True)
          layout.add_widget(title_label)

          # Campos de entrada
          input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})
          # Layout para Nome Completo
          name_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 300))  # Adicionamos margem inferior de 170
          name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                              font_size=12,
                              markup=True)
          name_layout.add_widget(name_label)

          name_input = TextInput(hint_text="Nome Completo", background_color=("#77C4FF"), size_hint_y=None, height=30)
          name_layout.add_widget(name_input)

          layout.add_widget(name_layout)
          
          # Layout para Email
          email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 200))  # Adicionamos margem inferior de 20)
          email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
          email_layout.add_widget(email_label)

          email_input = TextInput(hint_text="Email", background_color=("#77C4FF"), size_hint_y=None, height=30)
          email_layout.add_widget(email_input)

          layout.add_widget(email_layout)

         

        # Layout para Senha  
          senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 100))  # Adicionamos margem inferior de 20)
          senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
          senha_layout.add_widget(senha_label)

          senha_input = TextInput(hint_text="Senha", background_color=("#77C4FF"), size_hint_y=None, height=30)
          senha_layout.add_widget(senha_input)

          layout.add_widget(senha_layout)

          return layout
if __name__ == '__main__':
      LearPlusApp().run()