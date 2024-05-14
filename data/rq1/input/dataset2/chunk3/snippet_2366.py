#Source: https://stackoverflow.com/questions/62397348/filenotfounderror-on-heroku-after-creating-that-file
if not os.path.exists(f'Logs/{name}.log'):
    open(f'Logs/{name}.log', 'w+').close()