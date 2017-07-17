# Zendesk-Coding-Challenge-2017

Zendesk 2017 Coding Challenge for Melbourne Internship
**NOTE**: It is highly recommended that you use Windows 10 for running and testing this app. Even though installation and setup instructions for Ubuntu 16.04 and Mac OSX have been provided, this app hasn't been run there, so it may still have an issue. Windows 10 is the recommended OS for using this app for now.

## Installation & Set-up Instructions
This app has been written in Python 3.6.0. It has only been tested to run on Windows 10. The following are the installation instructions of Python 3.6.0 on Windows (hopefully all versions, but it is preferred to use Windows 10), Ubuntu 16.04 and Mac OSX. Each of these installations come with **pip** installation by default.

### Windows 10 Installation
To install Python 3.6.0, head to https://www.python.org/downloads/release/python-360/ and download the file which says "Windows x86-64 executable installer". After downloading, run the executable and follow the instrcutions to get a full installation of Python 3.6.0 on your system.

### Ubuntu 16.04 Installation
For installing Python 3.6.0 on Ubuntu 16.04, run the following commands in terminal successively. It may ask you for admin password the first time:
```shell
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-getupdate
sudo apt install python3.6
```
### Mac OSX Installation
For installing Python 3.6.0 on Mac, head to https://www.python.org/downloads/mac-osx/ and under "Python 3.6.0 - 2016-12-13" click on "Download Mac OS X 64-bit/32-bit installer" and download the one suitable for your machine.

## Dependencies/Libraries used
This app uses some standard libraries which should come by default with a complete installation of Python 3.6.0 as shown above. The libraries used are:

- **sys** (For exiting, using application packages etc.)
- **requests** (for API access and response)
- **mock, unittest** (for testing)
- **json** (for loading JSON data from file)
- **datetime** (for formatting dates)
- **math** (for rounding up page numbers)

Out of these, sys, json, math and unittest are built-in and don't require separate installation (If you try installing, you should get an error).
For the the rest, they can be installed as follows on Windows 10, Ubuntu 16.04 and Mac OSX:

#### Windows 10:
On command line, type:
```shell
pip install mock
pip install datetime
pip install requests
```
#### Ubuntu 16.04:
You might need to use pip3. In case it is not installed, install it using:
```shell
sudo apt-get update
sudo apt-get install python3-pip
```
OR
```shell
sudo apt-get install python3-setuptools
sudo easy_install3 pip
```
Now for installing libraries/modules (may ask for password first time):
```shell 
sudo pip3 install mock
sudo pip3 install datetime
sudo pip3 install requests
```

#### Mac OSX:
```shell
pip3 install mock
pip3 install datetime
pip3 install requests
```

# Usage
To start using this app, download the git repository or the zip file. Open terminal/command line and go in the "controller" directory of this app. Then type:
For Windows:
```shell
python appController.py
```
For Ubuntu/Mac OSX:
```shell
python3 appController.py
```

# Testing
For testing this app, go to the "tests" directory within the app on command line/terminal. Then type:
For Windows:
```shell
python testTicketViewer.py -b
```
For Ubuntu/Mac OSX:
```shell
python3 testTicketViewer.py -b
```

# To improve:
- Test file class division
- comments, renaming of methods and code readability and unserstandability
- Readme instructions including usage, system requirements, dependencies, pictures etc.
- Checking any irrelevant/redundant code and thorough error handling checking
- Making sure spaces and indents don't create errors
- Simple and easy to understand usage and setup instructions
    
