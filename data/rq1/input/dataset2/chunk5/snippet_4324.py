#Source: https://stackoverflow.com/questions/54315359/typeerror-check-missing-1-required-positional-argument-self
import re

class login(object):
    def check(self):
        self.mail = r"([\w\.-]+)@([\w\.-]+)([\w\.-]+)"
        with open('login.txt', 'r') as self.myfile:
            self.line1 = self.myfile.read().replace('\n', '')
        with open('username.txt', 'r') as self.usr:
            self.line2 = self.usr.read().replace('\n', '')
        if re.findall(self.mail, self.line1):
            goon()
        else:
            log()
        self.myfile.close()

    def goon(self):
        import assistant #another code to exec.

    def log(self):
        self.file = open("login.txt", "w")
        self.file.truncate(0)
        self.data = input("Your email: ")
        self.file.write(self.data)
        self.file.close()
        l.goon()

    if __name__ == '__main__':
        check() #error
        log()
        goon()