# 🎬 CÁCH CHẠY PLAYWRIGHT CODEGEN

## ❌ LỖI BẠN GẶP

```powershell
playwright install chromium
# playwright : The term 'playwright' is not recognized...
```

**Nguyên nhân:** Trên Windows, phải chạy qua Python module.

---

## ✅ CÁCH ĐÚNG

### 1️⃣ Cài Playwright (đã xong)

```powershell
pip install playwright
python -m playwright install chromium
```

### 2️⃣ Chạy Codegen

**Cách 1: Mở trang cụ thể**
```powershell
python -m playwright codegen merch.amazon.com
```

**Cách 2: Mở browser trống**
```powershell
python -m playwright codegen
```

**Cách 3: Với options**
```powershell
# Chọn browser
python -m playwright codegen --browser chromium merch.amazon.com

# Với viewport size
python -m playwright codegen --viewport-size=1920,1080 merch.amazon.com

# Save output to file
python -m playwright codegen --target python -o recorded_script.py merch.amazon.com
```

---

## 🎯 SAU KHI CHẠY CODEGEN

### Bạn sẽ thấy:

1. **Browser window** - Trình duyệt mở ra
2. **Playwright Inspector** - Cửa sổ ghi nhận code

### Thao tác:

1. Click, type, navigate như bình thường
2. Code Python được generate **REAL-TIME** trong Inspector
3. Copy code khi xong

---

## 📋 VÍ DỤ CODE ĐƯỢC GENERATE

Khi bạn thao tác:
- Click "Sign up" button
- Type email
- Type password
- Click "Create account"

Playwright sẽ generate:

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://merch.amazon.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("MyPassword123")
    page.get_by_role("button", name="Create account").click()
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

---

## 🔥 TIPS

### 1. Save to file
```powershell
python -m playwright codegen --target python -o merch_signup.py merch.amazon.com
```

### 2. Chọn browser
```powershell
# Chrome
python -m playwright codegen --browser chromium merch.amazon.com

# Firefox
python -m playwright codegen --browser firefox merch.amazon.com
```

### 3. Với device emulation
```powershell
python -m playwright codegen --device="iPhone 12" merch.amazon.com
```

---

## 🚀 WORKFLOW ĐỀ XUẤT

### BƯỚC 1: Record toàn bộ flow

```powershell
python -m playwright codegen --target python -o merch_full_flow.py merch.amazon.com
```

Thao tác:
1. Click Sign up
2. Fill email, password, name
3. Submit form
4. Wait for OTP page
5. Fill OTP
6. Continue to next steps
7. Fill personal info
8. Fill bank info
9. Fill tax info
10. Submit

### BƯỚC 2: Copy code

Mở file `merch_full_flow.py` và xem code được generate.

### BƯỚC 3: Refactor

Tách thành functions:
```python
def signup_step1(page, email, password, name):
    page.goto("https://merch.amazon.com/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_label("Name").fill(name)
    page.get_by_role("button", name="Create account").click()

def fill_otp(page, otp_code):
    page.get_by_label("Enter OTP").fill(otp_code)
    page.get_by_role("button", name="Verify").click()

# ... etc
```

### BƯỚC 4: Integrate với GPM

```python
from playwright.sync_api import sync_playwright

def connect_to_gpm(debug_address):
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://{debug_address}")
        context = browser.contexts[0]
        page = context.pages[0] if context.pages else context.new_page()
        return page

# Sử dụng
debug_address = "127.0.0.1:9222"  # Từ GPM API
page = connect_to_gpm(debug_address)

# Chạy automation
signup_step1(page, "test@example.com", "pass123", "John Doe")
```

---

## ❓ FAQ

**Q: Codegen có ghi nhận được mọi thao tác không?**
A: Có! Click, type, select, navigate, upload file, drag & drop, v.v.

**Q: Code được generate có chạy được ngay không?**
A: Có, nhưng nên refactor để dễ maintain.

**Q: Có thể edit code trong Inspector không?**
A: Không, chỉ xem. Phải copy ra file để edit.

**Q: Codegen có hoạt động với GPM Login không?**
A: Codegen dùng browser riêng. Sau khi record xong, bạn sẽ kết nối code đó với GPM.

---

## 🎯 CHẠY NGAY

```powershell
# Chạy lệnh này trong PowerShell:
python -m playwright codegen merch.amazon.com
```

Sau đó:
1. Thao tác thủ công toàn bộ flow đăng ký
2. Copy code từ Inspector
3. Gửi cho tôi, tôi sẽ giúp refactor và integrate với GPM!

