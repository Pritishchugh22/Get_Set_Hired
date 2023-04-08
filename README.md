# Get_Set_Hired
- A hiring platoform that is solely oriented towards meeting the needs of startups that face problem in hiring skilled workforce.
- Startups post about their requirement and get a sorted list of students based on their rankings
- Selected student gets to work as a professional in the startup 

## To setup-:

1. First fork this repo and then Clone it
2. Run `cd sms` - to move into the directory 
3. Install virtualenv using command - `pip install virtualenv`
3. Now activate the virtual environment using command - `virtualenv env`
4. Now activate the virtual env using command - `.\env\Scripts\activate` . This will activate the virtual environment. For linux and Mac try - `source env/bin/activate`
5. Install flask - `python -m pip install flask`.
6. Install all requirements by - `pip install -r requirements.txt`.
7. Now to migrate the models run - `python manage.py migrate`.
8. Now to activate the localhost server run - `python -m flask run`<br />

For linux-:<br>
4. `source venv/bin/activate`<br>
6. `pip install -r requirements.txt`<br>
7. `python manage.py runserver`<br>


<pre>
	Runs the app in the development mode.<br />
	Open (http://localhost:8000) to view it in the browser.
</pre>
