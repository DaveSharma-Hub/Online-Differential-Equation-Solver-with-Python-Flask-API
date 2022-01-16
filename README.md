# Online-Differential-Equation-Solver-with-Python-Flask-API
Online differential equation solver inspired by online math programs such as Symbolab, that calculated the differential equation entered by a user, using JS/AJAX , FLASK in Python for the REST API, and Sympy for the actual solving of the differential equation
The user enters the differential equation in a particular for such as y''+y'=1 and the value in the input-box is sent to the python REST API using AJAX in app.js. Then the python
REST API recieves the string value diff. equation to solve, uses a custom parser to organize the equation in a particular way for Sympy to solve the differential equation, and returns
the sovled equation back to app.js which uses AJAX to display the new data of the solved differential equation.

To run the program download all files

Set flask via

```
set FLASK_APP=app.py
  set FLASK_ENV=development
```
run the flask microframework
```
flask run
```
Replace localhost:5000 with the specific IP and Port Number displayed after runnning flask
```
Open index.html live server
```

![Capture2](https://user-images.githubusercontent.com/81478885/149671857-fff9979f-6a5a-4a94-ae80-330c1d900cde.JPG)
![solutionJPG](https://user-images.githubusercontent.com/81478885/149671858-83b89b2e-a08b-4654-957e-dd80031a97a9.JPG)
![Capture3](https://user-images.githubusercontent.com/81478885/149671859-003e41b6-298f-4702-8386-e85b26417322.JPG)
