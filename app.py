import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(page_title="Shopee Mock - Mô phỏng Shopee", page_icon="🛒", layout="wide")

# ==================== DỮ LIỆU MẪU ====================
PRODUCTS = [
    {"id": 1,  "name": "Áo thun nam cotton cao cấp",        "price": 89000,   "old_price": 150000, "shop": "ThờI Trang Nam 24h", "rating": 4.8, "sold": 15200, "cat": "ThờI trang",     "emoji": "👕"},
    {"id": 2,  "name": "Giày sneaker thể thao nữ",           "price": 250000,  "old_price": 420000, "shop": "Sneaker House",     "rating": 4.7, "sold": 8300,  "cat": "Giày dép",       "emoji": "👟"},
    {"id": 3,  "name": "Tai nghe Bluetooth TWS Pro",         "price": 199000,  "old_price": 399000, "shop": "TechZone VN",       "rating": 4.9, "sold": 26500, "cat": "Điện tử",        "emoji": "🎧"},
    {"id": 4,  "name": "Điện thoại Smartphone X10 5G",       "price": 4990000, "old_price": 6500000,"shop": "Mobile Center",     "rating": 4.6, "sold": 3200,  "cat": "Điện tử",        "emoji": "📱"},
    {"id": 5,  "name": "Sữa rửa mặt Hàn Quốc dưỡng ẩm",      "price": 120000,  "old_price": 220000, "shop": "BeautyShop HN",     "rating": 4.8, "sold": 19800, "cat": "Làm đẹp",        "emoji": "🧴"},
    {"id": 6,  "name": "Ba lô laptop chống nước 15.6 inch",  "price": 350000,  "old_price": 550000, "shop": "Balo Store",        "rating": 4.7, "sold": 6700,  "cat": "Phụ kiện",       "emoji": "🎒"},
    {"id": 7,  "name": "Đồng hồ nam dây thép không gỉ",      "price": 450000,  "old_price": 800000, "shop": "WatchKing",         "rating": 4.5, "sold": 4100,  "cat": "Phụ kiện",       "emoji": "⌚"},
    {"id": 8,  "name": "Quần jean nữ ống suông",             "price": 180000,  "old_price": 300000, "shop": "Jean Fashion",      "rating": 4.6, "sold": 9800,  "cat": "ThờI trang",     "emoji": "👖"},
    {"id": 9,  "name": "Loa bluetooth mini bass mạnh",       "price": 159000,  "old_price": 299000, "shop": "TechZone VN",       "rating": 4.7, "sold": 12400, "cat": "Điện tử",        "emoji": "🔊"},
    {"id": 10, "name": "Son môi lì siêu mịn màu đỏ cam",     "price": 99000,   "old_price": 180000, "shop": "BeautyShop HN",     "rating": 4.9, "sold": 22100, "cat": "Làm đẹp",        "emoji": "💄"},
    {"id": 11, "name": "Nồi chiên không dầu 5L",             "price": 890000,  "old_price": 1290000,"shop": "Gia Dụng VN",       "rating": 4.8, "sold": 5600,  "cat": "Gia dụng",       "emoji": "🍳"},
    {"id": 12, "name": "Máy xay sinh tố cầm tay",            "price": 230000,  "old_price": 380000, "shop": "Gia Dụng VN",       "rating": 4.5, "sold": 7300,  "cat": "Gia dụng",       "emoji": "🥤"},
    {"id": 13, "name": "Dép quai ngang unisex thờI trang",   "price": 45000,   "old_price": 90000,  "shop": "Sneaker House",     "rating": 4.4, "sold": 31000, "cat": "Giày dép",       "emoji": "🩴"},
    {"id": 14, "name": "Váy suông nữ công sở",               "price": 220000,  "old_price": 380000, "shop": "ThờI Trang Nữ Mia", "rating": 4.6, "sold": 8900,  "cat": "ThờI trang",     "emoji": "👗"},
    {"id": 15, "name": "Chuột gaming không dây RGB",         "price": 189000,  "old_price": 350000, "shop": "TechZone VN",       "rating": 4.7, "sold": 11500, "cat": "Điện tử",        "emoji": "🖱️"},
    {"id": 16, "name": "Kem chống nắng SPF50+ PA++++",       "price": 145000,  "old_price": 250000, "shop": "BeautyShop HN",     "rating": 4.8, "sold": 17600, "cat": "Làm đẹp",        "emoji": "🧴"},
]

BANNERS = ["🔥 Flash Sale - Giảm đến 50%", "🚚 Miễn phí vận chuyển toàn quốc", "🎁 Voucher 100K cho đơn đầu tiên"]
CATEGORIES = ["Tất cả"] + sorted(set(p["cat"] for p in PRODUCTS))

def fmt_price(n):
    return f"{n:,}".replace(",", ".")

# ==================== SESSION STATE ====================
if "cart" not in st.session_state:
    st.session_state.cart = {}          # {id: qty}
if "orders" not in st.session_state:
    st.session_state.orders = []        # danh sách đơn hàng
if "liked" not in st.session_state:
    st.session_state.liked = set()

def add_to_cart(pid):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1

# ==================== GIAO DIỆN ====================
st.markdown("""
<style>
    .shop-header {background: linear-gradient(90deg,#ee4d2d,#ff7337); color:white;
                   padding:12px 20px; border-radius:10px; font-size:26px; font-weight:800;}
    .flash-sale {background: linear-gradient(90deg,#d0011b,#ff5722); color:white;
                  padding:10px 15px; border-radius:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="shop-header">🛒 Shopee Mock — Sàn thương mại điện tử (mô phỏng)</div>', unsafe_allow_html=True)

# Thanh tìm kiếm + giỏ hàng
top_col1, top_col2 = st.columns([5, 1])
with top_col1:
    keyword = st.text_input("🔍 Tìm kiếm sản phẩm...", placeholder="Tìm áo thun, tai nghe, son môi...")
with top_col2:
    cart_count = sum(st.session_state.cart.values())
    st.metric("🛒 Giỏ hàng", f"{cart_count} SP")

# Banner chạy
banner_idx = (datetime.now().second // 5) % len(BANNERS)
st.info(f"📢 **{BANNERS[banner_idx]}**")

# Sidebar
st.sidebar.title("🗂️ Danh mục")
cat = st.sidebar.radio("Chọn danh mục", CATEGORIES)
st.sidebar.divider()
max_price = st.sidebar.slider("💰 Giá tối đa (đ)", 0, 5000000, 5000000, step=50000)
sort_by = st.sidebar.selectbox("Sắp xếp theo", ["Phổ biến (bán chạy)", "Giá: thấp → cao", "Giá: cao → thấp", "Đánh giá cao"])

st.sidebar.divider()
st.sidebar.markdown("### 💳 Ví ShopeeMock")
st.sidebar.progress(min(len(st.session_state.orders) * 0.15, 1.0))
st.sidebar.caption("Mua thêm để lên hạng thành viên!")

# ==================== FLASH SALE ====================
st.markdown('<div class="flash-sale">⚡ FLASH SALE - Mua nhanh kẻo lỡ!</div>', unsafe_allow_html=True)
flash_items = sorted(PRODUCTS, key=lambda x: x["sold"], reverse=True)[:5]
fcols = st.columns(len(flash_items))
for i, p in enumerate(flash_items):
    with fcols[i]:
        with st.container(border=True):
            st.markdown(f"#### {p['emoji']} {p['name']}")
            st.markdown(f"🔥 **₫{fmt_price(p['price'])}** ~~₫{fmt_price(p['old_price'])}~~")
            if st.button("Thêm ⚡", key=f"flash_{p['id']}", use_container_width=True):
                add_to_cart(p["id"])
                st.toast(f"Đã thêm {p['name']} vào giỏ! 🎉")
st.divider()

# ==================== DANH SÁCH SẢN PHẨM ====================
items = [p for p in PRODUCTS
         if (cat == "Tất cả" or p["cat"] == cat)
         and p["price"] <= max_price
         and (keyword.lower() in p["name"].lower() or keyword.lower() in p["shop"].lower())]

if sort_by == "Giá: thấp → cao":
    items.sort(key=lambda x: x["price"])
elif sort_by == "Giá: cao → thấp":
    items.sort(key=lambda x: -x["price"])
elif sort_by == "Đánh giá cao":
    items.sort(key=lambda x: -x["rating"])
else:
    items.sort(key=lambda x: -x["sold"])

st.subheader(f"🛍️ Sản phẩm ({len(items)} kết quả)")

if not items:
    st.warning("Không tìm thấy sản phẩm phù hợp. Hãy thử từ khóa khác nhé!")

cols = st.columns(4)
for i, p in enumerate(items):
    with cols[i % 4]:
        with st.container(border=True):
            st.markdown(f"### {p['emoji']}")
            st.markdown(f"**{p['name']}**")
            st.caption(f"🏪 {p['shop']}")
            disc = round((1 - p['price']/p['old_price']) * 100)
            st.markdown(f"₫{fmt_price(p['price'])}  ~~₫{fmt_price(p['old_price'])}~~  **-{disc}%**")
            st.caption(f"⭐ {p['rating']} | 🔥 Đã bán {p['sold']:,}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🛒 Thêm", key=f"add_{p['id']}", use_container_width=True):
                    add_to_cart(p["id"])
                    st.toast(f"Đã thêm {p['name']} vào giỏ! 🎉")
            with c2:
                like_lbl = "❤️" if p["id"] in st.session_state.liked else "🤍"
                if st.button(like_lbl, key=f"like_{p['id']}", use_container_width=True):
                    if p["id"] in st.session_state.liked:
                        st.session_state.liked.discard(p["id"])
                    else:
                        st.session_state.liked.add(p["id"])
                    st.rerun()

st.divider()

# ==================== GIỎ HÀNG ====================
st.header("🛒 Giỏ hàng của bạn")
if not st.session_state.cart:
    st.info("Giỏ hàng đang trống. Mua sắm thôi nào! 🛍️")
else:
    cart_rows = []
    total = 0
    for pid, qty in st.session_state.cart.items():
        p = next(x for x in PRODUCTS if x["id"] == pid)
        sub = p["price"] * qty
        total += sub
        cart_rows.append({"Sản phẩm": f"{p['emoji']} {p['name']}", "Đơn giá": fmt_price(p["price"]),
                          "SL": qty, "Thành tiền": fmt_price(sub), "id": pid})
    df = pd.DataFrame(cart_rows)
    st.dataframe(df.drop(columns=["id"]), use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        del_id = st.selectbox("Chọn sản phẩm để xóa", options=[r["id"] for r in cart_rows],
                              format_func=lambda i: next(x["name"] for x in PRODUCTS if x["id"] == i))
        if st.button("❌ Xóa khỏi giỏ"):
            st.session_state.cart.pop(del_id, None)
            st.rerun()
    with c2:
        if st.button("🧹 Xóa toàn bộ giỏ"):
            st.session_state.cart = {}
            st.rerun()
    with c3:
        ship_fee = 0 if total >= 300000 else 25000
        voucher = min(total // 10, 100000)
        final = total + ship_fee - voucher
        st.markdown(f"**Tạm tính:** ₫{fmt_price(total)}  ")
        st.markdown(f"**Phí ship:** {'Miễn phí 🚚' if ship_fee == 0 else f'₫{fmt_price(ship_fee)}'}  ")
        st.markdown(f"**Voucher:** -₫{fmt_price(voucher)}  ")
        st.markdown(f"### 💰 Tổng: ₫{fmt_price(final)}")
        if st.button("✅ ĐẶT HÀNG NGAY", type="primary", use_container_width=True):
            order = {
                "code": f"SM{random.randint(100000, 999999)}",
                "items": dict(st.session_state.cart),
                "total": final,
                "time": datetime.now().strftime("%H:%M %d/%m/%Y"),
                "status": "Chờ xác nhận",
            }
            st.session_state.orders.append(order)
            st.session_state.cart = {}
            st.success(f"🎉 Đặt hàng thành công! Mã đơn: **{order['code']}**")
            st.balloons()

# ==================== ĐƠN HÀNG CỦA TÔI ====================
st.divider()
st.header("📦 Đơn hàng của tôi")
if not st.session_state.orders:
    st.caption("Chưa có đơn hàng nào.")
else:
    for idx, o in enumerate(reversed(st.session_state.orders)):
        real_idx = len(st.session_state.orders) - 1 - idx
        names = [next(x["name"] for x in PRODUCTS if x["id"] == pid) for pid in o["items"]]
        with st.expander(f"🧾 {o['code']} — {o['time']} — ₫{fmt_price(o['total'])} — {o['status']}"):
            st.write(", ".join(names))
            col_a, col_b = st.columns(2)
            with col_a:
                if o["status"] == "Chờ xác nhận" and st.button("❌ Hủy đơn", key=f"cancel_{real_idx}"):
                    st.session_state.orders[real_idx]["status"] = "Đã hủy"
                    st.rerun()
            with col_b:
                if o["status"] == "Chờ xác nhận" and st.button("✔️ Xác nhận đã nhận", key=f"done_{real_idx}"):
                    st.session_state.orders[real_idx]["status"] = "Hoàn thành"
                    st.rerun()

st.caption("© 2026 ShopeeMock — Ứng dụng mô phỏng học tập, không phải Shopee thật.")
