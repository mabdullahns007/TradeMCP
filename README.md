# 🚀 TradeMCP

**AI-powered Tradingview Analyst** — connect Claude Desktop to TradingView via MCP for chart insights and much more.



https://github.com/user-attachments/assets/c1946e3c-0534-4460-99b3-e62f0dbc24dc


---

## 🎯 What It Does

- **open_tv()** – Launches TradingView via `Ctrl+Alt+T`, waits briefly, then minimizes the window  
- **get_chart_image()** – Activates TradingView, takes a screenshot, minimizes the window, and returns the image to Claude

Ideal for developers and traders aiming for AI-driven chart workflows and automation.

---

## 🛠️ Getting Started

### Prerequisites
- **Python 3.8+**
- **Windows OS**
- **Tradingview Desktop Application**
- **Configure Shortcut Key (Ctrl + Alt + T) for Tradingview**
- <img width="358" height="507" alt="image" src="https://github.com/user-attachments/assets/d6061953-b726-4ad7-acf6-1a1b276d0259" />
- Install dependencies:
  ```bash
  pip install mcp[cli] fastmcp pyautogui pygetwindow pywin32

## 🛠 Setup & Installation
- **Clone the Repo**
  ```
  git clone https://github.com/mabdullahns007/TradeMCP.git
  cd TradeMCP
- **Run the server.py and make sure the dependencies are installed correctly**
  ```
  python server.py
- **Edit claude_desktop_config.json file**
  ```
  {
    "mcpServers": {
      "tradingview": {
        "command": "python",
        "args": ["C:\\PATH\\TO\\FILE\\server.py"]
      }
    }
  }
- **Quit and Restart Claude Desktop**
- **Give the following prompts to test the MCP Server**
  ```
  1. Open Tradingview
  2. Get chart image
