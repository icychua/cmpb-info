import streamlit as st  

st.set_page_config(page_title="About")
st.title("About this App")

st.write('''
This is a Streamlit App that helps Singaporean pre-enlistees find out more information.''')

st.write('''It also includes a vocation suggester if you are still unsure about what vocation to choose.''')

st.write('''Navigate on the two tools via the bar on the left!''')

expand = st.expander("DISCLAIMER")
expand.markdown("""

IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.

""")