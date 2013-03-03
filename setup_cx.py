"""
py2app/py2exe build script for MyApplication.

Will automatically ensure that all build prerequisites are available
via ez_setup

Usage (Mac OS X):
    python setup_cx.py bdist_dmg

Usage (Windows):
    python setup_cx.py bdist_msi
"""
import sys
from cx_Freeze import setup, Executable

NAME='KindleComicConverter'
VERSION="2.4"
mainscript = 'kcc.py'

base = None

if sys.platform == 'darwin':
    extra_options = dict(
        bundle-iconfile='resources/comic2ebook.icns',
        volume-label=NAME + " " + VERSION
        app=[mainscript],
        options=dict(
            py2app=dict(
                argv_emulation=True,
                iconfile='resources/comic2ebook.icns',
                plist=dict(
                    CFBundleName               = NAME,
                    CFBundleShortVersionString = VERSION,
                    CFBundleGetInfoString      = NAME + " " + VERSION + ", written 2012-2013 by Ciro Mattia Gonano",
                    CFBundleExecutable         = NAME,
                    CFBundleIdentifier         = 'com.github.ciromattia.kcc',
                    CFBundleSignature       = 'dplt'
                )
            )
        )
    )
elif sys.platform == 'win32':
    base = "Win32GUI"
    extra_options = dict(
        upgrade-code = 'KindleComicConverter',
        executables = [Executable("kcc.py", base=base)]
    )
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        scripts=[mainscript],
    )

options = dict(

)

setup(
    name=NAME,
    version=VERSION,
    author="Ciro Mattia Gonano",
    author_email="ciromattia@gmail.com",
    description=("A tool to convert comics (CBR/CBZ/PDFs/image folders) to Mobipocket."),
    license = "ISC License (ISCL)",
    keywords = "kindle comic mobipocket mobi cbz cbr manga",
    url = "http://github.com/ciromattia/kcc",
    classifiers=[
        'Development Status :: 4 - Beta'
        'License :: OSI Approved :: ISC License (ISCL)',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Utilities'
    ],
    # make sure to add custom_fixers to the MANIFEST.in
    include_package_data=True,
    executables = [Executable("kcc.py", base=base)]),
    **extra_options
)