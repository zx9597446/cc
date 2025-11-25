# /code-analyzer

Configure and manage code analyzer settings.

## Usage

```
/code-analyzer:tool <tool-name>
/code-analyzer:status
/code-analyzer:help
```

## Commands

### Set Analysis Tool
```
/code-analyzer:tool gemini
/code-analyzer:tool qwen
```

**Parameters:**
- `gemini`: Use Google Gemini CLI for code analysis
- `qwen`: Use Alibaba Qwen Code CLI for code analysis (default)

### Check Status
```
/code-analyzer:status
```

Shows current configuration and available tools.

### Get Help
```
/code-analyzer:help
```

Shows this help information.

## Examples

### Set Gemini as default tool
```
/code-analyzer:tool gemini
```

### Set Qwen as default tool
```
/code-analyzer:tool qwen
```

### Check current status
```
/code-analyzer:status
```

## Default Behavior

By default, the code analyzer uses **Qwen CLI** for analysis. Use the tool command to switch to Gemini if preferred.

## Analysis Usage

After configuration, use the code analyzer skill normally:

```
Analyze authentication patterns in this codebase
Provide architectural overview of the application
Find React hooks usage patterns
```

The skill will automatically use the configured tool for analysis.