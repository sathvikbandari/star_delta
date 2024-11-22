import streamlit as st

def STAR_DELTA(R1, R2, R3):
    R_total = R1 * R2 + R2 * R3 + R3 * R1
    R12 = R_total / R3
    R23 = R_total / R1
    R31 = R_total / R2
    return R12, R23, R31


st.title("2205A21004-PS4")

st.write("Calculate the resistance values of the delta connection networks for the given star connection network having resistance R1,R2,R3.")

R1 = st.number_input("Resistance R1 (Ω):",value=1)
R2 = st.number_input("Resistance R2 (Ω):",value=1)
R3 = st.number_input("Resistance R3 (Ω):",value=1)

if st.button("Calculate"):
    R12, R23, R31 = STAR_DELTA(R1, R2, R3)
    st.write(f"Delta Resistances:")
    st.write(f"R12 = {R12:.2f} Ω")
    st.write(f"R23 = {R23:.2f} Ω")
    st.write(f"R31 = {R31:.2f} Ω")