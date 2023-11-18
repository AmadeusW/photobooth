# Setting up Python
`python -m venv env`
`env\Scripts\activate`

# Updating dependencies
On machine that updated: `python -m pip freeze > requirements.txt`
On all other machines: `python -m pip install -r requirements.txt`

# Using the prototype mechanism
`python sketch.py`
Use keys `q w a s d f z x c v o p` to change model variables and update the preview

# Taking and printing the photo directly
`photobooth.takePhoto()`

# Taking and printing the photo on GPIO button press
`python main.py`

# On Raspberry Pi
https://pypi.org/project/opencv-python-headless/
https://pyimagesearch.com/2018/09/19/pip-install-opencv/
`pip install "picamera[array]"`
`source env/bin/activate`

# Hardware
GPIO4 - LED power
GPIO14 - button sense (assumes internal pullup)
also: gnd button ground
also: gnd LED ground

# todo
fix in cups:
  This release addresses a security issue (CVE-2023-32360) which allows
  unauthorized users to fetch documents over local or remote networks.
  Since this is a configuration fix, it might be that it does not reach you if you
  are updating 'cups-daemon' (rather than doing a fresh installation).
  Please double check your /etc/cups/cupsd.conf file, whether it limits the access
  to CUPS-Get-Document with something like the following
  >  <Limit CUPS-Get-Document>
  >    AuthType Default
  >    Require user @OWNER @SYSTEM
  >    Order deny,allow
  >   </Limit>
  (The important line is the 'AuthType Default' in this section)