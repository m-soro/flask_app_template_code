# Flask App Template 

### My template for future flask apps

---
1. `gh repo clone m-soro/flask_app_template_code`

2. `mv flask_app_template_code <new-name>`

3. `cd <new-name>`

4. `pipenv install flask gunicorn`

5. `pipenv shell`

6. `rm -rf .git ; git init ; git add . ; git commit -m 'initial commit'`

7. `heroku login`

8. `heroku create <unique-app-name> `

9. `git push heroku master`

---

**if:** 
```
error: src refspec master does not match any
error: failed to push some refs to 'https://git.heroku.com/xyzxyzxyz.git'
```

remove git with:

`rm -rf .git`

---

[Deploying Flask App on Heroku - pdf file](https://github.com/m-soro/flask_app_template_code/files/8690169/Deploying.Flask.App.on.Heroku.1.pdf)

---

## To run Selenium in Heroku 

1. **Create main.py with Selenium import**.

```python
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

site = 'https://www.google.com'
driver.get(site) 

print(driver.page_source)

```

2. **In heroku** 

   a. **Create new app**
   
   b. **Settings > Add buildpack**
	    
   1. `python` 
	 2. `https://github.com/heroku/heroku-buildpack-google-chrome`
	 3. `https://github.com/heroku/heroku-buildpack-chromedriver`
	     
   c. **Reveal config vars**
   
	 1. `CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver`
	 2. `GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome`
	
3. **Create requirements.txt**    -->    `pip3 freeze > requirements.txt`

4. **Create Procfile**            -->    `echo web: python main.py > Procfile`

5. **Deploy to heroku**

    a. `git init` 

    b. `git add`

    c. `git commit -m 'initial commit'`	

    d. `git push heroku master`

6. **Run it**                     -->    `heroku run python main.py`

---

Create Postgres Database in Heroku:
* Get credentials

**In command line**

```python
psql --host=ec2-3-228-235-79.compute-1.amazonaws.com --port=5432 --username=nkftbsuouwdqkc --password --dbname=d43rfu8ko95dc9
```

* It will prompt for password, then copy and paste the password from the credentials page

test with `\dt`

**Create Schema**
in new terminal, cd to your project folder `subl projectname.sql`




