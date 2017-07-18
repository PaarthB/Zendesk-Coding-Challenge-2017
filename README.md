# Zendesk-Coding-Challenge-2017 :shipit:

Zendesk 2017 Coding Challenge for Melbourne Internship<br /><br />
**NOTE**: This app has been tested to work on 64-bit: **Windows 10**, **Mac OS X 10.11 El Capitan** and **Linux Ubuntu 16.04 LTS Xenial Xerus**. It is recommended to run this app on one of these OS, since any other OS would mean you'd have to find out its own installation and usage instructions, which would be time consuming and would need trial-error.

## Application Architecture/Design Explanation:
![Image](/deps.gif?raw=true "MVC Patter Passive View")<br />
This Application uses a variation of MVC and MVP. As with these the UI is split between a view that handles display and a controller that responds to user gestures. The significant change with Passive View is that the view is made completely passive and is no longer responsible for updating itself from the model. As a result all of the view logic is in the controller and no dependencies in either direction between the view and the model. <br />For more info, read https://martinfowler.com/eaaDev/PassiveScreen.html.

## Installation & Set-up
This app has been written in Python 3.6.0. The following are the installation instructions of Python 3.6.0 on 64-bit: Windows 10, Ubuntu 16.04 and Mac OS X 10.11 El Capitan. Each of these installations come with **pip**/**pip3** installation by default.

### Python 3.6.0 Installation:

#### Mac OS X 10.11 El Capitan:
For installing Python 3.6.0 on Mac, head to https://www.python.org/downloads/mac-osx/ and under **"Python 3.6.0 - 2016-12-13"** click on **"Download Mac OS X 64-bit/32-bit installer"** and download the one suitable for your machine.

#### Windows 10:
To install Python 3.6.0, head to https://www.python.org/downloads/release/python-360/ and download the file which says **"Windows x86-64 executable installer"**. After downloading, run the executable and chose **Add Python 3.6 to PATH** option. Then follow the instrcutions to get a full installation of Python 3.6.0 on your system.

#### Ubuntu 16.04:
For installing Python 3.6.0 on Ubuntu 16.04, run the following commands in terminal successively. It may ask you for admin password the first time:
```shell
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-getupdate
sudo apt install python3.6
```

## Installation of Libraries/Modules used
This app uses some standard libraries which should come by default with a complete installation of Python 3.6.0 as shown above. The libraries used are:

- **sys** (For exiting, using application packages etc.)
- **requests** (for API access and response)
- **mock, unittest** (for testing)
- **json** (for loading JSON data from file)
- **datetime** (for formatting dates)
- **math** (for rounding up page numbers)

Out of these, **sys**, **json**, **math** and **unittest** are built-in and don't require separate installation (If you try installing, you should get an error).
For the the rest, they can be installed as follows on and Mac OS X 10.11, Windows 10, Ubuntu 16.04 LTS:

#### Mac OS X 10.11 El Capitan:
```shell
pip3 install mock
pip3 install datetime
pip3 install requests
```
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

## Application Usage:
To start using this app, download the git repository or the zip file. Open terminal/command line and go in the **controller** folder of this app through **cd** commands. Then type:<br /><br />
**For Mac OS X 10.11 El Capitan & Ubuntu 16.04:**
```shell
python3 appController.py
```
**For Windows 10:**
```shell
python appController.py
```
You should see the following screen:
```shell
-------------------WELCOME TO ZENDESK TICKET VIEWER---------------------
This application lets you view tickets and their details on your zendesk account
Please enter a command, to view command options, type 'menu': menu
Menu Options:
1 : Display all tickets
2 : Display Single ticket
q : Quit program")
Enter your choice: 
```
## Application Testing:
This app has automated tests within the file **testTicketViewer.py** inside **tests** folder, which are executed at once when the test file is run. For testing this app, go to the **"tests"** folder within the app on command line/terminal by using **cd** commands. Then type:<br /><br />
**For Mac OS X 10.11 El Capitan & Ubuntu 16.04 LTS:**
```shell
python3 testTicketViewer.py -b
```
**For Windows 10:**
```shell
python testTicketViewer.py -b
```
**NOTE:** **"-b"** is used for supressing output/print statements during unit testing.


## To improve:
- [x] Test file class division (Done)
- [ ] comments, renaming of methods and code readability and unserstandability (Left)
- [x] Readme instructions including usage, system requirements, dependencies, pictures etc. (Done)
- [x] Checking any irrelevant/redundant code and thorough error handling checking (Done)
- [x] Making sure spaces and indents don't create errors (Done)
- [x] Simple and easy to understand usage and setup instructions (Done)
