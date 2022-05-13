# Flask App Template 

A template for future flask apps

[Deploying Flask App on Heroku - pdf file](https://github.com/m-soro/flask_app_template_code/files/8690169/Deploying.Flask.App.on.Heroku.1.pdf)

## Deploying Flask App on Heroku

Create a folder named *“eflask”* and open the command line and cd inside the *“eflask”* directory. 

Follow the following steps to create the sample application for this tutorial.

1.	Create a virtual environment with pipenv and install Flask and Gunicorn .
 
    `$ pipenv install flask gunicorn` 

2.	Create a “Procfile” and write the following code. 
 
    `$ touch Procfile` 
    
      ![Deploying Flask App on Heroku_page2_image1](https://user-images.githubusercontent.com/63247801/168375310-9d90e906-29bd-42a9-bcec-5f85b7afd38d.jpg)


3.	Create “runtime.txt” 

    `$ touch runtime.txt`
    
      ![Deploying Flask App on Heroku_page2_image2](https://user-images.githubusercontent.com/63247801/168375328-3eb727c8-1330-4bf2-9ba8-cc689e3dbd3f.jpg)

and write the following code.

4.	Create a folder named “app” and enter the folder. 

    ```
    $ mkdir app
    $ cd app
    ```

5.	Create a python file, “main.py” 
	
    `$ touch main.py`
  
    and enter the sample code.

    ```
    from flask import Flask
 
    app = Flask(__name__)
 
    @app.route("/")
    def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
    ```

6.	Get back to the previous directory “eflask”.Create a file“wsgi.py” 

    ```
    $ cd ../
    $ touch wsgi.py
    ```

    and insert the following code.

    ```
    from app.main import app
 
    if __name__ == "__main__":
            app.run()
    ```

7.	Run the virtual environment.

    `$ pipenv shell`

8.	Initialize an empty repo, add the files in the repo and commit all the changes.

    ```
    $ git init 
    $ git add .
    $ git commit -m "Initial Commit"
    ```

9.	Login to heroku CLI using 

    `$ heroku login`

Now, Create a unique name for your Web app.
    
    `$ heroku create eflask-app`

10.	Push your code from local to the heroku remote. 
    
    `$ git push heroku master`
