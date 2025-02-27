import streamlit as st
from pymatgen.core.composition import Composition

# Title and description
st.title("Molecular Mass Calculator")
st.write("Welcome to the app! Enter your chemical formula below.")

# Input field for chemical formula
formula = st.text_input("Enter molecular formula (e.g., H2O, CO2, C6H12O6):")

# Function to calculate molecular mass
def calculate_mass(formula):
    try:
        comp = Composition(formula)
        return comp.weight
    except Exception as e:
        return f"Error: {e}"

# Button to trigger calculation
if st.button("Calculate Molecular Mass"):
    if formula:
        mass = calculate_mass(formula)
        st.write(f"*Molecular Mass:* {mass} g/mol")
    else:
        st.write("⚠ Please enter a valid chemical formula.")