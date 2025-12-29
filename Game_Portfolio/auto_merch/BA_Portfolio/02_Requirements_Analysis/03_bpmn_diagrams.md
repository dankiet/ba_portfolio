# BPMN Process Diagrams
## Amazon Merch Registration Automation

---

## 1. Overview

Tài liệu này mô tả quy trình nghiệp vụ **trước (AS-IS)** và **sau (TO-BE)** khi triển khai hệ thống automation.

---

## 2. AS-IS Process: Manual Registration

### 2.1 High-Level Process

```mermaid
flowchart TB
    subgraph Start
        A((Start))
    end
    
    subgraph Preparation["1. Preparation Phase"]
        B[Create new email account]
        C[Prepare user information]
        D[Configure browser/VPN]
    end
    
    subgraph Registration["2. Registration Phase"]
        E[Navigate to Amazon Merch]
        F[Fill registration form manually]
        G[Submit form]
    end
    
    subgraph Verification["3. Verification Phase"]
        H{Email OTP received?}
        I[Check email inbox]
        J[Copy OTP manually]
        K[Enter OTP on Amazon]
        L{Captcha appeared?}
        M[Solve Captcha manually]
        N{Phone verification?}
        O[Enter phone number]
        P[Wait for SMS]
        Q[Enter SMS code]
    end
    
    subgraph Profile["4. Profile Completion"]
        R[Fill personal information]
        S[Fill bank details]
        T[Complete Tax Interview]
        U[Answer Questionnaire]
        V[Submit application]
    end
    
    subgraph Recording["5. Recording"]
        W[Record to spreadsheet manually]
        X[Save credentials]
    end
    
    subgraph End
        Y((End))
    end
    
    A --> B --> C --> D --> E --> F --> G --> H
    H -->|No| I --> H
    H -->|Yes| J --> K --> L
    L -->|Yes| M --> N
    L -->|No| N
    N -->|Yes| O --> P --> Q --> R
    N -->|No| R
    R --> S --> T --> U --> V --> W --> X --> Y
```

### 2.2 Pain Points Analysis

| Step | Pain Point | Time Impact | Error Rate |
|------|------------|-------------|------------|
| Create email | Manual creation, verification | 5-7 min | Low |
| Fill form | 20+ fields, repetitive | 10-15 min | Medium |
| Wait for OTP | Check inbox constantly | 2-5 min | Low |
| Solve Captcha | Must be present | 1-2 min | Low |
| Phone verify | SMS delays, manual entry | 3-5 min | Low |
| Tax Interview | 15 fields, complex | 5-7 min | High |
| Record results | Copy/paste to spreadsheet | 3-5 min | Medium |
| **Total** | | **30-45 min** | **15-20%** |

### 2.3 Swim Lane Diagram

```mermaid
flowchart TB
    subgraph Operator["👤 Operator"]
        O1[Prepare data]
        O2[Create email]
        O3[Fill all forms]
        O4[Solve Captcha]
        O5[Handle phone OTP]
        O6[Record to Excel]
    end
    
    subgraph Amazon["🛒 Amazon Platform"]
        A1[Display registration page]
        A2[Send Email OTP]
        A3[Show Captcha]
        A4[Request Phone Verification]
        A5[Accept submission]
    end
    
    subgraph EmailProvider["📧 Email Provider"]
        E1[Receive OTP email]
    end
    
    O1 --> O2 --> O3
    O3 --> A1
    A1 --> A2
    A2 --> E1
    E1 --> O3
    O3 --> A3
    A3 --> O4
    O4 --> A4
    A4 --> O5
    O5 --> A5
    A5 --> O6
```

---

## 3. TO-BE Process: Automated Registration

### 3.1 High-Level Process

```mermaid
flowchart TB
    subgraph Start
        A((Start))
    end
    
    subgraph TaskPrep["Phase 1: Preparation (Automated)"]
        B["🤖 Task 2: Load User Data from file"]
        C["🤖 Task 3: Buy Email via API"]
        D["🤖 Task 4: Generate Random Proxy"]
    end
    
    subgraph TaskLog["Phase 2: Logging"]
        E["🤖 Task 5: Save PENDING to Excel"]
    end
    
    subgraph TaskAuto["Phase 3: Automation"]
        F["🤖 Launch Camoufox Browser"]
        G["🤖 Step 1: Create Account (Auto-fill)"]
        H{Captcha?}
        I["⏸️ PAUSE: Manual Captcha"]
        J["🤖 Step 3: Auto Get Email OTP"]
        K["🤖 Auto Enter OTP"]
        L{Phone Required?}
        M["⏸️ PAUSE: Manual Phone Verify"]
        N["🤖 Step 4: Accept Terms"]
        O["🤖 Step 5: 2FA Setup"]
        P["🤖 Step 7: Fill Profile & Bank"]
        Q["🤖 Step 8: Tax Interview"]
        R["🤖 Step 9: Questionnaire"]
    end
    
    subgraph TaskComplete["Phase 4: Completion"]
        S{"Success?"}
        T["🤖 Task 5: Update SUCCESS"]
        U["🤖 Task 5: Update FAILED"]
    end
    
    subgraph End
        V((End))
    end
    
    A --> B --> C --> D --> E --> F --> G --> H
    H -->|Yes| I --> J
    H -->|No| J
    J --> K --> L
    L -->|Yes| M --> N
    L -->|No| N
    N --> O --> P --> Q --> R --> S
    S -->|Yes| T --> V
    S -->|No| U --> V
    
    style B fill:#90EE90
    style C fill:#90EE90
    style D fill:#90EE90
    style E fill:#90EE90
    style F fill:#90EE90
    style G fill:#90EE90
    style J fill:#90EE90
    style K fill:#90EE90
    style N fill:#90EE90
    style O fill:#90EE90
    style P fill:#90EE90
    style Q fill:#90EE90
    style R fill:#90EE90
    style T fill:#90EE90
    style U fill:#90EE90
    style I fill:#FFD700
    style M fill:#FFD700
```

**Legend:**
- 🟢 Green = Fully Automated
- 🟡 Yellow = Manual Intervention Required

### 3.2 Automation Coverage

| Step | Manual (AS-IS) | Automated (TO-BE) | Time Saved |
|------|----------------|-------------------|------------|
| Create email | ❌ Manual | ✅ API call | 5-7 min |
| Load user data | ❌ Manual copy | ✅ File parsing | 3-5 min |
| Fill registration | ❌ 20+ fields | ✅ Auto-fill | 10-15 min |
| Get Email OTP | ❌ Check inbox | ✅ API polling | 2-5 min |
| Enter OTP | ❌ Manual | ✅ Auto-fill | 1 min |
| Solve Captcha | ❌ Manual | ⏸️ Still manual | 0 |
| Phone verify | ❌ Manual | ⏸️ Still manual | 0 |
| Fill Tax form | ❌ Manual | ✅ Auto-fill | 5-7 min |
| Record results | ❌ Manual | ✅ Auto Excel | 3-5 min |
| **Total Time** | **30-45 min** | **8-12 min** | **~25 min** |

### 3.3 Detailed Swim Lane Diagram

```mermaid
flowchart TB
    subgraph Operator["👤 Operator"]
        O1[Run python main.py]
        O2[👁️ Monitor progress]
        O3[🧩 Solve Captcha when prompted]
        O4[📱 Phone verify if needed]
        O5[📊 Review Excel results]
    end
    
    subgraph System["🤖 Automation System"]
        S1[Task 2: Load user data]
        S2[Task 3: Buy email from API]
        S3[Task 4: Start Camoufox]
        S4[Auto-fill registration]
        S5[Poll for Email OTP]
        S6[Auto-fill OTP]
        S7[Complete Tax & Questionnaire]
        S8[Task 5: Update Excel]
    end
    
    subgraph ExternalAPI["🌐 External APIs"]
        E1[DongvanFB: Provide email]
        E2[DongvanFB: Return OTP]
        E3[Decodo: Provide proxy]
    end
    
    subgraph Amazon["🛒 Amazon"]
        A1[Registration page]
        A2[Send Email OTP]
        A3[Captcha challenge]
        A4[Phone verification]
        A5[Accept application]
    end
    
    O1 --> S1
    S1 --> S2
    S2 --> E1
    E1 --> S3
    S3 --> E3
    E3 --> S4
    S4 --> A1
    A1 --> A2
    A2 --> S5
    S5 --> E2
    E2 --> S6
    S6 --> A3
    A3 --> O3
    O3 --> A4
    A4 --> O4
    O4 --> S7
    S7 --> A5
    A5 --> S8
    S8 --> O5
```

---

## 4. Sub-Process: Email OTP Handling

### 4.1 BPMN Diagram

```mermaid
flowchart TB
    A((Start)) --> B[Initialize polling]
    B --> C[Set timeout = 120s]
    C --> D[Set interval = 10s]
    D --> E{Time elapsed > timeout?}
    E -->|Yes| F[Return None - Timeout]
    E -->|No| G[Call OTP API]
    G --> H{status == true?}
    H -->|Yes| I[Extract OTP code]
    I --> J[Return OTP]
    H -->|No| K[Log waiting message]
    K --> L[Sleep for interval]
    L --> E
    F --> M((End - Failure))
    J --> N((End - Success))
    
    style N fill:#90EE90
    style M fill:#FF6B6B
```

### 4.2 Sequence Diagram

```mermaid
sequenceDiagram
    participant S as System
    participant API as DongvanFB API
    participant A as Amazon
    
    S->>A: Submit registration form
    A->>A: Generate OTP
    A-->>API: Send OTP email (background)
    
    loop Every 10 seconds (max 120s)
        S->>API: POST /api/get_code_oauth2
        alt OTP Available
            API-->>S: {status: true, code: "123456"}
            S->>A: Fill OTP field
            S->>A: Click Verify button
        else OTP Not Available Yet
            API-->>S: {status: false, data: "Waiting..."}
            S->>S: Wait 10 seconds
        end
    end
```

---

## 5. Sub-Process: Error Handling with Timeout

### 5.1 Interactive Prompt Flow

```mermaid
flowchart TB
    A((Action Start)) --> B[Execute action with timeout]
    B --> C{Completed within timeout?}
    C -->|Yes| D[Continue to next step]
    C -->|No| E[Display timeout prompt]
    E --> F{User choice?}
    F -->|Enter/c| D
    F -->|r| B
    F -->|q| G[Raise Exception]
    G --> H[Update FAILED status]
    H --> I((End - Abort))
    D --> J((End - Success))
    
    style J fill:#90EE90
    style I fill:#FF6B6B
```

### 5.2 Timeout Handling Code Mapping

```
Prompt Display:
⏱️  TIMEOUT - Bước X: <step_name>
   Đã đợi 30s nhưng chưa hoàn thành
======================================================================
   👉 Nhấn Enter hoặc 'c': Continue (tiếp tục bước tiếp)
   👉 Nhấn 'r': Retry (thử lại bước này)
   👉 Nhấn 'q': Quit (thoát script)
======================================================================
```

**Traceability:**
- File: `task4_camoufox_workflow.py`
- Function: `wait_with_timeout()`
- Lines: 34-80

---

## 6. Process Metrics Comparison

### 6.1 Time Comparison

```mermaid
gantt
    title Process Time Comparison
    dateFormat mm:ss
    section Manual (AS-IS)
    Create Email     :a1, 00:00, 7m
    Fill Form        :a2, after a1, 15m
    Wait OTP         :a3, after a2, 5m
    Captcha          :a4, after a3, 2m
    Tax Interview    :a5, after a4, 7m
    Record           :a6, after a5, 5m
    section Automated (TO-BE)
    Buy Email API    :b1, 00:00, 30s
    Auto-fill        :b2, after b1, 3m
    Auto OTP         :b3, after b2, 1m
    Captcha          :b4, after b3, 2m
    Auto Tax         :b5, after b4, 2m
    Auto Record      :b6, after b5, 10s
```

### 6.2 Efficiency Metrics

| Metric | AS-IS | TO-BE | Improvement |
|--------|-------|-------|-------------|
| Time per account | 35 min | 10 min | **71% faster** |
| Accounts per hour | 1.7 | 6 | **3.5x more** |
| Manual effort | 100% | 20% | **80% reduction** |
| Error rate | 15% | 5% | **67% reduction** |
| Scalability | Low | High | **Significant** |

---

## 7. Exception Handling Processes

### 7.1 Phone Verification Required

```mermaid
flowchart TB
    A[System detects phone verification page] --> B[Take screenshot]
    B --> C[Display pause message]
    C --> D[Wait for operator input]
    D --> E{Operator presses Enter?}
    E -->|Yes| F[Continue automation]
    E -->|Timeout| G[Update status to REQUIRE_PHONE]
    G --> H[Exit gracefully]
    F --> I[Resume normal flow]
```

### 7.2 Captcha Challenge

```mermaid
flowchart TB
    A[System encounters Captcha] --> B[Display pause message]
    B --> C[Wait for iframe to disappear]
    C --> D{Captcha solved?}
    D -->|Yes, within 30s| E[Continue to next step]
    D -->|No, timeout| F[Show retry prompt]
    F --> G{User choice}
    G -->|Retry| C
    G -->|Continue| E
    G -->|Quit| H[Abort process]
```

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-28  
**Author:** Business Analyst
