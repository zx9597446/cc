# zx9597446's Claude Code Marketplace

A personal collection of Claude Code plugins and skills for development workflows.

## 🚀 Quick Start

### From GitHub (Recommended)

Add this marketplace to Claude Code:

```bash
claude plugin marketplace add zx9597446/cc
```

Then install individual plugins:

```bash

# Install code-analyzer plugin
claude plugin install code-analyzer@zx9597446/cc
```

## 📦 Available Plugins

### 🔧 Development Tools


- **code-analyzer** - Advanced code analysis tools
  - Comprehensive codebase analysis and pattern detection
  - Automatic architectural understanding and system overviews
  - Code quality assessment and security vulnerability scanning
  - Technology stack analysis and dependency mapping

## 🏗️ Plugin Structure

Each plugin in this marketplace follows the Claude Code best practices:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin configuration
├── skills/                  # Skills directory
│   └── skill-name/          # Individual skill
│       ├── SKILL.md         # Skill documentation
│       ├── references/      # Reference materials
│       └── scripts/         # Helper scripts
├── commands/                # Custom slash commands (optional)
└── agents/                  # Sub-agents (optional)
```

## 📄 License

Individual plugins may have their own licenses. See each plugin directory for details.

## 🤝 Contributing

This is a personal marketplace. For community contributions, please check the official [Claude Code Commands Directory](https://claudecodecommands.directory/).

---

Built with ❤️ by [zx9597446](https://github.com/zx9597446)
