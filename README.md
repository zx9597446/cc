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
# Install skill-creator plugin
claude plugin install skill-creator@zx9597446/cc
```

### From Local Path

If you have cloned this repository locally:

```bash
# Add marketplace from local path
claude plugin marketplace add ./.claude-plugin/marketplace.json

# Install skill-creator plugin
claude plugin install skill-creator@zx9597446-cc-marketplace
```

## 📦 Available Plugins

### 🔧 Development Tools

- **skill-creator** - Tools and guidance for creating effective Claude skills
  - Skill creation templates and best practices
  - Scripts for initializing, validating, and packaging skills
  - Reference documentation for skill development

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

## 🛠️ Development

### Adding New Plugins

1. Create a new directory in `plugins/`
2. Add `.claude-plugin/plugin.json` with plugin metadata
3. Organize components (skills, commands, agents) in appropriate directories
4. Update `.claude-plugin/marketplace.json` to include the new plugin

### Local Testing

To test plugins locally before pushing to GitHub:

```bash
# Add marketplace from local path
claude plugin marketplace add ./.claude-plugin/marketplace.json

# Install and test your new plugin
claude plugin install your-new-plugin@zx9597446-cc-marketplace

# Update marketplace to get latest changes
claude plugin marketplace update zx9597446-cc-marketplace
```

### Plugin Configuration

Each plugin requires a `plugin.json` file:

```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/your-username"
  },
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/"
}
```

## 📄 License

Individual plugins may have their own licenses. See each plugin directory for details.

## 🔧 Troubleshooting

### Common Issues

**Marketplace not found:**
- Ensure you're using the correct path to `marketplace.json`
- Check that the marketplace name in `marketplace.json` uses kebab-case (no spaces)

**Plugin not found:**
- Verify the plugin name matches exactly in `marketplace.json`
- Check that the plugin has a valid `.claude-plugin/plugin.json` file

**Local installation issues:**
- Make sure the local path is accessible
- Restart Claude Code after installing plugins

## 🤝 Contributing

This is a personal marketplace. For community contributions, please check the official [Claude Code Commands Directory](https://claudecodecommands.directory/).

---

Built with ❤️ by [zx9597446](https://github.com/zx9597446)

