#Source: https://stackoverflow.com/questions/65580274/why-does-chatterbot-raise-typeerror-for-my-custom-corpus
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatterbot = ChatBot('test')
trainer = ChatterBotCorpusTrainer(chatterbot)
trainer.train('chatterbot.corpus.custom.random')