import streamlit as st  


st.set_page_config(page_title="Methodology")
st.title("Methodology")

st.write('''
Information were all taken from the CMPB website: https://cmpb.gov.sg''')

with st.expander("AMA about CMPB"):
    st.write("""
- Information was retrieved from the various CMPB websites about pre-enlistee info
- The context was fed to the LLM
- Process user queries using only the context provided.
             """)
    st.image("./cmpb ama methodology.png")

with st.expander("Vocation chooser"):
    st.write("""
- Information was retrieved from the vocation details handbook, found at https://www.cmpb.gov.sg/ns-vocations/
- Vocation details were processed into csv
- Then fed into LLM 
- User descriptions were then used to assess their vocation suitability.
             """)
    st.image("./vocation chooser methodology.png")