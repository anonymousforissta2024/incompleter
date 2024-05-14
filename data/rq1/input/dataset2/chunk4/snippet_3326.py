#Source: https://stackoverflow.com/questions/63018269/builtins-attributeerror-bytes-object-has-no-attribute-append-in-python-twis
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from collections import defaultdict


class MultiChatProtocol(LineReceiver):
    
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.group_name = None
        

    def connectionMade(self):
        self.sendLine(b"Welcome to multi char server ")
        self.sendLine(b"") 
        print(type(self.factory.users))
        print(type(self.factory.groups))
        

        
        
        
    def connectionLost(self, reason):
        if self.name in self.factory.users:
            self.broadcastMessage(b"one member has left the channel.")
            
    def lineReceived(self, line):
        if line == b'':
            self.sendLine(b"write something or type /help for any")
            return
        print("line name" , line)
        
        a = line.split()
        if len(a) > 1:
            command = a[0]
            content = a[1]
            if command == b"/cuser":
                self.save_REGISTER(content)
            elif command == b"/cgroup":
                self.create_Group(content)
            elif command == b"/join":
                self.factory.groups.get(content, []).append(self)
                #self.join_group(content)
        elif line == b"/ulist":
            self.usercount()
        elif line == b"/glist":
            self.groupcount()
        elif line == b"/help":
            self.handle_menu()
        elif line == b"/quite":
            self.connectionLost()

    def join_group(self,args):
        print("args for join",args)
        print("user name for join",self.name)
        #for elem in self.factory.groups:
         #   if args == elem:
          #      elf.factory.groups[args].append(self.name)
        
        d = {}
        y = self.name
        d.setdefault(args, []).append(y)
        print("groups list of d ", d)
        self.factory.groups = d
        print("groups list", self.factory.groups)
    

    def save_REGISTER(self,name):
        if name in self.factory.users:
            self.transport.write(b"Name taken, please choose another.")
            return
        self.sendLine(b"Welcome, %s!" % (name,))
        self.broadcastMessage(b"%s has joined the channel." % (name,))
        self.name = name
        self.factory.users[name] = self
        print("users list",self.factory.users)
        
       
    def create_Group(self,name):
        self.sendLine(b"Enter group name? :")
        self.save_Group(name)

    def create_Group(self,name):
        print("group_name", name)
        print(self.name)
        if name in self.factory.groups:
            self.transport.write(b"Name taken, please choose another.")
            return
        if self.name in self.factory.users:
            self.sendLine(b"%s group created successfully" % (name,))
            self.group_name = name
            self.factory.groups[name] = self
            #self.factory.groups[name] = self.name
            print("groups list",  self.factory.groups)
            
        else:
            self.sendLine(b"you are not register with system sorry")
            
  

    def handle_menu(self):
        self.sendLine(b"")
        self.sendLine(b" please select Following MENU command:")
        self.sendLine(b"1) For register your name type : /cuser yourname")
        self.sendLine(b"2) For create group type : /cgroup groupname")
        self.sendLine(b"3) For Joined group type : /join groupname")
        self.sendLine(b"4) For see list Of group type : /glist")
        self.sendLine(b"5) For exit type : /quite")
        
        

    def handle_CHAT(self, message):    
        message = b"<%s> %s" % (self.name,message)
        self.broadcastMessage(message)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.items():
            if protocol != self:
                protocol.sendLine(message)

    def usercount(self):

        user_count = len(self.factory.users)                                               
        single_or_plural = b'is' if user_count == 1 else b'are'                                                    
        person_or_people = b'person' if user_count == 1 else b'people'                                             
        self.sendLine(b"There %s %i  %s connected:" % (single_or_plural, user_count, person_or_people, ) )                    

        for client in self.factory.users:                                              
            if client is not self:                                                       
                self.sendLine(client)                                               
        self.sendLine(b"")

    def groupcount(self):
        group_count = len(self.factory.groups)                                               
        single_or_plural = b'is' if group_count == 1 else b'are'                                                    
        person_or_people = b'group' if group_count == 1 else b'groups'                                             
        self.sendLine(b"There %s  %i following %s we have :" % (single_or_plural, group_count, person_or_people, ) )                    

        for group in self.factory.groups:                                              
            if group is not self:                                                       
                self.sendLine(group)                                               
        self.sendLine(b"")
        self.sendLine(b"joined above groups by command /join groupname")
        

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}
        self.groups = {}
        
    def buildProtocol(self, addr):
        return MultiChatProtocol(self)
    
reactor.listenTCP(8000, ChatFactory())
print ("Chat Server Started") 
reactor.run()