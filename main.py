import streamlit as st

# ✅ Define conversions globally
conversions = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
        "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(category, from_unit, to_unit, value):
    if category == "Temperature":
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            value = value - 273.15
        
        return conversions[category][to_unit](value)

    return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category:
    # ✅ Now, 'conversions' is accessible
    units = list(conversions[category].keys())  
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    
    if st.button("Convert"):
        result = convert_units(category, from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
