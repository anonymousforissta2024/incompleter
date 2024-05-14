#Source: https://stackoverflow.com/questions/54327442/filenotfounderror-even-though-file-exist
def main():
        lines =0
        path = '//10.8.4.49/Projects/QASA_BR_TCL_Env_7.2.250/Utils/BR_Env/Call Generator/results/Console_Logs/*'
        files = glob.glob(path)
        print ("files")
        print ('\n')
        print(files)
        for name in glob.glob(path):
            print (path)
            readFile = name.split("/")[9].split("\\")[1]
            print(readFile)
            with open(readFile,"r") as file:
                lines = file.readlines()
                print (lines)
main()

files