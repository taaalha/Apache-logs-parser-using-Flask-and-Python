Apache logs parser: Web GUI/UI to extract logs | Made with Flask, Python3
===================================================================

This is a simple application that parses Apache log files through filters, and displays it on a UI. 

A user can upload any .txt log file. The parser would **extract** all the available ip's from the file, count 
the number of times that ip is repeated in the logs, and display that number alongside the ip on a simple UI. 

A sample log file is included with the code. It is recommended to use that for testing purposes. 

Usage
----------
1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository.
3. cd into repository.
4. Activate virtualenv: ``pipenv shell``
5. Download flask: ``pip install flask``
6. Run ``python3 parser_app.py``
7. Go to the displayed local host address to access the application 
 .. image:: ./screenshots/app_running.PNG
    :width: 800




