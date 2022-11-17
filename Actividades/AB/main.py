from utils.data import Tokens, Issues
from utils.menus import menu_inicial

if __name__ == '__main__':
    tokens, issues = Tokens(), Issues()
    while menu_inicial(tokens, issues):
        pass
