import streamlit as st

st.set_page_config(page_title="Quán Cà Phê", page_icon="☕", layout="wide")

# =========================
# HEADER
# =========================
st.write("☕ Chào mừng bạn đến với quán cà phê của chúng tôi!")

st.divider()

# =========================
# CAFE IMAGE
# =========================
st.image(
    "https://phunugioi.com/wp-content/uploads/2021/10/Hinh-anh-quan-cafe-dep-thiet-ke-don-gian-1.jpg",
    width=800,
)

st.divider()

# =========================
# MENU DATA
# =========================
menu = [
    {
        "name": "Cà phê sữa",
        "price": 30000,
        "image": "https://thuytinhluminarc.com/wp-content/uploads/2022/08/hinh-ly-ca-phe-ve-trai-tim-2.jpg",
    },
    {
        "name": "Cà phê đen",
        "price": 25000,
        "image": "https://thf.bing.com/th/id/OIP.GlGuLTt83H3V5DosXBYABQHaHa?o=7&cb=thfc1falcon2rm=3&rs=1&pid=ImgDetMain&o=7&rm=3",
    },
    {
        "name": "Trà đào",
        "price": 35000,
        "image": "https://thf.bing.com/th/id/OIP.gfppbwjX0uHNLkStiqqnnwHaHa?cb=thfc1falcon2&rs=1&pid=ImgDetMain&o=7&rm=3",
    },
    {
        "name": "Trà sữa",
        "price": 40000,
        "image": "https://tse3.mm.bing.net/th/id/OIP.Az5dVIEa770xb_fmCKZA1gHaHa?cb=thfc1falcon2&rs=1&pid=ImgDetMain&o=7&rm=3",
    },
]

st.subheader("📋 Menu")

# =========================
# ORDER SECTION
# =========================
total = 0
orders = []

cols = st.columns(2)

for index, item in enumerate(menu):

    with cols[index % 2]:

        st.image(item["image"],width=500)

        st.markdown(f"## {item['name']}")
        st.write(f"💰 Giá: {item['price']:,} VNĐ")

        quantity = st.number_input(
            f"Số lượng - {item['name']}",
            min_value=0,
            max_value=20,
            step=1,
            key=item["name"],
        )

        sugar = st.selectbox(
            f"Đường - {item['name']}",
            ["Không đường", "Ít đường", "Bình thường", "Nhiều đường"],
            key=f"sugar_{item['name']}",
        )

        topping = st.selectbox(
            f"Thạch - {item['name']}",
            ["Không thạch", "Thạch cà phê"],
            key=f"topping_{item['name']}",
        )

        st.divider()

        if quantity > 0:
            subtotal = quantity * item["price"]
            total += subtotal

            orders.append(
                {
                    "name": item["name"],
                    "quantity": quantity,
                    "price": item["price"],
                    "subtotal": subtotal,
                    "sugar": sugar,
                    "topping": topping,
                }
            )

# =========================
# BILL
# =========================
st.subheader("🧾 Hóa đơn")

if orders:

    bill_text = "========== HÓA ĐƠN ==========\n\n"

    for order in orders:

        st.write(
            f"✅ {order['name']} x{order['quantity']} = {order['subtotal']:,} VNĐ"
        )

        st.write(f"Đường: {order['sugar']}")
        st.write(f"Thạch: {order['topping']}")

        st.divider()

        bill_text += (
            f"{order['name']} x{order['quantity']}\n"
            f"Đường: {order['sugar']}\n"
            f"Thạch: {order['topping']}\n"
            f"Thành tiền: {order['subtotal']:,} VNĐ\n\n"
        )

    st.markdown(f"# Tổng tiền: {total:,} VNĐ")

    bill_text += f"\nTỔNG TIỀN: {total:,} VNĐ"

    # =========================
    # PAY BUTTON
    # =========================
    if st.button("💳 Thanh toán"):

        st.success("🎉 Thanh toán thành công!")

        st.download_button(
            label="📥 Tải hóa đơn",
            data=bill_text,
            file_name="hoadon.txt",
            mime="text/plain",
        )

else:
    st.info("Vui lòng chọn món.")