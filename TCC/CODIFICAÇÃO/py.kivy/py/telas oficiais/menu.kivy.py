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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
          # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        layout = FloatLayout()
          
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.57}  # Define o topo do layout na parte superior da tela
          
          
          # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
        back_button = Button(text="",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe\ICONS\Menu/perfil.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 2.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior esquerdo
        image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

          # Botão "centro"
        btn5 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe/alunos.png",
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
        btn5.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        btn5.pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Ajuste o valor de 'center_y'
          
        with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
              
          # Rótulo para o primeiro botão
              label1 = Label(text="[color=000000]Alunos[/color]", 
                             halign='center',
                             markup= True)
        
              layout.add_widget(btn5)
              layout.add_widget(label1)

              
          
            # Botão2 "centro"
        btn6 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe\ICONS\Menu/professor.png",
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
        btn6.pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Ajuste o valor de 'center_y'
          
        with btn6.canvas.before:

              self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
              
              # Rótulo para o segundo botão
        label2 = Label(text="[color=000000]Professor[/color]", 
                         halign='center',
                         markup=True)

        layout.add_widget(btn6)
        layout.add_widget(label2)
        
        self.add_widget(layout)
        
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'

    def trocar_para_tela_menu(self, instance):
              self.manager.current = 'menu'

class LoginADMScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginADMScreen, self).__init__(**kwargs)
         # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

          
          
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.67}  # Define o topo do layout na parte superior da tela
          
           # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=30,
                              markup=True)
        layout.add_widget(title_label)
          
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
                      background_normal="py/img_wireframe/voltar.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
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
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria' 
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
        
class SecretariaScreen(Screen):
    def __init__(self, **kwargs):
        super(SecretariaScreen, self).__init__(**kwargs)
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
                    background_normal="py/img_wireframe/voltar.png",
                    size_hint=(None, None),
                    size=(55, 55),
                    pos_hint={'x': 0, 'top': 2.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        

      # Imagem 
        image = Image(source="py/img_wireframe/login.png",
              size_hint=(None, None),
              size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=90)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Botão "centro"
        btn5 = Button(text="", 
                      background_normal="py/img_wireframe\ICONS\Adm.secretaria\Segue.png",
                      size_hint=(None, None), 
                      size=(170, 170), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_cadastro)  # Associar a ação ao botão
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
                      background_normal="py/img_wireframe\ICONS\Adm.secretaria\Conta-verificada.png",
                      size_hint=(None, None), 
                      size=(170, 170), 
                      markup=True)
        btn6.bind(on_release=self.trocar_para_tela_listagem)  # Associar a ação ao botão
        btn6.pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Ajuste o valor de 'center_y'
        
        with btn6.canvas.before:

            self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
            
            # Rótulo para o segundo botão
        label2 = Label(text="[color=000000]Validar Conta[/color]", 
                        halign='center',
                        markup=True)

        layout.add_widget(btn6)
        layout.add_widget(label2)
        
        self.add_widget(layout)
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem' 
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def trocar_para_tela_cadastro(self, instance):
        self.manager.current = 'cadastro' 
        
class CadastroScreen(Screen):
    def __init__(self, **kwargs):
        super(CadastroScreen, self).__init__(**kwargs)
        
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.4}  # Define o topo do layout na parte superior da tela

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=620,
                            markup=True)
        layout.add_widget(title_label)

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Botão Voltar
        back_button = Button(text="Voltar",
                            font_size=7,
                            background_normal="py/img_wireframe/voltar.png",
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 8.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Imagem no canto superior direito
        image = Image(source="py/img_wireframe/Imagem1.png",
                    size_hint=(None, None),
                    size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

        # Nome Completo
        name_layout = BoxLayout (orientation='vertical', spacing=8, padding=(0, 0, 0, 205))

        # Nome Completo
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)

        name_input = TextInput(hint_text="Nome Completo", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        name_layout.add_widget(name_input)

        layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        email_layout.add_widget(email_input)
          
        layout.add_widget(email_layout)
          
        # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        senha_layout.add_widget(senha_input)
          
        layout.add_widget(senha_layout)

        # Botão "Finalizar Cadastro"
        btn5 = Button(text="[color=000000]FINALIZAR CADASTRO[/color]", 
                      background_color=(0.7, 0.87, 0.38, 1), 
                      size_hint=(None, None), 
                      size=(270, 75), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)

        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn6)

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'

        
class ListagemScreen(Screen):
    def __init__(self, **kwargs):
        super(ListagemScreen, self).__init__(**kwargs)
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
       
        self.add_widget(layout)
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'
        
class ContaADMScreen(Screen):
    def __init__(self, **kwargs):
        super(ContaADMScreen, self).__init__(**kwargs)
      # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)
        
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="Voltar",
                    font_size=7,
                    background_normal="py/img_wireframe/voltar.png",
                    size_hint=(None, None),
                    size=(55, 55),
                    pos_hint={'x': 0, 'top': 9.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_cadastro)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
          # Botão "Secretaria"
        btn1 = Button(text="[color=000000]SECRETARIA[/color]", 
                      font_size=18,
                    background_color=(220/255, 220/255, 220/255, 1), 
                    size_hint=(None, None), size=(200, 35), 
                    markup=True,
                    pos_hint={'center_x': 0.5, 'center_y': 0.9})
        btn1.background_normal = ''
        with btn1.canvas.before:
          Rectangle(pos=btn1.pos, size=btn1.size)
        layout.add_widget(btn1)
        
        # Imagem no canto superior direito
        image = Image(source="py/img_wireframe\ICONS\Conta\Avaliacao.png",
              size_hint=(None, None),
              size=(170, 170))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "LISTAGEM"
        btn5 = Button(text="[color=000000]LISTAGEM[/color]", 
                      font_size=18,
                      background_color=(0.7, 0.87, 0.38, 1), 
                      size_hint=(None, None), 
                      size=(200, 35), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_listagem)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
          
        self.add_widget(layout)
    def trocar_para_tela_cadastro(self, instance):
        self.manager.current = 'cadastro'
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'
    def trocar_para_tela_contaADM(self, instance):
        self.manager.current = 'contaADM'
        
class AlunoScreen(Screen):
    def __init__(self, **kwargs):
        super(AlunoScreen, self).__init__(**kwargs)
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
        btn5.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        btn5.pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Ajuste o valor de 'center_y'
        
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
            
        # Rótulo para o primeiro botão
            label1 = Label(text="[color=000000]ESCOLHER ATIVIDADE[/color]", 
                            halign='center',
                            markup= True)
      
            layout.add_widget(btn5)
            layout.add_widget(label1)
        
        self.add_widget(layout)
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'    
        
class EscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(EscolherScreen, self).__init__(**kwargs)
         # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        layout = FloatLayout()

        
          # Título 
        title_label1 = Label(text="[color=000000]Escolha sua Atividade[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=#000000]Nome Atividades[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título dificil
        title_label1 = Label(text="[color=#000000]Nome Atividades[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=400,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py/img_wireframe/voltar.png",
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 9))
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 240))#posicao
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 9))
        layout.add_widget(btn6)
        
        self.add_widget(layout)
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'
class LearPlusApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        # Adicione as telas ao gerenciador de telas
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(LoginADMScreen(name='login'))
        self.sm.add_widget(SecretariaScreen(name='secretaria'))
        self.sm.add_widget(CadastroScreen(name='cadastro'))
        self.sm.add_widget(ListagemScreen(name='listagem'))
        self.sm.add_widget(ContaADMScreen(name='contaADM'))
        self.sm.add_widget(AlunoScreen(name='aluno'))
        self.sm.add_widget(EscolherScreen(name='escolher'))
        return self.sm

if __name__ == '__main__':
    LearPlusApp().run()