#Source: https://stackoverflow.com/questions/21367320/searching-for-equivalent-of-filenotfounderror-in-python-2
#!/usr/bin/python
#-*-coding:utf-8*

#option_controller.py

#Walle Cyril
#25/01/2014

import json
import os

class Options():
    """Options is a class designed to read, add and change informations in a JSON file with a dictionnary in it.

    The entire object works even if the file is missing since it re-creates it.
    If present it must respect the JSON format: e.g. keys must be strings and so on.
    If something corrupted the file, just destroy the file or call read_file method to remake it."""

    def __init__(self,directory_name="Cache",file_name="options.json",imported_default_values=None):
        #json file
        self.option_file_path=os.path.join(directory_name,file_name)
        self.directory_name=directory_name
        self.file_name=file_name
        #self.parameters_json_file={'sort_keys':True, 'indent':4, 'separators':(',',':')}
        #the default data
        if imported_default_values is None:
            DEFAULT_INDENT = 2
            self.default_values={\
                "translate_html_level": 1,\
                "indent_size":DEFAULT_INDENT,\
                "document_title":"Titre"}
        else:
            self.default_values=imported_default_values


    def read_file(self,read_this_key_only=False):
        """returns the value for the given key or a dictionary if the key is not given.

        returns None if it s impossible"""
        try:
            text_in_file=open(self.option_file_path,'r').read()
        except FileNotFoundError:#not 2.X compatible
            text_in_file=""#if the file is not there we re-make one with default values
        if text_in_file=="":#same if the file is empty
            self.__insert_all_default_values()
            text_in_file=open(self.option_file_path,'r').read()

        try:
            option_dict=json.loads(text_in_file)
        except ValueError:
            #if the json file is broken we re-make one with default values
            self.__insert_all_default_values()
            text_in_file=open(self.option_file_path,'r').read()
            option_dict=json.loads(text_in_file)

        if read_this_key_only:
            if read_this_key_only in option_dict:
                return option_dict[read_this_key_only]#
            else:
                #if the value is not there it should be written for the next time
                if read_this_key_only in self.default_values:
                    self.add_option_to_file(read_this_key_only,self.default_values[read_this_key_only])
                    return self.default_values[read_this_key_only]
                else:
                    #impossible because there is not default value so the value isn t meant to be here
                    return None
        else:
            return option_dict

    def add_option_to_file(self,key,value):#or update
        """Adds or updates an option(key and value) to the json file if the option exists in the default_values of the object."""

        option_dict=self.read_file()
        if key in self.default_values:
            option_dict[key]=value
        open(self.option_file_path,'w').write(\
            json.dumps(option_dict,sort_keys=True, indent=4, separators=(',',':')))


    def __insert_all_default_values(self):
        """Recreate json file with default values.

    called if the document is empty or non-existing or corrupted."""
        try:
            open(self.option_file_path,'w').write(\
            json.dumps(self.default_values,sort_keys=True, indent=4, separators=(',',':')))
        except FileNotFoundError:
            os.mkdir(self.directory_name)#Create the directory
            if os.path.isdir(self.directory_name):#succes
                self.__insert_all_default_values()
            else:
                print("Impossible to write in %s and file %s not found" % (os.getcwd(),self.option_file_path))


#demo
if __name__ == '__main__':

    option_file_object=Options()
    print(option_file_object.__doc__)
    print(option_file_object.read_file())
    option_file_object.add_option_to_file("","test")#this should have no effect

    option_file_object.add_option_to_file("translate_html_level","0")#this should have an effect
    print("value of translate_html_level:",option_file_object.read_file("translate_html_level"))
    print(option_file_object.read_file())