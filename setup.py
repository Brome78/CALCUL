
from cx_Freeze import setup, Executable
base = None
executables = [Executable("CALCUL.py", base=base, icon="icone.ico")]

packages = ["tkinter", "tkinter.messagebox", "math"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "Calcul",
    author = "Brome78",
    options = options,
    version = "1",
    description = 'Programme de calcul',
    executables = executables,
    icon = "icone de l'app"
)