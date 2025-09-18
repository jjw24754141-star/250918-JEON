import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.set_page_config(layout="centered", page_title="간단 곱셈 계산기")

st.title("간단 곱셈 계산기 ✖️")
st.write("두 숫자를 입력하면 곱셈 결과를 계산해 드립니다.")

# 첫 번째 숫자 입력 받기
num1 = st.number_input("첫 번째 숫자를 입력하세요:", value=0, step=1)

# 두 번째 숫자 입력 받기
num2 = st.number_input("두 번째 숫자를 입력하세요:", value=0, step=1)

# 곱셈 결과 계산
result = num1 * num2

st.markdown("---") # 구분선

# 결과 표시
st.subheader("계산 결과:")
st.success(f"**{num1}** 곱하기 **{num2}** 는 **{result}** 입니다.")

if st.button("초기화"):
    st.experimental_rerun() # 앱을 다시 실행하여 초기화합니다.