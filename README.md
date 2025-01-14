# WORK IN PROGRESS

In its current state, this `README.md` is a work in progress and the template is non-functional.

# PyQt Template

### Project Template
```
00 PyQt5-template/
01 ├── app/
02 │   ├── utils/
03 │   │   ├── __init__.py
04 │   │   ├── settings.py
05 │   │   └── tools.py
06 │   ├── widgets/
07 │   │   ├── __init__.py
08 │   │   └── menu.py
09 │   ├── __init__.py
10 │   └── widget.py
11 ├── resources/
12 │   ├── icons/
13 │   │   └── icon.png
14 │   └── fonts/
15 │       └── font.ttf
16 ├── .gitignore
17 ├── LICENSE
18 ├── main.py
19 ├── README.md
20 └── requirements.txt
```

# Miscellaneous
- Add logging
- Without `Qt Designer`
- `app` at line `01` is a top-level package
- Settings are initialised early, and therefore accessable by any future modules
- Extensible
- Modular
- You can find `PyQt5` on `PyPi` via this [link](https://pypi.org/project/PyQt5/)