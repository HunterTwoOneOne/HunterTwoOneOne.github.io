<H1> A Network Outage Troubleshooting Flowchart </H1>

**This is intended to be taken very unseriously. Further depth on WHAT the checking of Layers intails is not present. Process is simply to follow the OSI Model from Layer to Layer either finding the issue or not and taking actions based on the findings. Generally, once at the 7th Layer, AKA the Application Layer, the Network Team should be passing along the findings to the Help Desk as this is the Layer that End Users are at. Obviously, if you are fixing this issue in the real world and have troubleshooted the problem all the way to Layer you're probably not going to just give up and pass the problem to the Help Desk, you'll fix it for them and document the findings.**

**At each junction, having found or not found the issue, the next step is clear. Correct the issue if it is found, or move to the next layer. The OSI Model is very clear about the process as if the issue isn't at the cables and power, it's more in depth and you check data transmission as the cause next. This carries on until you've expended pretty much all options BUT the final layer, the Application Layer, and you're likely dealing with a service issue or a poorly functioning End User machine. The final part of the chart is to document everything. This is important in the field in the case of you wanting to go back and see what you did or another person wants to see what was done. Good written explanations of your troubleshooting can be** *VERY* **important if you have to report to somebody on the issue so you have material to refer to.**

***For more information about <a href="https://en.wikipedia.org/wiki/OSI_model"> The OSI Model </a> use the link provided to the Wikipedia page on the subject.***

*The OSI Model is critical to all Network professionals, as it is one of the tools used for fixing problems we encounter on a day to day basis in our work. This Flowchart is effectively the slow way of troubleshooting an issue though, as in the field, you may not even check certain layers as the available information around the outage or disruption can already indicate a likely cause. By the book, you're supposed to go as the flow chart shows. It may not be correct as the Certifications would like professionals to operate, but as you gain expereince, you often will not need to check things you're able to rule out.*


```mermaid
---
config:
  theme: redux
---
flowchart TB
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
    H --> M[" CONSIDER blaming the End User"]
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