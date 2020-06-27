## install pip3

```bash
sudo apt-get install python3-pip
```

## yapf command sample

```bash
pip install yapf
python -m yapf -i sample.py
```
## flake8 command sample

```bash
pip install flake8
pip install pep8-naming # flake8 plugin
python -m flake8 sample.py
```

## mypy

```bash
python3 -m pip install -U mypy
python3 -m mypy fizzbuzz.py
```
### wdb

```bash
python3 -m pip install -U wdb
python3 -m pip install -U wdb.server
python3 -m wdb fizzbuzz.py
```

### python-web-pdb

```bash
python3 -m pip install -U web-pdb
python3 fizzbuzz.py
```

