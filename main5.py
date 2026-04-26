import streamlit as st

st.title("📖 LOGIN")
st.balloons()
st.snow()

user = st.text_input('Username:')
password = st.text_input('Password:', type='password')
btnLogin = st.button("LOGIN")
if btnLogin == True:
    if user == 'admin' and password == '123456':
        print("LOGIN SUCCESSFULY!")
    else:
        print("LOGIN FAIL")

# Tạo 1 text input: copy 1 đoạn văn bất kỳ.
# Khi click button "ĐẾM" đếm xem đoạn văn chúng ta copy vào có bao nhieu từ.
