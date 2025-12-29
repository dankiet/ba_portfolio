# 🚀 Quick Start Guide

## 📋 Prerequisites

1. **Python 3.8+**
2. **Hotmailbox API Key** (từ https://hotmailbox.me)

---

## 🛠️ Installation

### 1️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Install Camoufox

```bash
pip install camoufox[geoip]
camoufox fetch
```

### 3️⃣ Install Playwright

```bash
pip install playwright
python -m playwright install
```

---

## ⚙️ Configuration

### **Hotmailbox API Key**

Mở file `task3_mail_service.py` và sửa:

```python
API_KEY = "your_api_key_here"  # ← Thay bằng API key của bạn
```

---

## ▶️ Run Automation

### **Chạy automation:**

```bash
python main.py
```

### **Workflow sẽ tự động:**

1. ✅ Generate user data (fake info)
2. ✅ Mua email từ hotmailbox.me
3. ✅ Ghi trạng thái `PENDING` vào Excel
4. ✅ Khởi động Camoufox browser
5. ✅ Tạo tài khoản Amazon
6. ⏸️ **PAUSE** - Giải Captcha thủ công
7. ✅ Tự động lấy OTP từ email và verify
8. ⏸️ **PAUSE** (nếu cần) - Verify phone thủ công
9. ✅ Điền thông tin cá nhân & ngân hàng
10. ✅ Phỏng vấn thuế
11. ✅ Submit questionnaire
12. ✅ Cập nhật trạng thái `SUCCESS` vào Excel

---

## 🎯 Interactive Prompts

### **Khi timeout (30s):**

```
⏱️  TIMEOUT - Bước X: <step_name>
   Đã đợi 30s nhưng chưa hoàn thành
======================================================================
   👉 Nhấn Enter hoặc 'c': Continue (tiếp tục bước tiếp)
   👉 Nhấn 'r': Retry (thử lại bước này)
   👉 Nhấn 'q': Quit (thoát script)
======================================================================
⏸️  Lựa chọn của bạn:
```

### **Khi cần giải Captcha:**

```
📋 BƯỚC 2: XỬ LÝ CAPTCHA
======================================================================
⏸️  PAUSE: HÃY GIẢI CAPTCHA THỦ CÔNG
   👉 Giải Captcha trên trình duyệt
   👉 Sau khi giải xong, script sẽ tự động tiếp tục
======================================================================
```

### **Khi cần verify phone:**

```
📱 PHÁT HIỆN YÊU CẦU PHONE OTP!
======================================================================
⏸️  PAUSE: HÃY VERIFY PHONE THỦ CÔNG
======================================================================
   👉 Nhập số điện thoại trong trình duyệt
   👉 Nhận OTP qua SMS
   👉 Nhập OTP và verify
   👉 Sau khi verify xong, quay lại terminal
======================================================================
⏸️  Nhấn Enter sau khi đã verify phone xong...
```

---

## 📊 Output

### **Excel Log:**

File: `merch_registration_log.xlsx`

| Email | Password | Status | Profile | Timestamp | Error |
|-------|----------|--------|---------|-----------|-------|
| xxx@hotmail.com | xxx | SUCCESS | Camoufox | 2025-12-26 | |
| yyy@hotmail.com | yyy | FAILED | Camoufox | 2025-12-26 | Timeout |

### **Playwright Trace:**

File: `trace_<email>.zip`

Xem bằng:
```bash
# Cách 1: Dùng Python module
python -m playwright show-trace trace_xxx@hotmail.com.zip

# Cách 2: Dùng helper script
python view_trace.py trace_xxx@hotmail.com.zip
```

### **Screenshots:**

- `error_general.png` - Screenshot khi lỗi
- `require_phone.png` - Screenshot khi cần phone verification

---

## 🔧 Troubleshooting

### **Lỗi: "Không lấy được user data"**

→ Kiểm tra file `task2_data_manager.py` có hoạt động không

### **Lỗi: "Không mua được mail"**

→ Kiểm tra API key trong `task3_mail_service.py`

### **Lỗi: "Không lấy được OTP Email"**

→ Đợi lâu hơn hoặc kiểm tra email có nhận được không

### **Browser không mở:**

→ Kiểm tra Camoufox đã cài đặt chưa:
```bash
camoufox fetch
```

---

## 🎉 Success!

Khi thành công, bạn sẽ thấy:

```
======================================================================
🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH!
======================================================================
✅ GIAI ĐOẠN 4: CẬP NHẬT SUCCESS
======================================================================
🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH!
======================================================================
✅ Script kết thúc thành công!
```

---

## 📞 Support

Nếu gặp vấn đề, check:
1. `merch_automation.log` - Log file
2. `trace_<email>.zip` - Playwright trace
3. Screenshots trong thư mục gốc

---

**Happy Automating! 🚀**

