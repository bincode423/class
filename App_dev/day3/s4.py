import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title='Media Page',
                    page_icon=':tv:',
                    layout='wide')

st.title('Streamlit + Matplotlib')

tab1, tab2, tab3 = st.tabs(['images', 'charts', 'others'])

with tab1:
    st.header('image_gallery')

    uploaded_file = st.file_uploader("Upload images", type=['jpg', 'jpeg', 'png'], accept_multiple_files=False)

    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
        st.success('Image uploaded successfully')
    else:
        st.write('Random Image')
        random_image = np.random.randint(0, 255, (1080, 1080, 3))
        st.image(random_image, caption='Random Image', use_container_width=True)
with tab2:
    st.header("my_charts")
    subjects = st.multiselect("Select a subject", ["Korean", "English", "Math", "Science", "Social", "History"], default=["Korean", "English"])
    scores = {}
    if subjects:
        for subject in subjects:
            score = st.slider(f"Enter scores for {subject}", min_value=0, max_value=100, value=50, step=1)
            scores[subject] = score
    
    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values(), color=["red", "blue", "green", "yellow", "purple", "orange"])
    ax.set_title("Scores")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Score")
    st.pyplot(fig)
with tab3:
    st.header("funny_tools")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("balloon", use_container_width=True):
            st.balloons()
        if st.button("frozen", use_container_width=True):
            st.snow()
    with col2:
        if st.button('loading', use_container_width=True):
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i)
                time.sleep(0.1)
        