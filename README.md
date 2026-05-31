# 🤖 Autonomous Agentic AI Copywriter & Market Research Engine

An enterprise-grade, domain-constrained Agentic AI application engineered to automate market research, trend analysis, and multi-channel content generation specifically for the Facilities Services and Maintenance sector. Powered by LangChain, the core engine leverages dynamic tool-calling layers to crawl the web, synthesize live industry insights, and stream structured B2B copy text blocks over full-duplex WebSocket connections.

---

### 📐 Architectural Parameters & System Scope
* **Role:** Lead Full-Stack AI Engineer & Knowledge Architect
* **Core Orchestrator:** LangChain `create_tool_calling_agent` & `AgentExecutor` (Max Iterations: 3)
* **Agentic Toolkit:** DuckDuckGo Web Search Engine + Character-Constrained Wikipedia API Parser (Max Chars: 221)
* **State Delivery Engine:** Asynchronous Stateful WebSockets (`ws://`) via FastAPI
* **Output Validation Schema:** Pydantic Object Parsing (`Title`, `Response`, `sources`, `tools_used`)
* **Prompt-Driven Domain Guardrails:** In-context System Prompt Instruction Matrices optimized strictly for corporate Facilities Management (B2B Commercial Cleaning, MEP Engineering, Property Maintenance).

---

### 🗺️ System Data-Flow & Tool-Orchestration Architecture

The system uses a highly decoupled layout. The frontend UI establishes a persistent WebSocket connection to the FastAPI gateway. The gateway parses the incoming prompt payload and triggers an active LangChain agent graph. The model dynamically evaluates query intent, decides whether to execute direct reasoning or trigger external API search tools, structures the final response array using a Pydantic parser, and transmits the compiled HTML/Markdown payload over the socket interface in a single execution frame.

```mermaid
graph TB

    %% =========================================================
    %% 1. PIPELINE NODE DEFINITIONS (High Contrast Styling)
    %% =========================================================
    User[👤 Client User Interface <br> HTML5 / Native WebSockets UI]
    
    FastAPI{⚡ FastAPI Service Gateway <br> Persistent WebSocket Connection}
    
    Prompt[📝 System Prompt & Context Layer <br> Sector Domain Bounds Check]
    
    LangChain[🔀 LangChain Tool Calling Agent <br> AgentExecutor Graphs]
    
    Tool_Direct[💬 Native LLM Weight Paths <br> Direct Response Reasoning]
    Tool_DDG[🔍 DuckDuckGo API Wrapper <br> Dynamic Web Scraper]
    Tool_Wiki[📚 Wikipedia API Layer <br> Max Cap: 221 Characters]
    
    Context[🧠 Pydantic Output Parser <br> Structural Fields Validation]
    
    LLM[🚀 Target Inference Core <br> Model Processing Engine]
    
    Output[📤 Real-Time WebSocket Frame Stream]

    %% =========================================================
    %% 2. LINEAR STEP-BY-STEP DATAFLOW (Stateless WebSocket Loop)
    %% =========================================================
    User-->|1. Transmit Prompt Query via ws://|FastAPI
    FastAPI-->|2. Evaluate Query Relevance & Bounds|Prompt
    Prompt-->|3. Initialize Tool-Calling Agent State|LangChain
    
    LangChain-->|4A. Route Direct Response|Tool_Direct
    LangChain-->|4B. Route Live Web Search|Tool_DDG
    LangChain-->|4C. Route Factual Lookup|Tool_Wiki
    
    Tool_Direct-->|5A. Pass Raw Prompt Context|Context
    Tool_DDG-->|5B. Return Scraped Search Metadata|Context
    Tool_Wiki-->|5C. Return Reference Text Tokens|Context
    
    Context-->|6. Validate JSON via Pydantic Schema|LangChain
    LangChain-->|7. Pass Structured Context Window|LLM
    LLM-->|8. Convert Generated Output to HTML / Markdown|FastAPI
    FastAPI-->|9. Broadcast Completed Response String Frame|Output
    Output-->|10. Render Complete Text View on Chat UI|User

    %% =========================================================
    %% 3. REFINED GRAPH ACCENTS (Dark-Mode Harmony)
    %% =========================================================
    classDef default fill:#1a1d24,stroke:#4a5568,stroke-width:1px,color:#ffffff;
    
    style FastAPI fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#ffffff
    style LangChain fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#ffffff
    
    style LLM fill:#062040,stroke:#3b82f6,stroke-width:2px,color:#ffffff
    style Context fill:#062f21,stroke:#10b981,stroke-width:2px,color:#ffffff
    
    style Tool_Direct fill:#272510,stroke:#eab308,stroke-width:2px,color:#ffffff
    style Tool_DDG fill:#272510,stroke:#eab308,stroke-width:2px,color:#ffffff
    style Tool_Wiki fill:#272510,stroke:#eab308,stroke-width:2px,color:#ffffff
```

---

### Key Technical Indicators & Engineering Implementations

* **Prompt-Driven Domain Filtering & Alignment:** To prevent model manipulation and hallucination, domain filtering is handled natively through an extensive system prompt hierarchy via LangChain. The model evaluates the query's relevance against the Facilities Services matrix. If an out-of-domain query is processed (e.g., *"what is the capital of Austria?"*), the prompt enforces an immediate, structured Pydantic refusal response, short-circuiting the agent graph to save compute tokens.
* **Autonomous Tool Selection & Execution:** Implements multi-tool routing via an asynchronous `AgentExecutor` framework. The engine dynamically decides whether to query DuckDuckGo for real-time B2B trending metrics, pull core definitions via Wikipedia (capped strictly at a single page of 221 characters to prevent context length bloat), or answer using its native weights.
* **Pydantic Structural Enforcement Array:** Employs a strict `PydanticOutputParser` subclassing pattern. Every agent output is run through strict JSON schema constraints to guarantee uniform payload arrays (`Title`, `Response`, `sources`, `tools_used`). If the model fails schema validation, the executor triggers internal fallback parsing flags to re-try up to 3 times before graceful exception return.
* **Dynamic Markdown-to-HTML UI Rendering:** The backend microservices utilize the `markdown` library to programmatically parse generated copy outputs into clean, responsive HTML blocks at runtime before streaming them over the full-duplex socket channel.

---

### 📂 Repository File System Directory Layout

```text
├── .env.template          # Global API key configuration blueprint
├── requirements.txt       # Version-locked environment dependencies
├── main.py                # Primary FastAPI gateway execution entrypoint (Websocket Server)
└── app/
    ├── frontend/          # Frontend Web Layer (HTML5 User Interface, CSS, jQuery)
    │   └── index.html     # WebSocket Client Dashboard Terminal
    └── api/
        ├── central/
        │   ├── initializer.py # Base Model instantiation configurations
        │   └── prompt.py      # 📝 System templates & JSON Scenario models
        ├── models/
        │   └── output.py      # Pydantic schema layout definitions
        └── services/
            ├── llm_service.py # Core tool-calling agent graph executor loop
            └── tools.py       # LangChain custom DuckDuckGo and Wikipedia lookups
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
*Open the `.env` file and populate your secure LLM infrastructure provider tokens.*

#### 3. Start the Application Gateway
```bash
python main.py
```
