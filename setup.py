'''PyHook3: Python wrapper for out-of-context input hooks in Windows

The PyHook3 package provides callbacks for global mouse and keyboard events in Windows. Python
applications register event handlers for user input events such as left mouse down, left mouse up,
key down, etc. and set the keyboard and/or mouse hook. The underlying C library reports information
like the time of the event, the name of the window in which the event occurred, the value of the
event, any keyboard modifiers, etc.
'''

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: System :: Monitoring
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
"""

from distutils.core import setup, Extension

libs = ['user32']
doclines = __doc__.split('\n')

setup(name='PyHook3',
      version='1.6.0',
      author='Peter Parente, Markus Dod',
      author_email='mdod@hs-mittweida.de',
      url='https://github.com/gggfreak2003/PyHook3',
      download_url='https://github.com/gggfreak2003/PyHook3',
      license='http://www.opensource.org/licenses/mit-license.php',
      platforms=['Win32'],
      description = doclines[0],
      classifiers = filter(None, classifiers.split('\n')),
      long_description = ' '.join(doclines[2:]),
      packages = ['PyHook3'],
      package_dir = {'PyHook3' : ""},
      ext_modules = [Extension('PyHook3._cpyHook', ['cpyHook.i'], libraries=libs)],
      data_files=[('Lib/site-packages/PyHook3', ['LICENSE', 'README.md', 'CHANGELOG.txt'])]
      )
