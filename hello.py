import streamlit as st

st.title("Cold Call Calculator")

# Layout the input sliders
col1, col2, = st.columns(2)
gross = col1.slider('Select Gross Revenue Desired (in $)', 0, 1000000, 100000)
comm = col2.slider('Select Average Commission (in $)', 0, 5000, 3000)
cctod = col1.slider('Select CC to Demo %', 0, 60, 20)
demotosale = col2.slider('Select Demo to Sale %', 0, 75, 25)

# Calculate the demos.
salesgen = gross/comm
demogen = salesgen/(demotosale/100)
ccreq = demogen/(cctod/100)

single = ccreq/52
double = single/2
triple = single/3

# Display demo results
st.write("### Results")
col1, col2, col3 = st.columns(3)
col3.metric(label="Sales Generated", value=f"{salesgen:,.0f}")
col2.metric(label="Demos Generated", value=f"{demogen:,.0f}")
col1.metric(label="Cold Calls Required", value=f"{ccreq:,.0f}")

# Display demos per salesmen
col1, col2, col3 = st.columns(3)
col1.metric(label="CC/week for 1 salesman", value=f"{single:,.0f}")
col2.metric(label="CC/week for 2 salesmen", value=f"{double:,.0f}")
col3.metric(label="CC/week for 3 salesmen", value=f"{triple:,.0f}")







