# ✅ REORDER STEPS SUMMARY - Điều chỉnh thứ tự bước

---

## 🎯 ĐÃ THỰC HIỆN

### **1. Đổi thứ tự bước (Steps 3.5 và 4 → sau bước 5)**

**Thứ tự CŨ:**
```
Step 1: Create Account
Step 2: Handle Captcha
Step 3: Verify Email OTP
Step 3.5: Verify 2FA (Backup Code) ← SAU Step 3
Step 4: Verify Phone ← SAU Step 3.5
Step 5: Accept Terms
Step 6: Fill Profile & Bank
Step 7: Tax Interview
Step 8: Questionnaire
```

**Thứ tự MỚI:**
```
Step 1: Create Account
Step 2: Handle Captcha
Step 3: Verify Email OTP
Step 4: Accept Terms ← TRƯỚC 2FA
Step 5: Verify 2FA (Backup Code) ⭐ SAU Accept Terms
Step 6: Verify Phone ⭐ SAU 2FA
Step 7: Fill Profile & Bank
Step 8: Tax Interview
Step 9: Questionnaire
```

---

### **2. Lưu backup code vào Excel ngay khi phát hiện (Step 5)**

**File:** `task4_camoufox_workflow.py` (step_5_verify_2fa)

**Chức năng:**
- Screenshot backup code với tên file: `step5_backup_code_{email}.png`
- Gọi `save_backup_code()` từ `task5_excel_reporter.py`
- Lưu vào Excel columns:
  - Column 7: `Backup_Code` (text)
  - Column 8: `Backup_Screenshot` (path)

**Code:**
```python
# Screenshot backup code
backup_code_screenshot = f"step5_backup_code_{mail_data['mail']}.png"
await page.screenshot(path=backup_code_screenshot, full_page=True)

# Save backup code to Excel immediately
from task5_excel_reporter import save_backup_code
save_backup_code(mail_data['mail'], backup_code_text, backup_code_screenshot)
```

---

### **3. Rename Task 5 → Task 4, Task 6 → Task 5**

**Files renamed:**
- `task5_camoufox_workflow.py` → `task4_camoufox_workflow.py`
- `task6_excel_reporter.py` → `task5_excel_reporter.py`

**Lý do:**
- Workflow: Task 1 (Proxy) → Task 2 (User Data) → Task 3 (Email) → **Task 4 (Automation)** → **Task 5 (Excel)**
- Không có gap (1-2-3-5-6 → 1-2-3-4-5)

---

### **4. Update function names**

**Renamed functions trong task4_camoufox_workflow.py:**

| Old Name | New Name | Step Number |
|----------|----------|-------------|
| `step_3_5_verify_2fa` | `step_5_verify_2fa` | 5 |
| `step_4_verify_phone` | `step_6_verify_phone` | 6 |
| `step_5_accept_terms` | `step_4_accept_terms` | 4 |
| `step_6_fill_profile_bank` | `step_7_fill_profile_bank` | 7 |
| `step_7_tax_interview` | `step_8_tax_interview` | 8 |
| `step_8_questionnaire` | `step_9_questionnaire` | 9 |

**Signature changes:**
- `step_5_verify_2fa(page, mail_data)` ← Thêm `mail_data` parameter để lưu backup code

---

### **5. Update test_steps.py**

**Menu updated:**
```
0   → Setup
0f  → Setup FAKE PROXY
c   → Codegen Mode
1   → Step 1: Create Account
2   → Step 2: Handle Captcha
3   → Step 3: Verify Email OTP
4   → Step 4: Accept Terms
5   → Step 5: Verify 2FA (Backup Code) - OPTION 1 ⭐ NEW!
6   → Step 6: Verify Phone (if required)
7   → Step 7: Fill Profile & Bank Info (UK)
8   → Step 8: Tax Interview (Full Flow)
9   → Step 9: Questionnaire & Submit (Full Fields)
x   → Close Browser
q   → Quit
```

**Imports updated:**
```python
from task4_camoufox_workflow import (
    start_browser,
    step_1_create_account,
    step_2_handle_captcha,
    step_3_verify_email,
    step_4_accept_terms,
    step_5_verify_2fa,
    step_6_verify_phone,
    step_7_fill_profile_bank,
    step_8_tax_interview,
    step_9_questionnaire
)
```

---

### **6. Update main.py**

**Imports updated:**
```python
from task4_camoufox_workflow import start_automation
from task5_excel_reporter import save_pending, update_success, update_failed, update_status
```

---

### **7. Add save_backup_code() function**

**File:** `task5_excel_reporter.py`

**Function:**
```python
def save_backup_code(email, backup_code_text, screenshot_path):
    """
    Lưu backup code vào Excel ngay khi phát hiện (Step 5)
    
    Args:
        email: Email của account
        backup_code_text: Text của backup code
        screenshot_path: Path của screenshot backup code
    """
    # Tìm row của email
    # Thêm columns: Backup_Code (7), Backup_Screenshot (8)
    # Lưu vào Excel
```

---

## 📊 SO SÁNH TRƯỚC/SAU

| Item | Before | After |
|------|--------|-------|
| **Step 3.5** | Verify 2FA (sau Step 3) | → **Step 5** (sau Accept Terms) |
| **Step 4** | Verify Phone (sau Step 3.5) | → **Step 6** (sau Step 5) |
| **Step 5** | Accept Terms (sau Step 4) | → **Step 4** (sau Step 3) |
| **Step 6** | Fill Profile & Bank | → **Step 7** |
| **Step 7** | Tax Interview | → **Step 8** |
| **Step 8** | Questionnaire | → **Step 9** |
| **Task 5** | Automation | → **Task 4** |
| **Task 6** | Excel Reporter | → **Task 5** |
| **Backup Code** | Screenshot only | → **Save to Excel immediately** |

---

## 🎯 LÝ DO THAY ĐỔI

### **1. Thứ tự logic hơn:**
- Accept Terms (Step 4) nên đi trước 2FA (Step 5)
- 2FA và Phone verification nên đi sau Accept Terms

### **2. Lưu backup code ngay:**
- Backup code rất quan trọng, cần lưu ngay khi phát hiện
- Tránh mất backup code nếu workflow fail ở bước sau

### **3. Không có gap trong task numbers:**
- Task 1-2-3-4-5 (thay vì 1-2-3-5-6)
- Dễ hiểu và maintain hơn

---

## ✅ FILES UPDATED

1. ✅ `task4_camoufox_workflow.py` (renamed from task5)
   - Reorder steps
   - Rename functions
   - Add save_backup_code() call

2. ✅ `task5_excel_reporter.py` (renamed from task6)
   - Add save_backup_code() function
   - Update comment

3. ✅ `test_steps.py`
   - Update imports
   - Update menu
   - Update run_step() logic

4. ✅ `main.py`
   - Update imports

---

**🎉 Hoàn thành điều chỉnh thứ tự bước và task numbers!**


