import streamlit as st

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🦾",
)

# 컬럼을 사용하여 중앙 정렬
col1, col2, col3 = st.columns([1, 2, 3])

with col2:
    st.markdown(
        '''
        # Hello!
                    
        Welcome to my FullstackGPT Portfolio!
                    
        Here are the apps I made:
                    
        - [ ] [DocumentGPT](/DocumentGPT)
        - [ ] [PrivateGPT](/PrivateGPT)
        - [ ] [QuizGPT](/QuizGPT)
        - [ ] [SiteGPT](/SiteGPT)
        - [ ] [MeetingGPT](/MeetingGPT)
        - [ ] [InvestorGPT](/InvestorGPT)
        '''
    )
