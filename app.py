#Author:Dave Sharma
#This web RESTAPI uses FLASK

from sympy import Function, Derivative, dsolve, Eq, sin, cos, tan,symbols, log, sympify
import sympy
import re

def seperateVars(input):
    if "cos" in input:
        array = re.split("cos", input)
        tryOut = ""
        for i in range(len(array[1])):
            if array[1][i] != ')' and array[1][i] != '(':
                tryOut += array[1][i]
        backSide = seperateVars(tryOut)
        frontSide = seperateVars(array[0])
        if frontSide!="":
            return frontSide+"*cos("+backSide+")"
        else:
            return "cos("+backSide+")"
    elif "sin" in input:
        array = re.split("sin", input)
        tryOut = ""
        for i in range(len(array[1])):
            if array[1][i] != ')' and array[1][i] != '(':
                tryOut += array[1][i]
        backSide = seperateVars(tryOut)
        frontSide = seperateVars(array[0])
        if frontSide != "":
            return frontSide+"*sin("+backSide+")"
        else:
            return "sin("+backSide+")"
    elif "tan" in input:
        array = re.split("tan", input)
        tryOut = ""
        for i in range(len(array[1])):
            if array[1][i] != ')' and array[1][i] != '(':
                tryOut += array[1][i]
        backSide = seperateVars(tryOut)
        frontSide = seperateVars(array[0])
        if frontSide != "":
            return frontSide+"*tan("+backSide+")"
        else:
            return "tan("+backSide+")"
   
    elif "x" in input or "y" in input:
        holder=""
        for i in range(len(input)):
           if input[i]=="x" or input[i]=="y":
               if i!=0:
                   holder += "*"+input[i]
               else:
                   holder += input[i]
           else:
               holder+=input[i]
        return holder
    else:
        return input

def countOrder(string):
    count = 0
    for i in range(len(string)):
        if (string[i] == "'"):
            count += 1
    return count


# need to take in an equation, use a parser to search and input correct values then output the correct equation

def differentialSolver(input):
    yD = []

    input = input.replace("-", "+ -")
    # print(input)

    centerLine = 0;
    array = input.split("+")
  

    for i in range(len(array)):
        array[i].replace(" ", "")

    for index in range(len(array)):
        if ("=" in array[index]):
            centerLine = index

    # print(array[centerLine])

    for i in input:
        if (i == 'y'):
            yD.append([0, ""])

    counter = 0
    for i in array:
        if ("y" in i):
            yD[counter][0] = countOrder(i)
            for k in range(len(i)):
                if (i[k] == 'y'):
                    break
                else:
                    yD[counter][1] += i[k]
            counter += 1

    print(yD)

    for i in yD:
        i[1] = i[1].replace(" ", "")
        if (i[1] == ""):
            i[1] = "1"

    equation = ""
    for i in yD:
        if (i[0] > 0):
            if (equation == ""):
                equation += str(seperateVars(i[1])) + "*"
                equation += "Derivative(y(x)"
                for k in range(i[0]):
                    equation += ',x'
                equation += ')'
            else:
                equation += "+" + str(seperateVars(i[1])) + "*"
                equation += "Derivative(y(x)"
                for k in range(i[0]):
                    equation += ',x'
                equation += ')'

   
    rhsEqu = array[centerLine].split("=")

    rhsValue = ""
    firstHolder = ""
    firstOther = ""
    for i in range(len(rhsEqu[1])):
        if (rhsEqu[1][i] != "x" and rhsEqu[1][i] != "y"):
            firstHolder += rhsEqu[1][i]
        else:
            firstOther += rhsEqu[1][i]
    print(firstHolder)
    firstHolder = firstHolder.replace(" ", "")
    firstOther = firstOther.replace(" ", "")
    if (firstOther != ""):
        rhsValue += firstHolder + "*" + firstOther
    else:
        rhsValue += firstHolder
    for latterIndex in range(len(array)):
        if (latterIndex > centerLine):
            holder = ""
            other = ""
            if ("x" in array[latterIndex] or "y" in array[latterIndex]):
                for k in range(len(array[latterIndex])):
                    if (array[latterIndex][k] != "x" and array[latterIndex][k] != "y"):
                        holder += array[latterIndex][k]
                    else:
                        other += array[latterIndex][k]
                if(holder==""):
                    rhsValue += "+ 1*" + other
                else:
                    rhsValue += "+" + holder + "*" + other

            else:
                rhsValue += "+" + array[latterIndex]
                # rhsValue+="+"+array[latterIndex]

    print(rhsValue)

    x = sympy.symbols('x')
    y = sympy.symbols('y', cls=Function)
    print(equation)

    try:
        ode = Eq(sympify(equation), sympify(rhsValue))
        print(equation)
        returnValue = dsolve(ode, y(x)).rhs
        print(equation+"="+rhsValue)
        return returnValue
    except:
        return "Could not Calculate Differential Equation"
   
#FLASK WEB API
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
#Route endpoint as api_website/
@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def result():
    print(request.data.decode("utf-8")) #['diffEquation'])  # should display 'bar'
    holderInput = str(request.data.decode("utf-8"))#['diffEquation']
    solved = differentialSolver(holderInput)
    return str(solved)  # response to your request.

