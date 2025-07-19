# Contributing to TradeMCP

Welcome to TradeMCP - the world's first Claude-powered TradingView assistant! 🎉

We're excited to have you contribute to this open-source project that bridges AI and trading analysis through automated TradingView control.

## 🚀 About TradeMCP

TradeMCP uses MCP (Model Context Protocol) + FastMCP + pyautogui to enable Claude Desktop to control TradingView with simple prompts. Currently, it can:

- `open_tv()` — Launch TradingView
- `get_chart_image()` — Capture and return live chart screenshots

Our vision is to build the first fully AI-controlled Trading Analyst Agent with smart analysis, broker integration, and automated trade execution.

## 🎯 Priority Features We Need

We're looking for contributors to help implement these core TradingView automation features:

### 🔧 High Priority Tools

1. **Draw Trendline** - Enable drawing trendlines on charts
2. **Draw Fibonacci Retracement** - Add Fib retracement tools
3. **Draw Rectangle** - Implement rectangle drawing functionality
4. **Draw Horizontal Line** - Add horizontal line drawing
5. **Draw Vertical Line** - Add vertical line drawing
6. **Search Trading Pairs** - Enable searching for specific trading pairs
7. **Navigate Between Pairs** - Switch between different trading pairs

## 🛠️ Getting Started

### Prerequisites

- Python 3.7+
- Windows OS (required for pyautogui and win32 libraries)
- TradingView account
- Claude Desktop (for testing)

### Installation

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/TradeMCP.git
   cd TradeMCP
   ```

2. **Install dependencies**
   ```bash
    pip install mcp[cli] fastmcp pyautogui pygetwindow pywin32
   ```

3. **Set up TradingView hotkey**
   - Configure `Ctrl+Alt+T` to open/focus TradingView in your system

### Development Setup

1. **Test the existing functionality**
   ```bash
   python server.py
   ```

2. **Connect with Claude Desktop**
   - Add TradeMCP to your Claude Desktop MCP configuration
   - Test `open_tv()` and `get_chart_image()` functions

## 📋 How to Contribute

### 1. Choose a Feature

Pick one of the priority features from the list above. Comment on the corresponding issue or create a new one to let us know you're working on it.

### 2. Development Guidelines

#### Code Structure
- Follow the existing pattern in `server.py`
- Use descriptive function names (e.g., `draw_trendline()`, `search_pairs()`)
- Include proper error handling and logging

### 3. Testing

- Test your function individually
- Test integration with Claude Desktop
- Verify it works on different screen resolutions
- Test error handling scenarios

### 4. Documentation

- Add clear docstrings to your functions
- Update this CONTRIBUTING.md if you add new setup steps
- Comment complex automation sequences

## 🔄 Submission Process

### Pull Request Guidelines

1. **Create a feature branch**
   ```bash
   git checkout -b feature/draw-trendline
   ```

2. **Make your changes**
   - Implement the feature following our guidelines
   - Test thoroughly
   - Add appropriate logging

3. **Commit with clear messages**
   ```bash
   git commit -m "feat: add trendline drawing functionality"
   ```

4. **Push and create PR**
   ```bash
   git push origin feature/draw-trendline
   ```

5. **PR Description Template**
   ```markdown
   ## Feature: [Feature Name]
   
   ### What this PR does
   - Brief description of the implemented feature
   
   ### Testing
   - [ ] Function works independently
   - [ ] Integrates properly with Claude Desktop
   - [ ] Handles errors gracefully
   - [ ] Works on different screen sizes
   
   ### Screenshots/Demo
   (Optional: Add screenshots or GIFs of the feature working)
   ```

## 🐛 Bug Reports

Found a bug? Please create an issue with:

- **Description**: What happened vs. what you expected
- **Steps to reproduce**: Clear reproduction steps
- **Environment**: Python version, Windows version, TradingView setup
- **Screenshots**: If applicable
- **Logs**: Any error messages from the console

## 💡 Feature Requests

Have ideas beyond our priority list? We'd love to hear them!

Create an issue with the "enhancement" label and include:
- **Use case**: Why this feature would be valuable
- **Description**: How you envision it working
- **TradingView context**: How it relates to TradingView functionality

## 🤝 Code of Conduct

- Be respectful and inclusive
- Help newcomers get started
- Focus on constructive feedback
- Keep discussions relevant to the project

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and brainstorming
- **Tag @mabdullahns007**: For urgent matters or guidance

## 🏆 Recognition

Contributors will be:
- Added to our contributors list
- Mentioned in release notes
- Given early access to beta features
- Invited to shape the project roadmap

## 📊 Project Roadmap

**Phase 1** (Current): Core drawing, chart annotation and navigation tools
**Phase 2**: Advanced analysis features (indicators, alerts, trading concepts)
**Phase 3**: Broker integration and trade execution
**Phase 4**: Full AI trading agent capabilities

---


Let's build the future of AI-powered trading together! 🚀📈
