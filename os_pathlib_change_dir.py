import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
os.chdir('C:/Users/User/PycharmProjects/pythonProject')
print(os.getcwd())
print(Path.cwd())