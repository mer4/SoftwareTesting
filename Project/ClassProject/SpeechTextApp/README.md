Download repo 

Front End

    1. Open Terminal
    2. cd to Project root (ClassProject folder)
    3. node server.js (to start server in localhost:8081) 

Back End

    1. Install python 3.7.0
    2. sudo pip3 install virtualenv or sudo python3 -m install virtualenv
    3. cd into Project and run command source bin/activate
    4. python manage.py runserver (to start server in localhost:8080) 


    The folder hierarchy looks like

   ClassProject/
    ├── bin/
    ├── include/  
    ├── lib/
    ├── ClassProject/
    |   ├── Server/ (BackEnd Development)
    |   |   ├── config/     
    │   |   |   ├── __init__.py
    │   |   |   ├── settings.py
    │   |   |   ├── urls.py
    │   |   |   └── wsgi.py
    |   |   ├── __init__.py
    |   |   ├── manage.py
    |   |   └── url.py 
    |   ├── SpeechTextApp/ (FrontEnd Development)   
    |   |   ├── public/
    |   |   |   ├── components/
    |   |   |   |    ├── controllers/ (Javascript controllers files)
    |   |   |   |    |    ├── login.control.js
    |   |   |   |    ├── services/
    |   |   |   |    ├── templates /(HTML Views)
    |   |   |   |    |    ├── login.template.html
    |   |   |   ├── app.js (Angular Application definition)
    |   |   |   ├── appRoute.js (Angular Routes)
    |   |   ├── bower.json
    |   |   ├── package.json
    |   |   ├── server.js (To Start Node server)
    |   |   ├── README.me
    |   |   ├── node_modules/
    |   |   ├── bower_components


The front end will work on the SpeecTextApp folder
The back end will work on the Server folder