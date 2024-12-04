import streamlit as st
 
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
# sidebar
import streamlit as st
st.sidebar.markdown("This is the sidebar content")
st.sidebar.title("DDRS")
st.sidebar.button("click")
st.sidebar.radio("Pick your team",["TSP","S4F","EY","CU"])
 
container = st.container()
container.write("This is written inside the container")
 
st.write("This is written outside the container") 