# -*- mode: python -*-

block_cipher = None


a = Analysis(['service_in.py'],
             pathex=['C:\\Users\\Osama Chaudhary\\PycharmProjects\\non_pe_detections'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='service_in',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
