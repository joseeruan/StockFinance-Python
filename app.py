import streamlit as st
from plot.interactive import plot_line_i

st.title('Stock Price APP :sunglasses:')

# Sidebar
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Escolha um ativo: (e.g., AAPL):', 'AAPL')


#Plot
fig = plot_line_i(symbol)
st.plotly_chart(fig)

