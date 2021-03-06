# -*- mode: python -*-

from glob import glob

a = Analysis(['./mitmweb'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
          )
a.datas = Tree(
  "./libmproxy/onboarding/templates",
  prefix="libmproxy/onboarding/templates"
)
a.datas += Tree(
  "./libmproxy/onboarding/static",
  prefix="libmproxy/onboarding/static"
)
a.datas += Tree(
  "./libmproxy/web/templates",
  prefix="libmproxy/web/templates"
)
a.datas += Tree(
  "./libmproxy/web/static",
  prefix="libmproxy/web/static"
)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mitmweb',
          debug=False,
          strip=None,
          upx=True,
          console=True )
