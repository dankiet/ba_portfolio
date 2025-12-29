# Business Case
## Amazon Merch Registration Automation

---

## 1. Executive Summary

**Project Name:** Amazon Merch Automation Tool  
**Project Type:** RPA (Robotic Process Automation)  
**Duration:** 4 tuần phát triển  
**Target Users:** Print-on-Demand Sellers, E-commerce Entrepreneurs

### Tóm tắt
Xây dựng công cụ tự động hóa quy trình đăng ký tài khoản Amazon Merch on Demand, giúp giảm thời gian đăng ký từ **30-45 phút xuống còn 5-10 phút** mỗi tài khoản, đồng thời tránh bị phát hiện automation nhờ sử dụng anti-detection browser.

---

## 2. Business Context

### 2.1 Giới thiệu Amazon Merch on Demand
Amazon Merch on Demand là chương trình cho phép sellers thiết kế và bán sản phẩm Print-on-Demand (áo thun, cốc, sticker) trên Amazon mà không cần:
- Đầu tư inventory
- Xử lý shipping
- Customer service (Amazon lo)

### 2.2 Thị trường mục tiêu
- **Freelancers/Designers** muốn monetize designs
- **E-commerce Entrepreneurs** muốn scale business POD
- **Agencies** quản lý nhiều brands/stores

### 2.3 Nhu cầu thực tế
| Đối tượng | Số account cần | Lý do |
|-----------|---------------|-------|
| Individual Seller | 1-5 | Test nhiều niches |
| Small Agency | 10-20 | Đa dạng portfolio |
| Large Operation | 50-100+ | Scale production |

---

## 3. Problem Statement

### 3.1 Vấn đề hiện tại (AS-IS)

```mermaid
flowchart TD
    A[Bắt đầu đăng ký] --> B[Tạo email mới thủ công]
    B --> C[Điền form Amazon - 20+ fields]
    C --> D[Chờ email OTP]
    D --> E[Verify OTP thủ công]
    E --> F{Phone verification?}
    F -->|Yes| G[Nhập số điện thoại]
    G --> H[Chờ SMS OTP]
    H --> I[Verify phone]
    F -->|No| J[Điền Tax Interview - 15 fields]
    I --> J
    J --> K[Complete Questionnaire]
    K --> L[Submit & chờ approval]
    
    style A fill:#ffcccc
    style L fill:#ffcccc
```

**Pain Points:**

| # | Vấn đề | Impact |
|---|--------|--------|
| 1 | **Thời gian dài** | 30-45 phút/account |
| 2 | **Repetitive tasks** | Điền lặp lại 50+ fields |
| 3 | **IP blocking** | Amazon detect & block automation |
| 4 | **Email management** | Phải tạo/quản lý nhiều emails |
| 5 | **Human errors** | Điền sai format, thiếu thông tin |
| 6 | **Không scalable** | Max 5-10 accounts/ngày/người |

### 3.2 Root Cause Analysis

```mermaid
flowchart LR
    subgraph Root Causes
        RC1[Manual Process]
        RC2[No Anti-Detection]
        RC3[No Email Automation]
    end
    
    subgraph Effects
        E1[Slow Registration]
        E2[High Block Rate]
        E3[Cannot Scale]
    end
    
    RC1 --> E1
    RC2 --> E2
    RC3 --> E1
    E1 --> E3
    E2 --> E3
```

---

## 4. Proposed Solution

### 4.1 Solution Overview (TO-BE)

```mermaid
flowchart TD
    A[Operator chạy script] --> B[Task 2: Generate User Data]
    B --> C[Task 3: Auto Buy Email từ API]
    C --> D[Task 5: Log PENDING to Excel]
    D --> E[Task 4: Launch Camoufox Browser]
    E --> F[Auto Fill Registration Form]
    F --> G[Auto Get & Verify OTP]
    G --> H{Phone Required?}
    H -->|Yes| I[⏸️ Manual Phone Verify]
    H -->|No| J[Auto Fill Tax Interview]
    I --> J
    J --> K[Auto Complete Questionnaire]
    K --> L[Task 5: Update SUCCESS/FAILED]
    
    style A fill:#ccffcc
    style L fill:#ccffcc
```

### 4.2 Key Features

| Feature | Mô tả | Benefit |
|---------|-------|---------|
| **Anti-Detection Browser** | Sử dụng Camoufox với fingerprint masking | Giảm 80% block rate |
| **Auto Email Purchase** | Mua email từ API bên thứ 3 | Không cần tạo email thủ công |
| **Auto OTP Retrieval** | Polling API để lấy OTP tự động | Giảm 5 phút chờ đợi |
| **Proxy Rotation** | Random proxy từ pool 100 IPs | Tránh IP blocking |
| **Human-like Behavior** | Random delays, typing speed | Tránh bot detection |
| **Excel Logging** | Tracking status realtime | Dễ quản lý & debug |
| **Interactive Prompts** | Retry/Skip/Quit options | Handle edge cases |

### 4.3 Technology Stack

```mermaid
flowchart LR
    subgraph Core
        A[Python 3.8+]
    end
    
    subgraph Automation
        B[Playwright]
        C[Camoufox]
    end
    
    subgraph External APIs
        D[DongvanFB - Email]
        E[Decodo - Proxy]
    end
    
    subgraph Storage
        F[Excel/openpyxl]
        G[Text Files]
    end
    
    A --> B
    B --> C
    A --> D
    A --> E
    A --> F
    A --> G
```

---

## 5. Project Scope

### 5.1 In-Scope ✅

| # | Feature | Priority |
|---|---------|----------|
| 1 | Auto generate user data (12 fields) | P0 |
| 2 | Auto purchase Hotmail email | P0 |
| 3 | Auto fill Amazon registration form | P0 |
| 4 | Auto retrieve & verify Email OTP | P0 |
| 5 | Interactive Captcha handling | P0 |
| 6 | Auto complete Tax Interview | P0 |
| 7 | Auto complete Questionnaire | P0 |
| 8 | Excel status tracking | P0 |
| 9 | Proxy rotation support | P1 |
| 10 | Playwright trace recording | P1 |
| 11 | Error screenshots | P1 |
| 12 | Step-by-step testing mode | P2 |

### 5.2 Out-of-Scope ❌

| # | Feature | Lý do |
|---|---------|-------|
| 1 | Auto Phone OTP verification | Cần integration SMS service |
| 2 | Auto Captcha solving | Cần AI service (2captcha, CapMonster) |
| 3 | Multi-threading | Phase 2 feature |
| 4 | Web UI dashboard | CLI is sufficient |
| 5 | Database storage | Excel is adequate for current scale |

---

## 6. Success Criteria & KPIs

### 6.1 Success Metrics

| Metric | Before (Manual) | Target | Actual |
|--------|-----------------|--------|--------|
| **Time per account** | 30-45 min | < 10 min | 8-12 min |
| **Success rate** | 90% | > 60% | ~65% |
| **Accounts per day** | 5-10 | 30-50 | 40+ |
| **Block rate** | 30% | < 10% | ~8% |

### 6.2 ROI Calculation

```
Manual: 10 accounts/day × 40 min × $30/hr = $200/day labor cost
Auto:   40 accounts/day × 10 min × $30/hr = $200/day (4x output)

ROI = (40 - 10) accounts × $5 revenue/account = $150/day extra profit
Monthly: $150 × 30 = $4,500 additional revenue
```

### 6.3 Acceptance Criteria

- [ ] Tool runs successfully on macOS
- [ ] Handles Email OTP automatically
- [ ] Pauses properly for Captcha
- [ ] Logs all attempts to Excel
- [ ] Provides clear error messages
- [ ] Supports proxy configuration

---

## 7. Risks & Assumptions

### 7.1 Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Amazon updates form | Medium | High | Modular code, easy to update selectors |
| Email API down | Low | High | Fallback to manual email |
| Proxy blocked | Medium | Medium | Large proxy pool (100 IPs) |
| Captcha frequency increases | High | Medium | Interactive pause for manual solve |
| Phone verification required | High | High | Interactive pause (future: auto) |

### 7.2 Assumptions

| # | Assumption |
|---|------------|
| 1 | User có API key cho email service |
| 2 | User có proxy subscription |
| 3 | User có dữ liệu UK valid (address, bank, UTR) |
| 4 | Amazon không thay đổi form structure frequently |
| 5 | Camoufox anti-detection đủ mạnh |

---

## 8. Timeline & Milestones

```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Requirements Analysis    :a1, 2024-01-01, 3d
    System Design           :a2, after a1, 3d
    section Phase 2
    Core Development        :a3, after a2, 7d
    Email Integration       :a4, after a3, 2d
    Proxy Integration       :a5, after a4, 2d
    section Phase 3
    Testing & Debug         :a6, after a5, 5d
    Documentation           :a7, after a6, 3d
    section Phase 4
    Deployment              :a8, after a7, 2d
```

---

## 9. Stakeholder Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project Owner | [Name] | [Date] | __________ |
| Developer | [Name] | [Date] | __________ |
| QA | [Name] | [Date] | __________ |

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-28  
**Author:** Business Analyst
