# 🤖 Autonomous Agentic AI Copywriter & Market Research Engine

An enterprise-grade, domain-constrained Agentic AI application engineered to automate market research, trend analysis, and multi-channel content generation specifically for the Facilities Services and Maintenance sector. Powered by LangChain, the core engine leverages dynamic tool-calling layers to crawl the web, synthesize live industry insights, and compile structured marketing blueprints without human data-entry overhead.

---

### 📐 Architectural Parameters & Scope
* **Role:** Lead AI Solutions Developer & Knowledge Engineer
* **Core Framework:** LangChain (Tool Calling, Routing, & Context Assemblers)
* **Agentic Tools:** DuckDuckGo Search API Component + Wikipedia Search Parser
* **Domain Guardrails:** Hard-coded prompt templates optimized strictly for corporate Facilities Management (B2B Commercial Cleaning, MEP Engineering, Property Maintenance).

---

### 🗺️ System Data-Flow & Tool-Orchestration Architecture

The system uses a decoupled layout. The frontend UI transmits target search boundaries to a FastAPI gateway, which initializes an autonomous LangChain execution loop to pull live web insights, process context in memory, and deliver a completed data block in a single HTTP POST request.

```mermaid
graph TB

    %% =========================================================
    %% 1. PIPELINE NODE DEFINITIONS (High Contrast Styling)
    %% =========================================================
    User[👤 Client User Interface <br> HTML5 / jQuery State Machine]
    
    FastAPI{⚡ FastAPI Service Gateway <br> Router Core Layer}
    
    Prompt[📝 Domain-Constrained Prompt <br> Facilities Management Rules]
    
    LangChain[🔀 LangChain Orchestration Core <br> Dynamic Tool Router]
    
    Tool_DDG[🔍 DuckDuckGo API Wrapper <br> Live Web Index Scraper]
    Tool_Wiki[📚 Wikipedia API Layer <br> Historical Pattern Matcher]
    
    Context[🧠 Context Synthesis Engine <br> Information Merging Layer]
    
    LLM[🚀 Target Inference Core <br> Model Processing Engine]
    
    Output[📤 Atomic JSON Content Payload]

    %% =========================================================
    %% 2. LINEAR STEP-BY-STEP DATAFLOW (Error-Free Syntax)
    %% =========================================================
    User-->|1. Submit Research Topic & Parameters|FastAPI
    FastAPI-->|2. Inject Hardcoded Sector Guardrails|Prompt
    Prompt-->|3. Initialize Agent State Loop|LangChain
    
    LangChain-->|4A. Conditional Web Scrape Request|Tool_DDG
    LangChain-->|4B. Conditional Fact Check Request|Tool_Wiki
    
    Tool_DDG-->|5A. Return Live Search Tokens|Context
    Tool_Wiki-->|5B. Return Encyclopedic Reference String|Context
    
    Context-->|6. Route Compressed In-Context Window|LangChain
    LangChain-->|7. Pass Augmented Payload Block|LLM
    LLM-->|8. Process Full Structural Copy Text Loop|FastAPI
    FastAPI-->|9. Assemble Final Marketing Content Array|Output
    Output-->|10. Render Complete Text View on Dashboard|User

    %% =========================================================
    %% 3. REFINED GRAPH ACCENTS (Dark-Mode Harmony)
    %% =========================================================
    classDef default fill:#1a1d24,stroke:#4a5568,stroke-width:1px,color:#ffffff;
    
    style FastAPI fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#ffffff
    style LangChain fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#ffffff
    
    style LLM fill:#062040,stroke:#3b82f6,stroke-width:2px,color:#ffffff
    style Context fill:#062f21,stroke:#10b981,stroke-width:2px,color:#ffffff
    
    style Tool_DDG fill:#272510,stroke:#eab308,stroke-width:2px,color:#ffffff
    style Tool_Wiki fill:#272510,stroke:#eab308,stroke-width:2px,color:#ffffff
```

---

### 🚀 Key Technical Indicators & Engineering Implementations

* **Domain-Constrained Prompt Engineering:** The LLM's system state machine is strictly locked down using custom prompt templates. The agent rejects requests outside the Facilities Services matrix, guaranteeing highly professional text generation tailored specifically for B2B engineering platforms.
* **Autonomous Multi-Tool Orchestration:** Implements dynamic query analysis via LangChain. The engine intelligently judges when to query the live web index via DuckDuckGo for trending facilities problems or parse Wikipedia for operational standards definitions.
* **Decoupled Full-Stack Architecture:** Exposes non-blocking REST endpoints via FastAPI to receive web parameters from an optimized HTML5/jQuery interface, delivering structured text arrays in a single, stable atomic payload.

---

### 📂 Repository File System Directory Layout

```text
├── .env.template          # Global API key configuration blueprint
├── requirements.txt       # Version-locked environment dependencies
├── main.py                # Primary FastAPI gateway execution entrypoint
├── app/
│   ├── static/            # Frontend Web Layer (HTML5, Custom CSS, jQuery App Scripts)
│   ├── prompts.py         # 📝 Domain-specific system templates for Facilities Management
│   ├── tools.py           # LangChain custom DuckDuckGo and Wikipedia lookup scripts
│   └── agent.py           # Core agent routing execution graph logic
```

---

### 🚀 Local Quick-Start Workspace Execution

#### 1. Clone and Navigate to Infrastructure Workspace
```bash
git clone https://github.com
cd agentic-ai-copywriter
```

#### 2. Establish Environment File Configuration
```bash
cp .env.template .env
```
*Open `.env` and populate your target LLM model API tokens.*

#### 3. Start the Global Application Gateway
```bash
python main.py
```
*Open your local web browser to access the interactive full-stack market research dashboard dashboard.*
