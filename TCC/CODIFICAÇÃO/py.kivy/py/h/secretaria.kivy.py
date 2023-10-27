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
from kivy.uix.floatlayout import FloatLayout


class LearPlusApp(App):
      def build(self):
          # Defina a cor de fundo
          Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

          layout = FloatLayout()
          
          # Layout principal
          layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
          layout.pos_hint = {'top': 0.57}  # Define o topo do layout na parte superior da tela
          
          # Título (no topo do layout)
          title_label = Label(text="[color=000000]Secretaria[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=50,
                              markup=True)
          layout.add_widget(title_label)
          
          # Layout superior para os botões "Voltar" e "Login"
          top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
          back_button = Button(text="",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe/voltar.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 2.0})  # Posiciona no canto superior esquerdo
          top_button_layout.add_widget(back_button)
          

        # Imagem 
          image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
                size_hint=(None, None),
                size=(55, 55))
          anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
          anchor_layout.add_widget(image)
          top_button_layout.add_widget(anchor_layout)

          layout.add_widget(top_button_layout)

          # Botão "centro"
          btn5 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe\ICONS\Adm.secretaria\Segue.png",
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
          btn5.pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Ajuste o valor de 'center_y'
          
          with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
              
          # Rótulo para o primeiro botão
              label1 = Label(text="[color=000000]Adicionar Conta[/color]", 
                             halign='center',
                             markup= True)
        
              layout.add_widget(btn5)
              layout.add_widget(label1)

              
          
            # Botão2 "centro"
          btn6 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe\ICONS\Adm.secretaria\Conta-verificada.png",
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
          btn6.pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Ajuste o valor de 'center_y'
          
          with btn6.canvas.before:

              self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
              
              # Rótulo para o segundo botão
          label2 = Label(text="[color=000000]Validar Conta[/color]", 
                         halign='center',
                         markup=True)

          layout.add_widget(btn6)
          layout.add_widget(label2)


          return layout
          
if __name__ == '__main__':
      LearPlusApp().run() 