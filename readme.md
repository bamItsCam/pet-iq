# Setup
distilled from https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

## Windows Setup
1. Download python 3.6
2. Download/confirm you have pip
```bash
py -m pip install --upgrade pip
py -m pip --version
```
3. Install virtualenv
```bash
py -m pip install --user virtualenv
```
4. Create a virtualenv (/api is where our python flask stuff will be)
```bash
cd api && py -m virtualenv env
```
5. Using the virtualenv
    - To activate
    ```bash
    .\env\Scripts\activate
    ```
    - to deactivate
    ```bash
    deactivate
    ```

## Linux Setup (the correct OS)
1. Download python 3.6 (you probably already have it)
2. Download/confirm you have pip
```bash
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```
3. Install virtualenv
```bash
python3 -m pip install --user virtualenv
```
4. Create a virtualenv (/api is where our python flask stuff will be)
```bash
cd api && python3 -m virtualenv env
```
5. Using the virtualenv
    - To activate
    ```bash
    source env/bin/activate
    ```
    - to deactivate
    ```bash
    deactivate
    ```

## TempleOS (jk)

# Developing

1. Activate your virtualenv
    * Windows
    ```bash
    cd api && .\env\Scripts\activate
    ```
    * Linux
    ```bash
    cd api && source env/bin/activate
    ```
2. In your virtualenv:
    1. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
    2. If you've added reqs, you can either manually add your deps to the requirements.txt file, or "freeze" your current env into the file:
    ```bash
    pip freeze > requirements.txt
    ```
3. Run the server
```bash
python api.py
```
4. Profit
