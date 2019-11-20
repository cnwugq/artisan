"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup-mac35.py py2app
"""

# manually remove sample-data mpl subdirectory from Python installation:
# sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.6/site-packages/matplotlib/mpl-data/sample_data

# THIS PATCH SEEMS NOT TO BE NEEDED ANYMORE:
#from distutils import sysconfig
#their_parse_makefile = sysconfig.parse_makefile
#def my_parse_makefile(filename, g):
#    their_parse_makefile(filename, g)
#    g['MACOSX_DEPLOYMENT_TARGET'] = os.environ['MACOSX_DEPLOYMENT_TARGET']
#sysconfig.parse_makefile = my_parse_makefile

import sys, os
import subprocess
from setuptools import setup

import string
import plistlib

import artisanlib

# current version of artisan
VERSION = artisanlib.__version__
LICENSE = 'GNU General Public License (GPL)'

QTDIR = os.environ["QT_PATH"] + r'/'

APP = ['artisan.py']

DATA_FILES = [
    ("./LICENSE.txt", [r"../LICENSE"]),
    ("../Resources/qt_plugins/iconengines", [QTDIR + r'/plugins/iconengines/libqsvgicon.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqdds.dylib']),  # not on Qt5.8.x
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqgif.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqicns.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqico.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqjp2.dylib']),  # not on Qt5.6.x
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqjpeg.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqmacjp2.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqmng.dylib']), # not on Qt5.6.x
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqsvg.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqtga.dylib']),
#    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqtiff.dylib']),  # produces a strip error
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqwbmp.dylib']),
    ("../Resources/qt_plugins/imageformats", [QTDIR + r'/plugins/imageformats/libqwebp.dylib']),
    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqcocoa.dylib']), # qt5
#    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqoffscreen.dylib']), # qt5
#    ("../Resources/qt_plugins/platforms", [QTDIR + r'/plugins/platforms/libqminimal.dylib']), # qt5
    ("../Resources/qt_plugins/printsupport", [QTDIR + r'/plugins/printsupport/libcocoaprintersupport.dylib']), # qt5/# standard
    ("../Resources/qt_plugins/styles", [QTDIR + r'/plugins/styles/libqmacstyle.dylib']), # QT 5.10 and later requires this (not available on 5.8)
#    ("../Resources/qt_plugins/platformthemes", [QTDIR + r'/plugins/platformthemes/libqxdgdesktopportal.dylib']), # unclear what this is for (not available before 5.12)

# for now make a copy of the plugins in the default Qt directory to make Qt happy:
    ("../PlugIns/iconengines", [QTDIR + r'/plugins/iconengines/libqsvgicon.dylib']),
#    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqdds.dylib']),  # not on Qt5.8.x
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqgif.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqicns.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqico.dylib']),
#    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqjp2.dylib']),  # not on Qt5.6.x
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqjpeg.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqmacjp2.dylib']),
#    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqmng.dylib']), # not on Qt5.6.x
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqsvg.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqtga.dylib']),
#    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqtiff.dylib']),  # produces a strip error
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqwbmp.dylib']),
    ("../PlugIns/imageformats", [QTDIR + r'/plugins/imageformats/libqwebp.dylib']),
    ("../PlugIns/platforms", [QTDIR + r'/plugins/platforms/libqcocoa.dylib']), # qt5
#    ("../PlugIns/platforms", [QTDIR + r'/plugins/platforms/libqoffscreen.dylib']), # qt5
#    ("../PlugIns/platforms", [QTDIR + r'/plugins/platforms/libqminimal.dylib']), # qt5
    ("../PlugIns/printsupport", [QTDIR + r'/plugins/printsupport/libcocoaprintersupport.dylib']), # qt5/# standard
    ("../PlugIns/styles", [QTDIR + r'/plugins/styles/libqmacstyle.dylib']), # QT 5.10 and later requires this (not available on 5.8)
#    ("../PlugIns/platformthemes", [QTDIR + r'/plugins/platformthemes/libqxdgdesktopportal.dylib']), # unclear what this is for (not available before 5.12)


# standard QT translation needed to get the Application menu bar and 
# the standard dialog elements translated
    ("../translations", [QTDIR + r'/translations/qtbase_ar.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_de.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_en.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_es.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_fi.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_fr.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_he.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_hu.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_it.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_ja.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_ko.qm']),
#    ("../translations", [QTDIR + r'/translations/qtbase_pt.qm']),    # empty/missing
    ("../translations", [QTDIR + r'/translations/qtbase_pl.qm']),
    ("../translations", [QTDIR + r'/translations/qtbase_ru.qm']),
#    ("../translations", [QTDIR + r'/translations/qtbase_sv.qm']),    # empty/missing
#    ("../translations", [QTDIR + r'/translations/qtbase_zh_CN.qm']), # empty/missing
    ("../translations", [QTDIR + r'/translations/qtbase_zh_TW.qm']),
    ("../translations", [r'translations/artisan_ar.qm']), 
    ("../translations", [r"translations/artisan_de.qm"]),
    ("../translations", [r"translations/artisan_el.qm"]),
    ("../translations", [r"translations/artisan_es.qm"]),
    ("../translations", [r"translations/artisan_fa.qm"]),
    ("../translations", [r"translations/artisan_fi.qm"]),
    ("../translations", [r"translations/artisan_fr.qm"]),
    ("../translations", [r"translations/artisan_he.qm"]),
    ("../translations", [r"translations/artisan_hu.qm"]), 
    ("../translations", [r"translations/artisan_id.qm"]),  
    ("../translations", [r"translations/artisan_it.qm"]),
    ("../translations", [r"translations/artisan_ja.qm"]),
    ("../translations", [r'translations/artisan_ko.qm']),
    ("../translations", [r'translations/artisan_pt.qm']),
    ("../translations", [r'translations/artisan_pt_BR.qm']),
    ("../translations", [r'translations/artisan_pl.qm']),
    ("../translations", [r'translations/artisan_ru.qm']),
    ("../translations", [r"translations/artisan_sv.qm"]),
    ("../translations", [r'translations/artisan_zh_CN.qm']),
    ("../translations", [r'translations/artisan_zh_TW.qm']),
    ("../translations", [r"translations/artisan_no.qm"]),
    ("../translations", [r"translations/artisan_nl.qm"]),
    ("../translations", [r"translations/artisan_tr.qm"]),
    ("../translations", [r"translations/artisan_th.qm"]),
    ("../translations", [r"translations/qtbase_el.qm"]), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ("../translations", [r"translations/qtbase_fa.qm"]), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ("../translations", [r"translations/qtbase_pt.qm"]), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ("../translations", [r"translations/qtbase_sv.qm"]), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ("../translations", [r"translations/qtbase_zh_CN.qm"]), # unfinished translations from https://code.qt.io/cgit/qt/qttranslations.git/
    ("../Resources", [r"qt.conf"]),
    ("../Resources", [r"artisanProfile.icns"]),
    ("../Resources", [r"artisanAlarms.icns"]),
    ("../Resources", [r"artisanPalettes.icns"]),
    ("../Resources", [r"artisanSettings.icns"]),
    ("../Resources", [r"artisanTheme.icns"]),
    ("../Resources", [r"artisanWheel.icns"]),
    ("../Resources", [r"includes/alarmclock.eot"]),
    ("../Resources", [r"includes/alarmclock.svg"]),
    ("../Resources", [r"includes/alarmclock.ttf"]),
    ("../Resources", [r"includes/alarmclock.woff"]),
    ("../Resources", [r"includes/artisan.tpl"]),
    ("../Resources", [r"includes/bigtext.js"]),
    ("../Resources", [r"includes/sorttable.js"]),
    ("../Resources", [r"includes/report-template.htm"]),
    ("../Resources", [r"includes/roast-template.htm"]),
    ("../Resources", [r"includes/ranking-template.htm"]),
    ("../Resources", [r"includes/Humor-Sans.ttf"]),
    ("../Resources", [r"includes/jquery-1.11.1.min.js"]),
    ("../Resources", [r"includes/Machines"]),
    ("../Resources", [r"includes/Themes"]),
    ("../Resources", [r"includes/Icons"]),
  ]

if os.environ['ARTISAN_LEGACY_BUILD'] == "true":
    # we remove Qt components that are not available on legacy Qt installations
    DATA_FILES = [e for e in DATA_FILES if not "qt_plugins/styles" in e[0] and not "qt_plugins/platformthemes" in e[0]]

with open('Info.plist', 'r+b') as fp:
    plist = plistlib.load(fp)
    plist['CFBundleDisplayName'] = 'Artisan'
    plist['CFBundleGetInfoString'] = 'Artisan, Roast Logger'
    plist['CFBundleIdentifier'] = 'org.artisan-scope.artisan'
    plist['CFBundleShortVersionString'] = VERSION
    plist['CFBundleVersion'] = 'Artisan ' + VERSION
    plist['LSMinimumSystemVersion'] = os.environ['MACOSX_DEPLOYMENT_TARGET']
    plist['LSMultipleInstancesProhibited'] = 'false'
    plist['LSPrefersPPC'] = False,
    plist['LSArchitecturePriority'] = 'x86_64',
    plist['NSHumanReadableCopyright'] = LICENSE
    plist['NSHighResolutionCapable'] = True
    fp.seek(0, os.SEEK_SET)
    fp.truncate()
    plistlib.dump(plist, fp)

OPTIONS = {
    'strip': True,
#    'xref': True,
    'argv_emulation': False, # this would confuses GUI processing
# this does not work on Python3.4/PyQt5 for unknown reasons (seems only work for Qt4)
#    'qt_plugins': [
#                    'iconengines/libqsvgicon.dylib',
#                    'imageformats/libqsvg.dylib',
#                    'imageformats/libqjpeg.dylib',
#                    'imageformats/libqgif.dylib',
#                    'imageformats/libqtiff.dylib',
#                    'platforms/libqcocoa.dylib',  # qt5
#                    'platforms/libqminimal.dylib',  # qt5
#                    'platforms/libqoffscreen.dylib'],  # qt5
    'semi_standalone': False,
    'site_packages': True,
# this seems not to work
#    'dylib_excludes': ['phonon','QtDeclarative','QtDesigner',
#                    'QtHelp','QtMultimedia',
#                    'QtOpenGL','QtScript','QtScriptTools',
#                    'QtSql','QtTest','QtXmlPatterns','QtWebKit'],
    'packages': ['yoctopuce','gevent','openpyxl','numpy','scipy','certifi'],
    'optimize':  1,
    'compressed': True,
    'iconfile': 'artisan.icns',
    'arch': 'x86_64',
    'matplotlib_backends': '-', # '-' for imported or explicit 'qt5agg'
    'includes': ['serial',
                 'PyQt5',
                 'PyQt5.QtCore',
                 'PyQt5.QtGui',
                 'PyQt5.QtWidgets',
                 'PyQt5.QtSvg',
                 'PyQt5.QtDBus',
                 'PyQt5.QtNetwork',
                 'PyQt5.QtPrintSupport',
                 'PyQt5.QtBluetooth',
                 'PyQt5.QtConcurrent',
                 ],
    'excludes' :  ['tkinter','curses', # 'sqlite3',
                ],
    'plist'    : plist}

setup(
    name='Artisan',
    version=VERSION,
    author='YOUcouldbeTOO',
    author_email='zaub.ERASE.org@yahoo.com',
    license=LICENSE,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

            
subprocess.check_call(r'cp README.txt dist',shell = True)
subprocess.check_call(r'cp ../LICENSE dist/LICENSE.txt',shell = True)
subprocess.check_call(r'mkdir dist/Wheels',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Cupping',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Other',shell = True)
subprocess.check_call(r'mkdir dist/Wheels/Roasting',shell = True)
subprocess.check_call(r'cp Wheels/Cupping/* dist/Wheels/Cupping',shell = True)
subprocess.check_call(r'cp Wheels/Other/* dist/Wheels/Other',shell = True)
subprocess.check_call(r'cp Wheels/Roasting/* dist/Wheels/Roasting',shell = True)
os.chdir('./dist')

try:
    PYTHONPATH = os.environ["PYTHONPATH"] + r'/'
except:
    PYTHONPATH = r'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/'

try:
    PYTHON_V = os.environ["PYTHON_V"]
except:
    PYTHON_V = '3.7'
    
# (independent) matplotlib (installed via pip) shared libs are not copied by py2app (both cp are needed!)
subprocess.check_call(r'mkdir Artisan.app/Contents/Resources/lib/python' + PYTHON_V + '/lib-dynload/matplotlib/.dylibs',shell = True)
subprocess.check_call(r'cp -R ' + PYTHONPATH + r'site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Resources/lib/python' + PYTHON_V + '/lib-dynload/matplotlib/.dylibs',shell = True)
subprocess.check_call(r'cp ' + PYTHONPATH + r'site-packages/matplotlib/.dylibs/* Artisan.app/Contents/Frameworks',shell = True)

# copy snap7 dylib (we try both directories)
try:
    subprocess.check_call(r'cp -f /usr/local/lib/libsnap7.dylib Artisan.app/Contents/Frameworks/libsnap7.dylib',shell = True)
except:
    subprocess.check_call(r'cp -f /usr/lib/libsnap7.dylib Artisan.app/Contents/Frameworks/libsnap7.dylib',shell = True)

# add localization stubs to make OS X translate the systems menu item and native dialogs
for lang in ['ar', 'de','el','en','es','fa','fi','fr','he','hu','id','it','ja','ko','nl','no','pl','pt_BR','pt','ru','sv','th','tr','zh_CN','zh_TW']:
    loc_dir = r'Artisan.app/Contents/Resources/' + lang + r'.lproj'
    subprocess.check_call(r'mkdir ' + loc_dir,shell = True)
    subprocess.check_call(r'touch ' + loc_dir + r'/Localizable.string',shell = True)



# copy brew installed libusb (note the slight name change of the dylib!)
    # cannot be run brew as root thus the folllowing does not work
    # subprocess.check_call(r'cp $(brew list libusb | grep libusb-1.0.0.dylib) Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
try:
    subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.22/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
except Exception as e:
    subprocess.check_call(r'cp /usr/local/Cellar/libusb/1.0.21/lib/libusb-1.0.0.dylib Artisan.app/Contents/Frameworks/libusb-1.0.dylib',shell = True)
    

            
# for Qt5
print('*** Removing unused Qt frameworks ***')
Qt_frameworks = [
    'QtCore.framework',
    'QtGui.framework',
    'QtWidgets.framework',
    'QtSvg.framework',
    'QtPrintSupport.framework',
    'QtNetwork.framework',
    'QtDBus.framework',
    'QtBluetooth.framework',
    'QtConcurrent.framework'
]
for root,dirs,files in os.walk('./Artisan.app/Contents/Frameworks/'):
    for d in dirs:
        if d.startswith("Qt") and d.endswith(".framework") and d not in Qt_frameworks:
#            print("dir",os.path.join(root,d))
            subprocess.check_call("rm -rf " + os.path.join(root,d),shell = True)

# remove doublicate Qt installation

subprocess.check_call("rm -rf ./Artisan.app/Contents/Resources/lib/python3.7/PyQt5/Qt",shell = True)
                        

print('*** Removing unused files ***')
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'debug' in file:
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.startswith('test_'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.pyc') and file != "site.pyc" and os.path.isfile(os.path.join(root,file[:-3] + 'pyo')):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        # remove also all .h .in .cpp .cc .html files 
        elif file.endswith('.h') and file != "pyconfig.h":
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.in'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cpp'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
        elif file.endswith('.cc'):
#            print('Deleting', file)
            os.remove(os.path.join(root,file))
# .afm files should not be removed as without matplotlib will fail on startup            
#        elif file.endswith('.afm'):
#            print('Deleting', file)
#            os.remove(os.path.join(root,file))
    # remove test files        
    for dir in dirs:
        if 'tests' in dir:
            for r,d,f in os.walk(os.path.join(root,dir)):
                for fl in f:
#                    print('Deleting', os.path.join(r,fl))
                    os.remove(os.path.join(r,fl))                
            
os.chdir('..')
if os.environ['ARTISAN_LEGACY_BUILD'] == "true":
    subprocess.check_call(r"rm -f artisan-mac-" + VERSION + r"-legacy.dmg",shell = True)
    subprocess.check_call(r'hdiutil create artisan-mac-' + VERSION + r'-legacy.dmg -volname "artisan legacy" -fs HFS+ -srcfolder "dist"',shell = True)
else:
    subprocess.check_call(r"rm -f artisan-mac-" + VERSION + r".dmg",shell = True)
    subprocess.check_call(r'hdiutil create artisan-mac-' + VERSION + r'.dmg -volname "artisan" -fs HFS+ -srcfolder "dist"',shell = True)
# otool -L dist/Artisan.app/Contents/MacOS/Artisan
#