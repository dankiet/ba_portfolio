# 🔄 State Diagrams
## MapleStory M Auto Flow Launcher

---

## 1. Flow Execution State Machine

### 1.1 Main Flow States

```mermaid
stateDiagram-v2
    [*] --> Idle: Launch Application
    
    Idle --> SelectingAccountGroup: User selects flow
    SelectingAccountGroup --> SelectingServer: Account group selected
    SelectingServer --> Initializing: Server selected
    
    Initializing --> LoggingIn: Config loaded
    
    LoggingIn --> LoginSuccess: Login OK
    LoggingIn --> LoginFailed: Login Error
    LoginFailed --> ChangingServer: Auto retry
    ChangingServer --> LoggingIn: Server changed
    ChangingServer --> FlowAborted: Change failed
    
    LoginSuccess --> ExecutingTasks: Start game
    
    state ExecutingTasks {
        [*] --> Group1
        Group1 --> CharSwitch1: Group 1 complete
        CharSwitch1 --> Group2: Switch done
        Group2 --> CharSwitch2: Group 2 complete
        CharSwitch2 --> OptionalTasks: Switch done
        OptionalTasks --> LoggingOut: Optional complete
        LoggingOut --> [*]: Logged out
    }
    
    ExecutingTasks --> TaskFailed: Script error
    TaskFailed --> ExecutingTasks: User continues
    TaskFailed --> FlowAborted: User stops
    
    ExecutingTasks --> FlowComplete: All done
    FlowComplete --> Idle: Return to menu
    FlowAborted --> Idle: Return to menu
```

### 1.2 State Descriptions

| State | Description | Entry Action | Exit Action |
|-------|-------------|--------------|-------------|
| **Idle** | Waiting at main menu | Display menu | Clear screen |
| **SelectingAccountGroup** | User choosing account 1/2/3 | Show options | Store selection |
| **SelectingServer** | User choosing server | Load available servers | Store server |
| **Initializing** | Loading config | Load config.json | Log start |
| **LoggingIn** | Executing login script | Run account script | Check result |
| **LoginFailed** | Login unsuccessful | - | Trigger retry |
| **ChangingServer** | Retrying via server change | Run change_server | - |
| **ExecutingTasks** | Running gameplay scripts | Start timer | Stop timer |
| **TaskFailed** | A script failed | Show error | Ask user |
| **FlowComplete** | All tasks done | Calculate time | Show summary |
| **FlowAborted** | User cancelled or error | Log error | - |

---

## 2. Script Execution State Machine

### 2.1 Single Script States

```mermaid
stateDiagram-v2
    [*] --> Pending: Script queued
    
    Pending --> Validating: Start execution
    Validating --> PathValid: Script exists
    Validating --> PathInvalid: Script not found
    
    PathInvalid --> Failed: Log error
    Failed --> [*]: Return 1
    
    PathValid --> Running: subprocess.call()
    Running --> Succeeded: Exit code 0
    Running --> Failed: Exit code != 0
    
    Succeeded --> [*]: Return 0
```

### 2.2 Transitions

| From | Event | To | Guard |
|------|-------|-----|-------|
| Pending | execute() | Validating | - |
| Validating | path_check | PathValid | os.path.exists() = True |
| Validating | path_check | PathInvalid | os.path.exists() = False |
| Running | complete | Succeeded | exit_code == 0 |
| Running | complete | Failed | exit_code != 0 |

---

## 3. Region Processing State Machine

### 3.1 AutoBattle Region States

```mermaid
stateDiagram-v2
    [*] --> Unprocessed: Region identified
    
    Unprocessed --> Checking: Start processing
    Checking --> Skipped: Taikhoan found
    Skipped --> [*]: Skip region
    
    Checking --> Active: No taikhoan
    
    state Active {
        [*] --> CheckingPopups
        CheckingPopups --> ClosingPopup: Popup found
        ClosingPopup --> CheckingPopups: Popup closed
        
        CheckingPopups --> SearchingAuto: No popup
        SearchingAuto --> ClickingAuto: Button found
        SearchingAuto --> WaitingRetry: Not found
        
        WaitingRetry --> CheckingPopups: Counter < max
        WaitingRetry --> AskingUser: Counter >= max
        
        AskingUser --> CheckingPopups: User retries
        AskingUser --> [*]: User skips
        
        ClickingAuto --> HandleUse: Auto clicked
        HandleUse --> RightClicking: Done
        RightClicking --> [*]: Success
    }
    
    Active --> Succeeded: Process complete
    Active --> TimedOut: Timeout reached
    TimedOut --> AskContinue: popAsk
    AskContinue --> Active: User retries
    AskContinue --> Failed: User cancels
    
    Succeeded --> [*]: Mark success
    Failed --> [*]: Mark failed
```

---

## 4. Configuration State Machine

### 4.1 Optional Script Config States

```mermaid
stateDiagram-v2
    [*] --> Viewing: Enter config menu
    
    Viewing --> WaitingInput: Display list
    
    WaitingInput --> Toggling: User enters number
    WaitingInput --> Saving: User enters 0
    
    Toggling --> StatusON: Was OFF, now ON
    Toggling --> StatusOFF: Was ON, now OFF
    
    StatusON --> Viewing: Show green message
    StatusOFF --> Viewing: Show red message
    
    Saving --> Saved: Config written
    Saved --> [*]: Return to config menu
```

### 4.2 Script Status Values

| Status | Value | Meaning | Visual |
|--------|-------|---------|--------|
| **Optional/Random** | 1 | May or may not run | 🟢 BẬT |
| **Fixed/Always** | 0 | Always runs | 🔴 TẮT |

---

## 5. Master Flow State Machine

### 5.1 Multi-Server Execution States

```mermaid
stateDiagram-v2
    [*] --> OrderSelected: User selects order
    
    OrderSelected --> AccountGroupSelected: Group chosen
    AccountGroupSelected --> Validating: Check scripts exist
    
    Validating --> Ready: All scripts found
    Validating --> InvalidOrder: Missing scripts
    InvalidOrder --> [*]: Show error
    
    Ready --> Processing: Start master flow
    
    state Processing {
        [*] --> ServerPending
        
        ServerPending --> Delaying: Not first server
        ServerPending --> RunningFlow: First server
        
        Delaying --> RunningFlow: Delay complete
        
        RunningFlow --> ServerComplete: Flow success
        RunningFlow --> ServerFailed: Flow error
        
        ServerComplete --> CheckMore: Log complete
        ServerFailed --> CheckMore: Continue anyway
        
        CheckMore --> ServerPending: More servers
        CheckMore --> [*]: All done
    }
    
    Processing --> Complete: All flows done
    Complete --> [*]: Show summary
```

---

## 6. ADB Script State Machine

### 6.1 Device Launch States

```mermaid
stateDiagram-v2
    [*] --> Reading: Start script
    
    Reading --> DevicesLoaded: File read OK
    Reading --> NoDevices: File not found
    NoDevices --> [*]: Exit
    
    DevicesLoaded --> ProcessingDevices: Loop start
    
    state ProcessingDevices {
        [*] --> DevicePending
        
        DevicePending --> Launching: Next device
        Launching --> LaunchSuccess: Command OK
        Launching --> LaunchFailed: Command error
        
        LaunchSuccess --> Waiting: Log success
        LaunchFailed --> Waiting: Log error
        
        Waiting --> DevicePending: Sleep 2s done
        
        DevicePending --> [*]: No more devices
    }
    
    ProcessingDevices --> Completed: All devices processed
    Completed --> [*]: Print completed
```

---

## 7. State Transition Summary

### 7.1 Critical State Transitions

| State Machine | Critical Transition | Trigger | Fallback |
|---------------|---------------------|---------|----------|
| Main Flow | LoggingIn → LoginFailed | Exit code != 0 | ChangingServer |
| Script Exec | Running → Failed | Exception | Return 1 |
| Region | Searching → WaitingRetry | Pattern not found | Ask user |
| Master Flow | RunningFlow → ServerFailed | Flow error | Continue next |

### 7.2 Error Recovery States

```mermaid
stateDiagram-v2
    [*] --> Normal
    
    Normal --> Error: Exception/Failure
    Error --> Recovery: Auto or User
    
    Recovery --> Retry: User chooses retry
    Recovery --> Skip: User chooses skip
    Recovery --> Abort: Critical error
    
    Retry --> Normal: Success
    Retry --> Error: Failed again
    Skip --> Normal: Continue next
    Abort --> [*]: Exit
```

---

*Document maintained in: `BA_Portfolio/03_System_Design/07_state_diagram.md`*
