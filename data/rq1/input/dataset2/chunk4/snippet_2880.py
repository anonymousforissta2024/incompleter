#Source: https://stackoverflow.com/questions/71928720/attributeerror-imagecard-object-has-no-attribute-source
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Imports para trabalhar com Firebase
from config import config
import pyrebase


Builder.load_string("""
<ImageCard@MDCard>
    id: ec

    size_hint: ('180dp', None)
    ripple_behavior: True
    image:''
    text:''

    orientation:'vertical'

    FitImage:
        pos_hint: {'center_x': .5, 'center_y': .25} 
        source: './images/user.png' # root.source
        size_hint: None, None
        width: dp(150) 
        height: dp(150) 
        #radius: [99, 99, 99, 99]

    MDBoxLayout:
        orientation:'horizontal'
        MDLabel:
            text:root.text
            halign:"center"
            #bold: True

    MDFlatButton:
        text: "New Screen Here"
        increment_width: "164dp"

        on_release: root.show_confirmation_dialog()

<ScreenRecycleView>:
    name: 'recycle_view' 

    FloatLayout:

        MDTextField:
            id: pesquisa

            helper_text: "Escreva um trecho da pesquisa e clique em pesquisar."
            helper_text_mode: "on_focus"
            size_hint: .99, None
            halign: 'center' 
            multiline: False 


            hint_text: 'Digite o que procura'
            text_validate_unfocus: False
            pos_hint: {'center_x': 0.42, 'center_y': 0.84}
            padding: dp(15)        
            #size_hint_x: .75
            #on_text: root.on_kv_post(self, self.text)

        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": .95, "center_y": 0.84}
            on_release: root.on_kv_post(self, pesquisa.text)            
        

        #:import get_color_from_hex kivy.utils.get_color_from_hex        
        MDBoxLayout:
            
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            RecycleView:
                data: root.image_data
                viewclass: "ImageCard"
                RecycleGridLayout:
                    cols: 2
                    default_size: dp(155), dp(200)
     
                    padding: dp(5) # Determina o espaçamento entre um widget e outro pelos lados               
                    spacing: dp(5) # Determina o espaçamento entre um widget e outro de cima para baixo
                    default_size_hint: 1, None ##### Define a largura do widget sempre próximo as bordas
                    size_hint_y: None ##### Associado a default_size_hint
                    height: self.minimum_height
                    #ripple_behavior: True""")    

class Content(BoxLayout):
    pass

class ImageCard(MDCard):
    dialog = None
    text = StringProperty()
    source = StringProperty()

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                #title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

class ScreenRecycleView(Screen):   
    image_data = ListProperty()

    def on_kv_post(self, base_widget, text="", search=False):
        
        # Inicializando o banco de dados.
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

        self.produtos = self.db.child("Produtos").get(token='**************************************')
        
        #self.ids.rv3.data = []
        self.image_data = []
        
        for produto in self.produtos.each():
            if text.upper() in produto.val()['nmproduto']:
                if produto.val()['url'] != 'SemUrl':
                    self.image_data.append(
                        {"source": produto.val()['url'],
                        "text": produto.val()['nmproduto']
                        }
                    )
                else:
                    self.image_data.append(
                        {"source": './images/sem_imagem.png',
                        "text": produto.val()['nmproduto']
                        }
                    ) 

        #print(json.dumps(self.ids.rv3.data, indent=4))