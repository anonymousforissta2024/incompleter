#Source: https://stackoverflow.com/questions/73864920/kivy-python-3-8-if-statement-in-canvas-returns-attributeerror-nonetype-ob
# Using kivy 2.0.0 and Python 3.8

import kivy
from kivy.config import Config  # For setting height (19.5:9)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty
from kivy.storage.jsonstore import JsonStore

kivy.require('2.0.0')  # Version of Kivy)
Config.set('graphics', 'width', '360')  # (New Android smartphones e.g. OnePlus 7 series, iPhone X,
Config.set('graphics', 'height', '640')  # 11 and 12 series, upsampled)
store = JsonStore('user_data.json')  # For saving high score and wallet
root_widget = Builder.load_file('layout.kv')

# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # If necessary, uncomment to prevent OpenGL error


class GameWidget(Screen):

    score = NumericProperty(0)  # Current score
    highscore = NumericProperty(store.get('highscore')['score'])  # High score
    old_highscore = NumericProperty(store.get('highscore')['score'])  # Previous high score for comparison
    broke_record = BooleanProperty(False)  # For checking if a new high score is achieved

    wallet = NumericProperty(store.get('wallet')['coins'])  # Amount of coins that user has collected
    wallet_label = ObjectProperty()  # In-game label where wallet is viewed
    old_wallet = wallet  # Used for count_coins() function

    coins = NumericProperty(0)  # Amount of coins earned in current level

    # Update the wallet
    def pay_coins(self):

        if self.game_finish:

            self.wallet += self.coins
            store.put("wallet", coins=self.wallet)
            self.wallet = store.get("wallet")["coins"]
            print("Wallet: %s" % self.wallet)
            self.old_wallet -= self.coins

    # Function to visually show the coins being added to the wallet
    def count_coins(self, dt):

        if self.coins >= 1:
            self.coins -= 1
            self.old_wallet += 1

    # Check if new high score is achieved
    def check_score(self):

        if self.score > self.highscore:
            store.put("highscore", score=self.score)
            self.highscore = store.get("highscore")["score"]

            self.broke_record = True

            print('new high!')
        else:
            self.broke_record = False

    # Reset all variables
    def reload(self):

        self.score = 0
        self.highscore = store.get("highscore")["score"]
        self.old_highscore = self.highscore
        self.broke_record = False

        self.wallet = store.get("wallet")["coins"]
        self.old_wallet = self.wallet

        self.coins = 0


class Menu(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    WindowManager = WindowManager()

    def build(self):

        return self.WindowManager

MyApp().run()