# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['labelImg.py'],
             pathex=['./libs', './', 'C:\\Projects\\HighVenueLabelUtil\\venv', 'C:/Users/wojia/AppData/Local/Programs/Python/Python37/Lib/encodings', 'C:\\Projects\\HighVenueLabelUtil\\venv\\Lib', 'C:\\Projects\\HighVenueLabelUtil\\venv\\Lib\\site-packages', 'C:\\Projects\\HighVenueLabelUtil\\data', 'C:\\Projects\\HighVenueLabelUtil'],
             binaries=[],
             datas=[("data", "data")],
             hiddenimports=['xml', 'xml.etree', 'xml.etree.ElementTree', 'lxml.etree', 'PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='labelImg',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
