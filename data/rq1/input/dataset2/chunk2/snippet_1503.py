#Source: https://stackoverflow.com/questions/68239345/typeerror-after-converting-python-game-to-executable
# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'icinga.py'],
             pathex=['/home/user/projects/icinga_python/releases/v2.1'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'myscript'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )