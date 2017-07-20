# Zendesk-Coding-Challenge-2017 :shipit:

Zendesk 2017 Coding Challenge for Melbourne Internship<br /><br />
**NOTE**: This app has been tested to work on 64-bit: **Windows 10** and **Mac OS X 10.11 El Capitan**. It is recommended to run this app on one of these OS, since any other OS would mean you'd have to find out its own installation and usage instructions, which would be time consuming and would need trial-error.

## Application Architecture/Design Explanation, MVC-Passive View:
![Image](/deps.gif?raw=true "MVC Patter Passive View")<br />
Unlike most MVC-style configurations, Passive View results in no dependencies between view and model. As with these the UI is split between a view that handles display and a controller that responds to user gestures. The significant change with Passive View is that the view is made completely passive and is no longer responsible for updating itself from the model. Controller handles responses to user events and does all the updating of the view.<br />For more info, read: https://martinfowler.com/eaaDev/PassiveScreen.html.

## Installation & Set-up
This app has been written in Python 3.6.0. The following are the installation instructions of Python 3.6.0 on 64-bit: Windows 10 and Mac OS X 10.11 El Capitan. Each of these installations come with **pip**/**pip3** installation by default.

### Python 3.6.0 Installation:
#### Mac OS X 10.11 El Capitan:
For installing Python 3.6.0 on Mac, head to https://www.python.org/downloads/mac-osx/ and under **"Python 3.6.0 - 2016-12-13"** click on **"Download Mac OS X 64-bit/32-bit installer"** and download the one suitable for your machine.

#### Windows 10:
To install Python 3.6.0, head to https://www.python.org/downloads/release/python-360/ and download the file which says **"Windows x86-64 executable installer"**. After downloading, run the executable and chose **Add Python 3.6 to PATH** option. Then follow the instrcutions to get a full installation of Python 3.6.0 on your system.

### Installation of Libraries/Modules used:

The libraries used are:

- **sys** (For exiting, using application packages etc.)
- **requests** (for API access and response)
- **mock, unittest** (for testing)
- **json** (for loading JSON data from file)
- **datetime** (for formatting dates)
- **math** (for rounding up page numbers)

Out of these, **sys**, **json**, **math** and **unittest** are built-in in a standard Python 3.6.0 installation and don't require separate installation (If you try installing, you should get an error).
For the the rest, they can be installed as follows on Mac OS X 10.11 and Windows 10:

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

## Application Usage:
To start using this app, download the git repository or the zip file. Open terminal/command line and go in the **controller** folder of this app through **cd** commands. Then type:<br /><br />
**For Mac OS X 10.11 El Capitan:**
```shell
python3 appController.py
```
**For Windows 10:**
```shell
python appController.py
```
You should see the following screen:
```
-------------------------WELCOME TO ZENDESK TICKET VIEWER-------------------------
This application lets you view tickets and their details on your zendesk account
Please enter a command, to view command options, type 'menu': menu
Command Options:
Enter 1 - Display all tickets
Enter 2 - Display single ticket
Enter q - Exit application
Enter your choice: 1
```
## Application Testing:
For testing this app, go to the **"tests"** folder within the app on command line/terminal by using **cd** commands. Then type:<br /><br />
**For Mac OS X 10.11 El Capitan:**
```shell
python3 testTicketViewer.py -b
```
**For Windows 10:**
```shell
python testTicketViewer.py -b
```
**NOTE:** **"-b"** is used for supressing output/print statements during unit testing.<br /><br />
You should see a message similar to the following on your CLI Screen:
```
............
----------------------------------------------------------------------
Ran 12 tests in 0.135s

OK
```
<!--
## To improve:
- [x] Test file class division (Done)
- [x] comments, renaming of methods and code readability and unserstandability (Done)
- [x] Readme instructions including usage, system requirements, dependencies, pictures etc. (Done)
- [x] Checking any irrelevant/redundant code and thorough error handling checking (Done)
- [x] Making sure spaces and indents don't create errors (Done)
- [x] Simple and easy to understand usage and setup instructions (Done)
-->
