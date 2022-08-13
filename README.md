
## Table Extraction

#### Packages
- pandas
- opencv-python
- tk
- [ghostscript](https://www.ghostscript.com/releases/gsdnld.html)
- camelot-py

## Web Automation and Scraping

#### Packages
- [WebDriver](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/)
- selenium
- pyinstaller

#### Generate execuatable

``pyinstaller --onefile news_headlines.py``
`` python -m PyInstaller --onefile news_headlines.py``

#### Schedule Python script

##### Unix
1. ``crontab -e``
- [cron expression generator](https://crontab.guru/)
2. ``cron expression <file path>``
3. ``:wq`` Write and quit to save the crontab script

##### Windows
1. Open Task Scheduler
2. Create a custom tasks folder under Task Scheduler Library
3. Select custom tasks folder
4. Select the Action tab and then Create Basic Task...
5. Give the new tasks a name and description
6. Set the desired trigger frequency
7. Set the action to Start a program
8. Set the executable path with no arguments
9. Click finish

## Automate Excel Report
