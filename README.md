# All steps needed to run automation test
* <em>install Python</em> (3.9 recommended version) ([Python 3.9 dowload link](https://www.python.org/downloads/release/python-390/ "Python 3.9 download"))
* add Python/Scripts folder to environment variables
* install all modules (pip3.9.exe install requirements.txt)
* (optional) install selenium webdriver ([Selenium webdriver link](https://selenium-python.readthedocs.io/installation.html#drivers "Selenium driver"))

* <em>in the configuration.py file (features/configuration.py) add path to the drivers (drivers downloaded in the step 4) or set configuration/automatic_download_driver value on True.</em>
* <em> open terminal in the test_m_project folder and run command (<b>behave features/cart_verification.feature</b>). It will run all tests related to cart form </em>
* <em> if we want to generate the allure report we should run two commands (from test_m_project folder) <b> behave -f allure_behave.formatter:AllureFormatter -o features/reports/ -f pretty features/cart_verification.feature </b> (json files will be generated in the reports folder) and then to generate file we need to run <b> allure serve features/reports/ </b></em> 