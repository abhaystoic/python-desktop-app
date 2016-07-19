# -*- mode: python -*-
a = Analysis(['provision.py'],
             pathex=['/home/abhay/Desktop/TKINTER/pkging'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='provision',
          debug=False,
          strip=None,
          upx=True,
          console=True )
