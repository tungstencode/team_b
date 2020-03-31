## Requirements 

Install python3 : https://www.python.org/


# First run:

Install requirements

```bash
python3 -m pip install --user --upgrade pip
py -m pip install --user virtualenv
```

Create env

```bash
py -m venv env
```

Activate env

```bash
.\env\Scripts\activate.bat
```

Install requirements

```bash
pip3 install -r requirements.txt
```

# To Run:

 * Open 2 terminals
 * Activate python enviorment in both of them with ".\env\Scripts\activate.bat"
 * In one terminal run python backend/start.py
 * In the other run python frontend/start.py


# Useful commands

Activate env

```bash
.\env\Scripts\activate.bat
```

To deactivate:

```bash
 .\env\Scripts\deactivate.bat
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
