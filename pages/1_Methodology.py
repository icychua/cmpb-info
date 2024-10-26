import streamlit as st  


st.set_page_config(page_title="Methodology")
st.title("Methodology")

st.write('''
Information were all taken from the CMPB website: https://cmpb.gov.sg''')

expand = st.expander("AMA about CMPB")
expand.markdown("""
- Information was retrieved from the various CMPB websites about pre-enlistee info
- The context was fed to the LLM
- Process user queries using only the context provided.
""")

expand2 = st.expander("Vocation chooser")
expand2.markdown("""
- Information was retrieved from the vocation details handbook, found at https://www.cmpb.gov.sg/ns-vocations/
- Vocation details were processed into csv
- Then fed into LLM 
- User descriptions were then used to assess their vocation suitability.""")