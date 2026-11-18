# 🛒 Shopee Mock

Ứng dụng mô phỏng sàn thương mại điện tử Shopee, xây dựng bằng **Streamlit + Python**.  
Dự án phục vụ học tập và demo quy trình phát triển ứng dụng web với Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

## 📸 Tính năng

- 🔍 Tìm kiếm sản phẩm theo tên / tên shop
- 🗂️ Lọc theo danh mục, khoảng giá, sắp xếp (giá, đánh giá, bán chạy)
- ⚡ Flash Sale (top sản phẩm bán chạy nhất)
- 🛒 Giỏ hàng: thêm / xóa / xóa toàn bộ
- 💰 Tự động tính phí ship (freeship đơn ≥ 300K) và voucher giảm 10% (tối đa 100K)
- ❤️ Yêu thích sản phẩm
- 📦 Đặt hàng, quản lý đơn hàng (hủy đơn, xác nhận nhận hàng)
- 📢 Banner quảng cáo luân chuyển

## 🚀 Chạy local

```bash
# 1. Clone repo
git clone https://github.com/<username>/shopee-mock.git
cd shopee-mock

# 2. Tạo môi trường ảo (khuyến nghị)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Cài dependencies
pip install -r requirements.txt

# 4. Chạy app
streamlit run app.py
```

Mở trình duyệt tại: `http://localhost:8501`

## ☁️ Triển khai lên Streamlit Cloud

1. **Đẩy code lên GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Shopee Mock app"
   git branch -M main
   git remote add origin https://github.com/<username>/shopee-mock.git
   git push -u origin main
   ```

2. **Deploy**:
   - Truy cập [share.streamlit.io](https://share.streamlit.io)
   - Đăng nhập bằng tài khoản GitHub
   - Bấm **New app** → chọn repo `shopee-mock`
   - **Main file path**: `app.py`
   - Bấm **Deploy** 🚀

App sẽ tự động build và có URL dạng `https://<app-name>.streamlit.app`

## 📁 Cấu trúc project

```
shopee-mock/
├── app.py                  # Ứng dụng chính
├── requirements.txt        # Python dependencies
├── packages.txt            # System packages (nếu cần)
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml         # Theme & cấu hình Streamlit
```

## 🛠️ Công nghệ

- [Streamlit](https://streamlit.io/) — framework xây dựng app data/web
- [Pandas](https://pandas.pydata.org/) — hiển thị dữ liệu bảng

## 📄 Giấy phép

MIT License — xem file [LICENSE](LICENSE).
