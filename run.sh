python3 -m pytest --alluredir ./reports
allure generate -c ./reports
allure serve ./reports