#!/usr/bin/python3

from sys import argv
import configparser

color_name = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def hex_color(color):
    c = color.split(',')
    for i in range(0, 3):
        c[i] = int(c[i])
    return f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}'


def kitty_color(section, param):
    col = hex_color(config[section]['color'])
    return f'{param}\t{col}'


if len(argv) == 1:
    csname = "Breeze.colorscheme"
else:
    csname = argv[1]

config = configparser.ConfigParser()
config.read(csname)

print(f"# --- {config['General']['Description']} color scheme ---\n")

print(kitty_color('Foreground', 'foreground'))
print(kitty_color('Background', 'background'))
print('')

for c in range(0, 8):
    print(kitty_color(f'Color{c}', f'color{c}'))
    print(kitty_color(f'Color{c}Intense', f'color{c + 8}'))
    print(f'#: {color_name[c]}\n')

print(f"# --- End of {config['General']['Description']} color scheme ---\n")
