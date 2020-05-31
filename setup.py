import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='googlefunirator',
    version='1.0',
    packages=[''],
    url='',
    license='GPLv3',
    author='sergds',
    author_email='sergdser@gmail.com',
    description='A program that translates text many times in many languages',
    options = {"build_exe": build_exe_options},
    executables = [Executable("googfun.py", base=base)])
