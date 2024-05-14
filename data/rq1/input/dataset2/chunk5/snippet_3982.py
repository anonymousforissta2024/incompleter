#Source: https://stackoverflow.com/questions/42145686/issue-with-accessing-kivy-widgets-from-python-attributeerror-nonetype-object
class LoginScreen(Screen):
    spinner_bay = ObjectProperty()#ListProperty()
    spinner_part_number = ObjectProperty()#ListProperty()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.load_login_view()

    def load_login_view(self):
        print("Loading login screen ... " + strftime("%H:%M:%S"))
        #Window.size = (300, 550) 

        PART_NUMBERS = []#ListProperty([])
        BAY_NUMBERS = []#ListProperty([])

        # Open configuration.txt file and find bay numbers & part numbers
        try:
            config_file = open('configuration.txt')
            list_config_file = config_file.readlines()
            #BAY_NUMBERS = bay_number_file.close
            config_file.close

            for line in list_config_file:
                split_line = line.split(' ')
                split_line[-1] = split_line[-1].strip()

                if 'PART_NUMBERS' in split_line:
                    self.spinner_part_number.values = split_line[2:]

                if 'BAY_NUMBERS' in split_line:
                    #for i in range(int(split_line[2]), int(split_line[3]) + 1, 1):
                    self.spinner_bay.values = split_line[2:]
                    print('Loaded bay numbers.')
        except:
            print("Error found.")