# Grub 
## Project Setup
### Virtual Environment Setup
    
1. Set `.virtualenvs/` in your home directory, if you don't have one yet.

```
$ mkdir ~/.virtualenvs
```

2. Create a new virtual environment

```
$ python3 -m venv ~/.virtualenvs/grub
```

3. Activate virtual environment

```
$ source ~/.virtualenvs/grub/bin/activate
```

### Test Django Project

4. Clone the repository

```
$ git clone https://github.com/aerielcruz/grub.git
```

5. Change to the project's directory

```
$ cd grub/
```

6. Install the package requirements

```
$ pip install -r requirements.txt
```

7. Run the server (Open the browser: http://127.0.0.1:8000/)

```
$ python manage.py runserver
```
