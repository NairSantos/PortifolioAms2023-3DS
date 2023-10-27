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
          
          
          # Layout superior para os botões "Voltar" e "Login"
          top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
          back_button = Button(text="Voltar",
                      font_size=7,
                      background_normal="py/img_wireframe/voltar.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 4.6})  # Posiciona no canto superior esquerdo
          top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior direito
          image = Image(source="py/img_wireframe/login.png",
                size_hint=(None, None),
                size=(55, 55))
          anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=230)
          anchor_layout.add_widget(image)
          top_button_layout.add_widget(anchor_layout)

          layout.add_widget(top_button_layout)


         # Botão "centro"
          btn5 = Button(text="", 
                        background_normal="PY/img_wireframe/ICONS/Aluno/escolher_atividade.png",
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
          btn5.pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Ajuste o valor de 'center_y'
          
          with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
              
          # Rótulo para o primeiro botão
              label1 = Label(text="[color=000000]ESCOLHER ATIVIDADE[/color]", 
                             halign='center',
                             markup= True)
        
              layout.add_widget(btn5)
              layout.add_widget(label1)
          return layout
          
if __name__ == '__main__':
      LearPlusApp().run()