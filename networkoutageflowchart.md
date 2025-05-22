```mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Network Issue Begins"]) --> B["Check Layer 1 Status"]
    B --> C["No Issues at Layer 1"] & D["Issue found at the Physical Layer"]
    D --> I["Fix the Problem"]
    C --> E["Check Layer 2 Status"]
    E --> G["No Issues at Layer 2"] & F["Issue found at the Data Link Layer"]
    F --> I
    G --> J["Check Layer 3 Status"]
    J --> L["No Issues at Layer 3"] & K["Issue at the Network Layer Found"]
    K --> I
    L --> N["Check Layer 4 Status"]
    N --> O["No Issues at Layer 4"] & P["Issue found at the Transport Layer"]
    P --> I
    O --> H["Check Layer 5 Status"]
    H --> M["Consider blaming the End User"]
    M --> Q@{ label: "Be nice and don't blame the End User" } & R["Blame the End User"]
    R --> S["Submit Ticket for Help Desk for Investigation"]
    Q --> T["Issue Found at the Session Layer"] & U["No Issues at Layer 5"]
    T --> I & V["Notify Help Desk of the Issue and Correction Used"]
    U --> Y["Check Layer 6 Status"]
    I --> X["Document actions taken"]
    Y --> Z["Issue Found at the Presentation Layer"] & AA["No Issue Found at Layer 6"]
    Z --> I & V
    AA --> W["Issue Falls Outside Net Ops Jurisdiction, Submit Ticket to Help Desk for Investigation"]
    W --> X
    n1["OSI Model Network Troubleshooting Flowchart"]
    n2["Assumes there is a limit to Net Ops desire to Troubleshoot. This is only half serious, please take this as unseriously as possible."]
    Q@{ shape: rect}
    n2@{ shape: text}
