import streamlit as st

st.set_page_config(
    page_title="체육대회선호종목조사",
    page_icon='✔'
)

st.header('TEST')

st.header('석용원님 반갑습니다.')
st.subheader(':red[체육대회] 선호 종목 선택')
st.subheader('2023년 4월 20일 까지 :red[반드시] 제출')
st.markdown('한번 제출된 설문은 수정할 수 없습니다.')
st.sidebar.image('guam.jpg', width=200)
st.sidebar.image('soccer.jpg' , width= 150)
st.sidebar.image('baseball.jpg', width= 150)
st.sidebar.image('basketball.png',width= 150)
title = st.text_input('학년')
subtitle = st.text_input('반')
subtitle = st.text_input('번호')
subtitle = st.text_input('이름')
운동종목 = st.radio( "선호하는 종목은?", ('축구', '야구', '농구'),
                               horizontal=True)
if 운동종목 == '축구':
    st.write('축구를 선택하셨습니다.')
elif 운동종목 == '야구':
    st.write('야구를 선택하셨습니다.')
else:
    st.write('농구를 선택하셨습니다.')
btn = st.button('제출하기')
if btn :
    st.header('제출이 완료되었습니다.')


