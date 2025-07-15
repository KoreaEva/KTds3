import streamlit as st
import random

st.title("숫자 맞추기 게임")
st.write("1부터 100 사이의 임의의 숫자를 맞춰보세요!")

# 세션 상태에 정답 저장
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
if "tries" not in st.session_state:
    st.session_state.tries = 0

guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)
if st.button("제출"):
    st.session_state.tries += 1
    if guess < st.session_state.answer:
        st.write("더 큰 숫자입니다!")
    elif guess > st.session_state.answer:
        st.write("더 작은 숫자입니다!")
    else:
        st.success(f"정답입니다! 시도 횟수: {st.session_state.tries}")
        if st.button("다시 시작"):
            st.session_state.answer = random.randint(1, 100)
            st.session_state.tries = 0