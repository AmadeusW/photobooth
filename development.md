# Setting up Python
`python -m venv env`
`env\Scripts\activate`

# Updating dependencies
On machine that updated: `python -m pip freeze > requirements.txt`
On all other machines: `python -m pip install -r requirements.txt`

# Using the prototype mechanism
`python sketch.py`
Use keys `q w a s d f z x c v o p` to change model variables and update the preview

# Using the main photobooth
`python main.py`

# Todo
Let model be either a simple dictionary or dictionary of Data (tweakable as prototype)
