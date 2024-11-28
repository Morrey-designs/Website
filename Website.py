import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Weekly Budget", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Set the background of the main page */
    .stApp {
        background: linear-gradient(135deg, black, blue);
        color: white;
        font-family: Arial, sans-serif;
    }

    /* Make hyperlinks bigger and more readable */
    a {
        font-size: 20px;
        font-weight: bold;
        color: #FFD700; /* Gold color */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
        color: #FFA500; /* Orange color on hover */
    }

    /* Styling buttons (optional) */
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #4682B4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Design ---
# --- IMPORTANT STUFF ----
with st.container():
    st.subheader("Welcome :wave:")
    st.title("Weekly Budget")
    st.write("Hello Miles")
    st.write("[Learn More >](https://w3schools.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About")
        st.write("##")
        st.write(
            """
            This is just a test and it is not final. There will be major errors or bugs that will occur.
            """
        )
        st.write("##")
        st.write(
            """
            - Looking for karan?

            - Struggling with the big three?

            - Hi Miles

            If this sounds interesting, why don't you buy siomai ni ki for some treat.
            """
        )
        st.write("[Israels house >](https://www.google.com/maps/@10.3001829,123.870742,3a,75y,95.45h,84.11t/data=!3m7!1e1!3m5!1s9SLap29av87H1Z4Ma9uE_Q!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D5.889009597453708%26panoid%3D9SLap29av87H1Z4Ma9uE_Q%26yaw%3D95.4541059061834!7i16384!8i8192?entry=ttu&g_ep=EgoyMDI0MTEyNC4xIKXMDSoASAFQAw%3D%3D)")

# ----PROJECTS----
with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with text_column:
        st.subheader("By using our website you can calculate your daily finance")
        st.write(
            """
            Saba dira Mercado
            """
        )
