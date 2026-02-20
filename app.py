import streamlit as st
from tax_rules import calculate_net_salary
import pandas as pd

st.set_page_config(page_title="Calcolatore Stipendio Netto", layout="centered")
st.title("💰 Calcolatore Stipendio Netto - CCNL Metalmeccanici")

st.write(
    "Inserisci il tuo stipendio lordo annuale e premi 'Calcola stipendio netto'. "
    "Si tratta di una simulazione semplificata per un lavoratore dipendente a tempo indeterminato a Milano."
)

# Input RAL
gross_salary = st.number_input("Stipendio lordo annuale (€)", min_value=0.0, step=1000.0)

# Input numero di mensilità
months = st.number_input("Numero di mensilità", min_value=12, max_value=14, value=13, step=1)

# Input regione per addizionale regionale - imporre che sia fra le regioni del CSV
df_regioni = pd.read_csv("data/addreg2026.csv", sep=';')
regioni_disponibili = df_regioni['REGIONE'].unique().tolist()
regioni_disponibili = [r[8:] for r in regioni_disponibili]
regione = st.selectbox("Regione", options=regioni_disponibili)

# Input comune per addizonale comunale - imporre che sia fra i comuni del CSV
# df_comuni = pd.read_csv("data/addizionale_comunale_2025.csv")
# comuni_disponibili = df_comuni['COMUNE'].unique().tolist()
# comune = st.selectbox("Comune", options=comuni_disponibili)

# Switch mensile/annuale
if st.checkbox("Mostra valori mensili"):
    factor = months
    st.subheader("💵 Risultati mensili")
else:
    factor = 1
    st.subheader("💵 Risultati annuali")

# Bottone per calcolo
if st.button("Calcola stipendio netto"):
    result = calculate_net_salary(gross_salary, regione)

    st.metric("Stipendio netto", f"{result['net']/factor:,.2f} €")
    st.write(f"Contributi INPS: {result['inps']/factor:,.2f} €")
    st.write(f"IRPEF lorda: {result['irpef']/factor:,.2f} €")
    st.write(f"Detrazioni: {result['detrazioni']/factor:,.2f} €")
    st.write(f"Addizionale regionale: {result['addizionale_regionale']/factor:,.2f} €")
    st.caption("⚠️ L'addizionale regionale è calcolata in base al reddito dell'anno precedente.")

st.caption("⚠️ Simulazione semplificata a scopo dimostrativo. Non sostituisce un calcolo fiscale ufficiale.")
