# 📊 Activity Diagrams
## MapleStory M Auto Flow Launcher

---

## 1. Main Flow Execution Activity

### 1.1 Complete Flow Activity Diagram

```mermaid
flowchart TD
    Start([Start Flow]) --> LoadConfig[Load Configuration]
    LoadConfig --> SelectAccount{Select Account Group}
    
    SelectAccount --> Acc1[accounts_1]
    SelectAccount --> Acc2[accounts_2]
    SelectAccount --> Acc3[accounts_3]
    
    Acc1 --> GetServers[Get Available Servers]
    Acc2 --> GetServers
    Acc3 --> GetServers
    
    GetServers --> SelectServer{Select Server}
    SelectServer --> A1[A1]
    SelectServer --> US[US]
    SelectServer --> EU[EU]
    SelectServer --> A2[A2 Group]
    
    A1 --> RunFlow[run_common_flow]
    US --> RunFlow
    EU --> RunFlow
    A2 --> RunFlow
    
    subgraph FlowExec["Flow Execution"]
        RunFlow --> LoginCheck{Login Script}
        LoginCheck -->|Success| StartGame[Execute start.py]
        LoginCheck -->|Fail| ChangeServer[Execute change_server]
        ChangeServer --> LoginCheck
        
        StartGame --> RandomG1[Randomize Group 1]
        RandomG1 --> ExecG1[Execute AB, Guild, Dim]
        ExecG1 --> CC1[Change Character 1]
        
        CC1 --> RandomG2[Randomize Group 2]
        RandomG2 --> ExecG2[Execute AB2, Guild2, Dim2]
        ExecG2 --> CC2[Change Character 2]
        
        CC2 --> FilterOpt[Filter Optional Scripts]
        FilterOpt --> RandomOpt[Random Select Optional]
        RandomOpt --> ExecOpt[Execute Selected]
        ExecOpt --> Logout[Execute Logout]
    end
    
    Logout --> LogResults[Log Results]
    LogResults --> DisplayTime[Display Time Summary]
    DisplayTime --> End([Flow Complete])
```

---

## 2. Script Execution Activity

### 2.1 run_sikuli_script Activity

```mermaid
flowchart TD
    Start([Call run_sikuli_script]) --> BuildPath[Build Script Path]
    BuildPath --> CheckPath{Script Exists?}
    
    CheckPath -->|No| LogError[Log: Script not found]
    LogError --> ReturnError[Return 1]
    ReturnError --> End1([End - Failed])
    
    CheckPath -->|Yes| BuildCmd[Build Java Command]
    BuildCmd --> LogStart[Log: Running script]
    LogStart --> Execute[subprocess.call]
    
    Execute --> CheckResult{Exit Code = 0?}
    CheckResult -->|Yes| LogSuccess[Log: Success]
    CheckResult -->|No| LogFail[Log: Failed]
    
    LogSuccess --> PrintSuccess[Print Green Result]
    LogFail --> PrintFail[Print Red Result]
    
    PrintSuccess --> Return0[Return 0]
    PrintFail --> Return1[Return 1]
    
    Return0 --> End2([End - Success])
    Return1 --> End3([End - Failed])
```

---

## 3. Auto Battle Process Activity

### 3.1 AutoBattle.run() Activity

```mermaid
flowchart TD
    Start([Start Auto Battle]) --> Init[Initialize Patterns]
    Init --> GetPriority[Get Priority Regions]
    
    GetPriority --> LoopStart{More Regions?}
    LoopStart -->|No| Summary[Print Summary]
    Summary --> End([End])
    
    LoopStart -->|Yes| CheckTaikhoan{Check Taikhoan Pattern}
    CheckTaikhoan -->|Found| SkipRegion[Skip Region]
    SkipRegion --> LoopStart
    
    CheckTaikhoan -->|Not Found| CheckActive{Already Active?}
    CheckActive -->|Yes| LoopStart
    CheckActive -->|No| ProcessRegion[Process Region]
    
    subgraph RegionProcess["process_region()"]
        ProcessRegion --> CheckPopup[Check Popups]
        CheckPopup -->|Found| ClosePopup[Click All Popups]
        ClosePopup --> CheckPopup
        
        CheckPopup -->|No Popup| FindAuto{Find Auto Button}
        FindAuto -->|Found| ClickAuto[Click Auto]
        ClickAuto --> WaitUse[Check Use Button]
        WaitUse --> RightClick[Right Click Center]
        RightClick --> RegionSuccess[Mark Success]
        
        FindAuto -->|Not Found| IncCount[Increment Counter]
        IncCount --> CheckMax{Max Attempts?}
        CheckMax -->|No| Sleep[Sleep 0.5s]
        Sleep --> CheckPopup
        CheckMax -->|Yes| AskRetry{Ask User Retry?}
        AskRetry -->|Yes| ResetCount[Reset Counter]
        ResetCount --> CheckPopup
        AskRetry -->|No| RegionFail[Skip Region]
    end
    
    RegionSuccess --> LoopStart
    RegionFail --> LoopStart
```

---

## 4. Popup Handling Activity

### 4.1 check_and_close_popups Activity

```mermaid
flowchart TD
    Start([Check Popups]) --> CheckDead[Find Dead Images]
    
    CheckDead -->|Found| ClickDead[Click All Dead Matches]
    ClickDead --> SetFlag1[popup_closed = True]
    SetFlag1 --> CheckBlue
    
    CheckDead -->|Not Found| CheckBlue[Find X_blue Pattern]
    CheckBlue -->|Found| ClickBlue[Click All Matches]
    ClickBlue --> SetFlag2[popup_closed = True]
    SetFlag2 --> CheckX
    
    CheckBlue -->|Not Found| CheckX[Find X_button Pattern]
    CheckX -->|Found| ClickX[Click All Matches]
    ClickX --> SetFlag3[popup_closed = True]
    SetFlag3 --> CheckOther
    
    CheckX -->|Not Found| CheckOther[Find Other X Patterns]
    CheckOther -->|Found| ClickOther[Click All]
    ClickOther --> SetFlag4[popup_closed = True]
    SetFlag4 --> CheckConfirm
    
    CheckOther -->|Not Found| CheckConfirm[Find Confirm Button]
    CheckConfirm -->|Found| ClickConfirm[Click Confirm]
    ClickConfirm --> ReturnTrue[Return True]
    
    CheckConfirm -->|Not Found| ReturnFalse[Return False]
    
    ReturnTrue --> End([End])
    ReturnFalse --> End
```

---

## 5. Master Flow Activity

### 5.1 Multi-Server Sequential Execution

```mermaid
flowchart TD
    Start([Start Master Flow]) --> ParseOrder[Parse Server Order]
    ParseOrder --> StartTimer[Start Timer]
    
    StartTimer --> DisplayOrder[Display Flow Order]
    DisplayOrder --> LoopStart{More Servers?}
    
    LoopStart -->|No| CalcTime[Calculate Total Time]
    CalcTime --> PrintSummary[Print Summary]
    PrintSummary --> End([All Flows Complete])
    
    LoopStart -->|Yes| CheckFirst{First Server?}
    CheckFirst -->|Yes| RunServer[run_common_flow]
    
    CheckFirst -->|No| CheckA2{Both are A2?}
    CheckA2 -->|Yes| ShortDelay[Delay 5-10s]
    CheckA2 -->|No| LongDelay[Delay 10-30s]
    
    ShortDelay --> RunServer
    LongDelay --> RunServer
    
    RunServer --> LogComplete[Log: Flow Complete]
    LogComplete --> NextServer[Move to Next]
    NextServer --> LoopStart
```

---

## 6. Configuration Activity

### 6.1 Configure Optional Scripts Activity

```mermaid
flowchart TD
    Start([Enter Config]) --> ClearScreen[Clear Screen]
    ClearScreen --> PrintHeader[Print Header]
    
    PrintHeader --> EnsureScripts[Ensure All Scripts in Config]
    EnsureScripts --> DisplayList[Display Script List]
    
    DisplayList --> WaitInput[Wait for Input]
    WaitInput --> CheckExit{Input = 0?}
    
    CheckExit -->|Yes| SaveConfig[Save to JSON]
    SaveConfig --> PrintSaved[Print Saved Message]
    PrintSaved --> End([Return])
    
    CheckExit -->|No| ParseIndex[Parse Index]
    ParseIndex --> CheckValid{Valid Index?}
    
    CheckValid -->|No| PrintError[Print Error]
    PrintError --> WaitInput
    
    CheckValid -->|Yes| ToggleStatus[Flip 0↔1]
    ToggleStatus --> PrintMessage{New Status?}
    
    PrintMessage -->|1| PrintOn[Print: BẬT Green]
    PrintMessage -->|0| PrintOff[Print: TẮT Red]
    
    PrintOn --> WaitInput
    PrintOff --> WaitInput
```

---

## 7. Activity Swimlane Diagram

### 7.1 Complete Flow with Actors

```mermaid
flowchart TD
    subgraph Player["👤 Player"]
        P1[Select Flow Type]
        P2[Select Account/Server]
        P3[Wait for Completion]
        P4[Handle Errors]
    end
    
    subgraph Launcher["🖥️ Main Launcher"]
        L1[Show Menus]
        L2[Load Config]
        L3[Orchestrate Flow]
        L4[Log Results]
    end
    
    subgraph Sikuli["🤖 Sikuli Engine"]
        S1[Execute Scripts]
        S2[Image Recognition]
        S3[Click Actions]
    end
    
    subgraph Emulator["📱 Emulator"]
        E1[Receive Clicks]
        E2[Update UI]
        E3[Send to Server]
    end
    
    P1 --> L1
    L1 --> P2
    P2 --> L2
    L2 --> L3
    L3 --> S1
    S1 --> S2
    S2 --> S3
    S3 --> E1
    E1 --> E2
    E2 --> E3
    E3 --> S2
    S1 --> L4
    L4 --> P3
    P3 --> P4
```

---

*Document maintained in: `BA_Portfolio/03_System_Design/06_activity_diagram.md`*
