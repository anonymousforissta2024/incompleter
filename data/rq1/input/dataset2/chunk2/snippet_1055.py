#Source: https://stackoverflow.com/questions/51153553/not-returning-updates-to-yaml-file-and-returning-typeerror-on-string-update
class YAML_Config:
    '''
    Class used to interact with .YAML filetypes. Allows the creation of objects \
    that can be manipulated and save certain YAML files and configuration settings.
    '''

    def __init__(self, filename):
        '''
        Initial defintion. Defines the location for saving a new .YAML file or for loading \
        a previous one. The dictionary corresponding to the .YAML file is saved to self.dict. \
        If this is a new .YAML file, an empty dictionary is created.

        Input Arguments:
            -filename: (string) The name of the file where the current .YAML file is \
            located or the new .YAML will be saved.
        '''
        #Get the filename and save it to the class as a property.
        self.file = filename

        #Check if the file exists...
        if os.path.isfile(self.file):

            #Prepare to open the file with reading capabilities
            with open(self.file,'r') as infile:

                #Get a dictionary with all of the YAML informatin.
                yaml_dict = yaml.load(infile)

        #If the file does not exist...
        else:

            #Create an empty dictionary to save all YAML data.
            yaml_dict = {}

            #Create an empty .yaml file with the dictionary.
            with open(self.file, 'w') as infile:

                #Save updated dictionary to YAML file.
                yaml.dump(yaml_dict, infile, default_flow_style=False)

            print('YAML configuration file not found. New, empty dictionary, and .yaml file created.')

        self.dict=yaml_dict




    def update_value(self, kwargs):
        '''
        Used to update YAML files, and checks that the files were updated properly.
        '''
        #If these are not keyword arguments, then throw an error.
        assert kwargs, 'Input Error'

        #Get the YAML dictionary before it is updated.
        yaml_dict = self.dict


        #Make a copy of the dictionary to compare against later.
        yaml_dict_original = copy.deepcopy(self.dict)

        #Check if the dictionary is nonetype. This happens if the file is new as the file is empty.
        if yaml_dict_original is None:

            #Redefine orginal dictionary as an empty dictionary.
            yaml_dict_original={}

            #The new dictionary will simply be what is passed to the function.
            yaml_dict=kwargs

        else:

            #Update the original dictionary and update it with the arguments passed.
            #This also updates self.dict as yaml_dict is simply a reference to
            #that dictionary, not a copy of it.
            yaml_dict.update(kwargs)


        #Check if changes were made
        if (yaml_dict==yaml_dict_original) is False:

            #Open the YAML file to write to it.
            with open(self.file, 'w') as outfile:

                #Save updated dictionary to YAML file.
                yaml.dump(self.dict, outfile, default_flow_style=False)


    #Check that the file actually updated properly:

            #Double-check the file that it actually updated.
            with open(self.file, 'r') as infile:

                lastupdate = yaml.load(infile)

            #Get any nonmatching values between what should be in the YAML file and what actually is.
            errors = { k : yaml_dict[k] for k in set(yaml_dict) - set(lastupdate) }

            #Find out what changed in the YAML file.
            edits = { k : yaml_dict_original[k] for k in set(yaml_dict_original) - set(lastupdate) }

            #Check if errors is not empty. Evaluating dictionaries as boolean either returns True (not empty)
            #or False (empty).
            if bool(errors) is True:

                #First line of return print statement.
                print('The following entries did not update successfully:')

                #Loop through keys in errors
                for n in errors:

                    #Print the current key
                    print (n)

                    #Loop through entries of current key
                    for m in errors[n]:

                        #Print current entry of current key
                        print (m,':',errors[n][m])

            #Saved properly, check for edits and display to user.
            else:

                #Find where any edits were made.
                edits = {k: yaml_dict_original[k] for k in yaml_dict_original if k in lastupdate and yaml_dict_original[k] != lastupdate[k]}

                #Show user what edits were successfuly made.
                print('%s was successfully updated with the following changes:' %  os.path.basename(self.file))

                #Loop through keys in edits
                for n in edits:

                    #Print the current key
                    print (n)

                    #Loop through entries of current key
                    for m in edits[n]:

                        #Print current entry of current key
                        print (m,':',edits[n][m])

        #If no changes were made...        
        else:

            #Show user what edits were successfuly made.
            print('No changes to %s were passed. File not updated.' %  

    os.path.basename(self.file))



test=YAML_Config(r'...Path\Python Work\yaml_test.yaml')

d = {'A': 7, 'B':{'C':'D', 'D':False, 'E':'Julio'},\
     'The Real C': {'J?':'Yes, this is J.', 'K' : 241},'Q' : 'PQ'}

test.update_value(d)