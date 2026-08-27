#working with numbers
from pyscript import display, document

def addition(e): 
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} & {second_number} is {sum}', target='result')

def subtraction(e): 
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number
    
    display(f'The difference of {first_number} & {second_number} is {difference}', target='result')

def multiplication(e): 
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number
    
    display(f'The product of {first_number} & {second_number} is {product}', target='result')

def division(e): 
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotent = first_number / second_number
    
    display(f'The quotent of {first_number} & {second_number} is {quotent}', target='result')