import streamlit as st
from functions import quotes , random_image,temp_city,get_news, news_summarizer,smart_plan
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

st.set_page_config(
    page_title="Daily Insight AI Assistant",
    layout="wide",       
    initial_sidebar_state="expanded"
)

st.title("AI Daily Insight Assistant")


tab1,tab2,tab3,tab4 = st.tabs(["Home","Weather", "News by Interest", "Smart Planner"])

with tab1:
    st.title("Thought of the Day")
    st.markdown(quotes())
    st.image(random_image(),width = 400)


with tab2:
    city = st.text_input("Entre the city name")
    button = st.button("Get Weather Detail", type="primary")
    
    if button:
        if city:
            with st.spinner("Fetching the Weather Details"):
                output= temp_city(city)
                st.subheader(f"Weather Info: {output}")
                st.success("Weather Fetched Sucessfully")
        else:
            st.error("Please Entre City Name")

with tab3:
    topic = st.text_input("Entre Topic of Interest")
    button = st.button("Fetch News", type="primary")
    if button:
        if city:
            with st.spinner("Fetching the news"):
                output = get_news(topic)
                titles=[]
                url=[]
                image_url=[]
                for articles in output[:5]:
                    titles.append(articles['title'])
                    url.append(articles['url'])
                    image_url.append(articles['urlToImage'])
                cols = st.columns(len(titles))

                for i, title in enumerate(titles):
                    with cols[i]:
                        st.header(titles[i])
                        st.markdown("---")
                        st.image(image_url[i])
                        st.markdown("---")
                        st.write("Read full article at:", url[i])
                        st.markdown("---")
                        st.header("Summary:")
                        resp = news_summarizer(url[i])
                        st.write(resp)
                if not articles:
                    st.error("No News found")
            

with tab4:
    city_name = st.text_input("Entre City you want to Travel")
    button = st.button("Smart Planner", type="primary")
    if button:
        if city_name:
             with st.spinner("Making your Plan...This will take some time"):
                st.markdown(smart_plan(city_name))
                st.success('Have a nice day')

