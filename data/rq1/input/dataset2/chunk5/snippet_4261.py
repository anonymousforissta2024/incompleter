#Source: https://stackoverflow.com/questions/57345721/how-to-fix-attributeerror-on-using-pyinstaller-on-a-project-with-tensorflow-an
a = Analysis(['main.py'],
             pathex=['<path to project folder>', '<path to venv folder>\lib\site-packages\tensorflow\python\keras\api\_v2\keras\__init__.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)