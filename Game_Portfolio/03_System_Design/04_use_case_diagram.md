# 🎭 Use Case Diagram
## MapleStory M Auto Flow Launcher

---

## 1. System Context

```mermaid
flowchart TB
    subgraph External["External Entities"]
        Player[("👤 Player")]
        GameServer["🎮 Game Server<br/>(MapleStory M)"]
        Emulator["📱 Android Emulator"]
    end
    
    subgraph System["MapleStory M Auto Launcher"]
        Launcher["Main Launcher"]
    end
    
    Player -->|Interacts with| Launcher
    Launcher -->|Controls| Emulator
    Emulator <-->|Communicates| GameServer
```

---

## 2. Main Use Case Diagram (with System Boundary)

```mermaid
flowchart TB
    subgraph Actors["External Actors"]
        Player[("👤 Player")]
        SikuliEngine["🤖 Sikuli Engine"]
        ADB["📱 ADB Manager"]
    end
    
    subgraph SystemBoundary["═══════ System Boundary: MapleStory M Auto Launcher ═══════"]
        subgraph FlowMgmt["Flow Management"]
            UC1((UC-01<br/>Run Single Flow))
            UC2((UC-02<br/>Run Multi-Server Flow))
            UC3((UC-03<br/>Resume from Point))
        end
        
        subgraph ConfigMgmt["Configuration"]
            UC4((UC-04<br/>Configure Settings))
            UC5((UC-05<br/>Toggle Optional Scripts))
        end
        
        subgraph DeviceCtrl["Device Control"]
            UC6((UC-06<br/>Launch Apps via ADB))
            UC7((UC-07<br/>View ADB Status))
        end
        
        subgraph ScriptExec["Script Execution"]
            UC8((UC-08<br/>Execute Account Script))
            UC9((UC-09<br/>Execute Gameplay Script))
            UC10((UC-10<br/>Handle Popups))
        end
    end
    
    Player --> UC1
    Player --> UC2
    Player --> UC3
    Player --> UC4
    Player --> UC5
    Player --> UC6
    Player --> UC7
    
    UC1 --> UC8
    UC1 --> UC9
    UC2 --> UC1
    
    UC8 --> SikuliEngine
    UC9 --> SikuliEngine
    UC10 --> SikuliEngine
    
    UC6 --> ADB
    UC7 --> ADB
    
    UC9 -.->|<<include>>| UC10
    
    style SystemBoundary fill:#f5f5f5,stroke:#333,stroke-width:3px
```

---

## 3. Use Case List

| UC ID | Use Case Name | Primary Actor | Description |
|-------|---------------|---------------|-------------|
| UC-01 | Run Single Flow | Player | Chạy automation flow cho một server |
| UC-02 | Run Multi-Server Flow | Player | Chạy tuần tự nhiều server theo thứ tự tùy chọn |
| UC-03 | Resume from Point | Player | Tiếp tục flow từ một điểm cụ thể |
| UC-04 | Configure Settings | Player | Cấu hình đường dẫn và delays |
| UC-05 | Toggle Optional Scripts | Player | Bật/tắt tính năng random cho scripts |
| UC-06 | Launch Apps via ADB | Player | Khởi động app trên emulators qua ADB |
| UC-07 | View ADB Status | Player | Xem trạng thái devices |
| UC-08 | Execute Account Script | Sikuli Engine | Chạy script đăng nhập/đổi server |
| UC-09 | Execute Gameplay Script | Sikuli Engine | Chạy script gameplay (AB, Guild, etc.) |
| UC-10 | Handle Popups | Sikuli Engine | Đóng popups tự động |

---

## 4. Use Case Relationships

### 4.1 Include Relationships

```mermaid
flowchart LR
    subgraph "Include Relationships"
        UC1((UC-01<br/>Run Single Flow))
        UC8((UC-08<br/>Execute Account Script))
        UC9((UC-09<br/>Execute Gameplay Script))
        UC10((UC-10<br/>Handle Popups))
        
        UC1 -->|<<include>>| UC8
        UC1 -->|<<include>>| UC9
        UC9 -->|<<include>>| UC10
    end
```

### 4.2 Extend Relationships

```mermaid
flowchart LR
    subgraph "Extend Relationships"
        UC1((UC-01<br/>Run Single Flow))
        UC_EXT1((Change Server<br/>on Login Fail))
        UC_EXT2((Retry on<br/>Timeout))
        
        UC_EXT1 -->|<<extend>>| UC1
        UC_EXT2 -->|<<extend>>| UC1
    end
```

---

## 5. Detailed Actor Descriptions

### 5.1 Primary Actors

| Actor | Description | Goals |
|-------|-------------|-------|
| **Player** | Người chơi điều khiển launcher | Tự động hóa daily tasks, tiết kiệm thời gian |

### 5.2 Secondary Actors

| Actor | Description | Role |
|-------|-------------|------|
| **Sikuli Engine** | Java-based image recognition | Thực thi automation scripts |
| **ADB Manager** | Android Debug Bridge | Điều khiển emulators |
| **Game Server** | Nexon MapleStory M server | Xử lý game logic |

---

## 6. Use Case Priority

```mermaid
quadrantChart
    title Use Case Priority Matrix
    x-axis Low Frequency --> High Frequency
    y-axis Low Business Value --> High Business Value
    quadrant-1 High Priority
    quadrant-2 Medium-High Priority
    quadrant-3 Low Priority
    quadrant-4 Medium Priority
    
    "Run Single Flow": [0.9, 0.9]
    "Run Multi-Server": [0.7, 0.85]
    "Execute Gameplay": [0.95, 0.8]
    "Handle Popups": [0.9, 0.7]
    "Configure Settings": [0.2, 0.6]
    "Toggle Optional": [0.3, 0.5]
    "Launch ADB": [0.4, 0.4]
```

---

## 7. Subsystem Use Cases

### 7.1 Account Management Subsystem

```mermaid
flowchart TB
    Player[("👤 Player")]
    
    subgraph "Account Management"
        A1((Login to Server))
        A2((Change Server))
        A3((Select Account Group))
    end
    
    Player --> A1
    Player --> A2
    Player --> A3
    
    A2 -.->|extends| A1
```

### 7.2 Gameplay Automation Subsystem

```mermaid
flowchart TB
    Sikuli[("🤖 Sikuli Engine")]
    
    subgraph "Gameplay Automation"
        G1((Start Game))
        G2((Run Auto Battle))
        G3((Run Guild Tasks))
        G4((Run Dungeon))
        G5((Change Character))
        G6((Logout))
    end
    
    Sikuli --> G1
    Sikuli --> G2
    Sikuli --> G3
    Sikuli --> G4
    Sikuli --> G5
    Sikuli --> G6
```

---

*Document maintained in: `BA_Portfolio/03_System_Design/04_use_case_diagram.md`*
