# Amazon Merch Automation

Automation tool để đăng ký tài khoản Amazon Merch với anti-detection (Camoufox).

---

## 📁 Cấu trúc Project

```
auto_merch/
├── main.py                      # 🎯 Entry point - Orchestrator chính
├── proxy_config.py              # 🌐 Task 1: Proxy configuration & rotation
├── task2_data_manager.py        # 📊 Task 2: Generate user data (fake info)
├── task3_mail_service.py        # 📧 Task 3: Mua email từ hotmailbox.me
├── task4_camoufox_workflow.py   # 🦊 Task 4: Automation workflow (9 steps)
├── task5_excel_reporter.py      # 📝 Task 5: Excel logger + Backup code
├── test_steps.py                # 🧪 Interactive step-by-step testing
├── test_get_2fa.py              # 📱 TOTP generator (for 2FA)
├── info_text.txt                # 📄 Input: User data (12 fields)
└── merch_registration_log.xlsx  # 📊 Output: Excel report
```

---

## 🚀 Workflow

### **1. Prepare Phase**
- `task2_data_manager.py`: Generate user data (fullname, address, SSN, bank info, etc.)
- `task3_mail_service.py`: Mua email từ hotmailbox.me API

### **2. Log Phase**
- `task6_excel_reporter.py`: Ghi trạng thái `PENDING` vào Excel

### **3. Automation Phase**
- `task5_camoufox_workflow.py`: Chạy automation với Camoufox
  - **Bước 1**: Tạo tài khoản Amazon
  - **Bước 2**: Xử lý Captcha (manual)
  - **Bước 3**: Xác thực Email OTP
  - **Bước 4**: Xác thực Phone (nếu cần - manual)
  - **Bước 5**: Chấp nhận điều khoản
  - **Bước 6**: Điền thông tin cá nhân & ngân hàng
  - **Bước 7**: Phỏng vấn thuế
  - **Bước 8**: Questionnaire & Submit

### **4. Finalize Phase**
- `task6_excel_reporter.py`: Cập nhật trạng thái `SUCCESS` hoặc `FAILED`

---

## 🛠️ Installation

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Camoufox
pip install camoufox[geoip]
camoufox fetch
```

---

## ▶️ Usage

### **1️⃣ Full Automation:**

```bash
python main.py
```

### **2️⃣ Step-by-Step Testing:**

```bash
python test_steps.py
```

**Interactive menu** để chạy từng bước riêng lẻ:
- 0️⃣ Setup (Generate data + Buy email + Start browser)
- c️⃣ **Codegen Mode** (Record actions với Playwright Inspector) ← NEW!
- 1️⃣ Step 1: Create Account
- 2️⃣ Step 2: Solve Captcha
- 3️⃣ Step 3: Verify Email OTP
- 4️⃣ Step 4: Fill Profile
- 5️⃣ Step 5: Accept Terms
- 6️⃣ Step 6: Fill Bank Info
- 7️⃣ Step 7: Tax Interview
- 8️⃣ Step 8: Final Submit
- 9️⃣ Close Browser

Xem chi tiết: [STEP_BY_STEP_TESTING.md](STEP_BY_STEP_TESTING.md)

### **3️⃣ Codegen Mode (Standalone):**

```bash
python codegen_camoufox.py
```

**Sử dụng Playwright Inspector** để record actions và generate code.

Xem chi tiết: [CODEGEN_GUIDE.md](CODEGEN_GUIDE.md)

### **4️⃣ Xem Playwright Trace:**

```bash
playwright show-trace trace_<email>.zip
```

---

## 🔧 Configuration

### **Hotmailbox API Key**
Sửa trong `task3_mail_service.py`:
```python
API_KEY = "your_api_key_here"
```

### **Proxy Config**
Sửa trong `proxy_config.py`:
```python
PROXY_HOSTS = ["gb.decodo.com"]
PROXY_PORT_RANGE = (30001, 30100)
PROXY_USERNAME = "your_username"
PROXY_PASSWORD = "your_password"
```

### **Headless Mode**
Sửa trong `main.py`:
```python
result = await start_automation(
    user_data=user_data,
    mail_data=mail_data,
    headless=True,  # True = ẩn browser
    proxy_config=proxy_config  # Proxy config
)
```

---

## 📝 Features

✅ **Anti-Detection**: Sử dụng Camoufox với humanize mode
✅ **Proxy Support**: Random proxy rotation từ pool
✅ **Playwright Trace**: Record toàn bộ workflow để debug
✅ **Timeout Handling**: Mỗi action có timeout 30s + interactive prompt (Retry/Skip/Quit)
✅ **Human-like Behavior**: Random delay, typing speed
✅ **Email OTP**: Tự động lấy OTP từ email
✅ **Excel Logging**: Ghi log chi tiết vào Excel
✅ **Error Handling**: Screenshot khi lỗi

---

## 🔮 Future Improvements

- [ ] Tích hợp `test_get_2fa.py` để tự động verify phone
- [ ] Proxy rotation
- [ ] Multi-threading để chạy nhiều account cùng lúc
- [ ] Retry mechanism khi lỗi

---

## 📄 License

MIT License

