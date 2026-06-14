# password_generator.py

import streamlit as st
import random
import string

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Trình tạo mật khẩu",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Trình tạo mật khẩu ngẫu nhiên")

st.write("Tạo mật khẩu mạnh và an toàn ngay lập tức")

# -----------------------------
# SETTINGS
# -----------------------------
length = st.slider(
    "Độ dài mật khẩu",
    min_value=4,
    max_value=50,
    value= 12
)

use_uppercase = st.checkbox("Bao gồm chữ cái in hoa", value=True)
use_numbers = st.checkbox("Bao gồm số", value=True)
use_symbols = st.checkbox("Bao gồm ký hiệu", value=True)

# -----------------------------
# CHARACTER POOL
# -----------------------------
characters = string.ascii_lowercase

if use_uppercase:
    characters += string.ascii_uppercase

if use_numbers:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

# -----------------------------
# GENERATE PASSWORD
# -----------------------------
if st.button("Tạo Mật Khẩu"):

    password = "".join(random.choice(characters) for _ in range(length))

    st.success("Mật khẩu đã được tạo")

    st.code(password, language="text")

    # -----------------------------
    # PASSWORD STRENGTH
    # -----------------------------
    strength = 0

    if length >= 8:
        strength += 1

    if use_uppercase:
        strength += 1

    if use_numbers:
        strength += 1

    if use_symbols:
        strength += 1

    # DISPLAY STRENGTH
    if strength == 1:
        st.error("Mật khẩu yếu")
    elif strength == 2:
        st.warning("Mật khẩu vừa phải")
    elif strength == 3:
        st.info("Mật khẩu mạnh")
    else:
        st.success("Mật khẩu rất mạnh")