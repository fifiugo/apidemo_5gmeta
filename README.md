# Flask RESTplus 5GMeta Demo   🌶
Flask demo project with auto generated Swagger documentation for 5Gmeta. 

## Start Application Instructions

Clone the repo to your local machine by running the command:

```sh
git clone https://github.com/fifiugo/flask5gdemo.git
```

You must have python installed in your machine. The code presented will run in python3. If you want to use python2 and/or are following this procedure in a Windows machine please refer to the instructions presented in the [Flask installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/)

After that, go into the folder with the project and create a virtual environment with the following command:

```sh
python3 -m venv venv
```

Active the the respective environment by running:

```sh
. venv/bin/activate
```

**Note:** It might be important to specify the environment you are considering when running this code in your IDE.


### Documented endpoints

Endpoints created based on the Flask-RESTPlus suggested structure and documentation. All the endpoints previously created are presented with a better structure inside the **blueprints** folder. This is achieved with the usage of [Flask-RESTPlus extension](https://flask-restplus.readthedocs.io/en/stable/) You can check the generated documentation by referring to this link: https://flask-5gmeta.herokuapp.com/api/doc
