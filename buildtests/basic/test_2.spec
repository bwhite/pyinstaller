# -*- mode: python -*-

__testname__ = 'test_2'

config['useZLIB'] = 0
a = Analysis([__testname__ + '.py'],
             pathex=[],
             hookspath=['hooks1'])
pyz = PYZ(a.pure, level=0)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build', 'pyi.'+sys.platform, __testname__ + '.exe'),
          icon='test_2.ico',
          version='test_2-version.txt',
          debug=0,
          console=1)
coll = COLLECT( exe,
               a.binaries - [('zlib','','EXTENSION')],
               name=os.path.join('dist', __testname__),)
