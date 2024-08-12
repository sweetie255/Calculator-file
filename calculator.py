import streamlit as st
import add
import subtract
import multiply
import divide

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Dropdown for operator selection
operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/"])

# Perform the calculation based on the selected operator
if operator == '+':
    result = add.add(num1, num2)
elif operator == '-':
    result = subtract.subtract(num1, num2)
elif operator == '*':
    result = multiply.multiply(num1, num2)
elif operator == '/':
    result = divide.divide(num1, num2)

# Display the result
st.write(f"The result is: {result}")

# Option to quit
if st.button("Quit"):
    st.stop()