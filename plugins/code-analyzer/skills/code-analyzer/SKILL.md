---
name: code-analyzer
description: Comprehensive code analysis using CLI tools for pattern detection, architecture review, code quality assessment, and systematic code reviews. Use when: (1) Analyzing codebases for patterns and architecture, (2) Performing code reviews and quality assessments, (3) Identifying technical debt and improvement opportunities, (4) Understanding complex code structures, (5) Preparing for refactoring or migration. Configure with /code-analyzer:tool command.
allowed-tools:
  - Bash
---

# Code Analyzer

Use advanced CLI tools for comprehensive codebase analysis, pattern detection, and systematic code reviews.

## Quick Start

When you need code analysis, express your analysis needs:

```
Analyze authentication patterns in this codebase
Provide architectural overview of the application
Review code quality and identify technical debt
Scan for security vulnerabilities
Perform systematic code review
```

## Analysis Workflow

1. **Configure Tool**: Use `/code-analyzer:tool` to select analysis tool
2. **Define Scope**: Specify analysis type (patterns, architecture, quality, review)
3. **Execute Analysis**: Run analysis with configured tool
4. **Review Results**: Interpret patterns and provide recommendations

## Analysis Scenarios

### Pattern Detection
- Authentication patterns, API usage, data flow patterns
- State management, component relationships, architectural patterns

### Architecture Analysis
- System architecture, component hierarchy, data flow
- Integration patterns, service boundaries, design decisions

### Quality Assessment
- Performance bottlenecks, security vulnerabilities, code consistency
- Best practices adherence, maintainability issues

### Code Review
- Systematic code review, technical debt identification
- Refactoring opportunities, improvement suggestions

### Technology Audit
- Dependencies, testing strategy, migration readiness
- Technology stack analysis, integration patterns

## Resources

- **Scripts**: See `scripts/analyze_codebase.py` for analysis command templates
- **References**: See `references/analysis_patterns.md` for detailed analysis patterns

## Configuration

Use the `/code-analyzer` command to configure which CLI tool to use:

### Set Analysis Tool
```
/code-analyzer:tool gemini    # Use Gemini CLI
/code-analyzer:tool qwen      # Use Qwen CLI (default)
```

### Check Status
```
/code-analyzer:status
```

### Get Help
```
/code-analyzer:help
```

## Implementation

### Execution Workflow

When performing code analysis:

1. **Determine Analysis Type**: Identify the analysis scenario and target based on user request
2. **Execute Analysis**: Run the CLI wrapper with appropriate parameters:
   ```bash
   python scripts/analyze_codebase.py execute --scenario <scenario> --target <target>
   ```
3. **Wait for Completion**: This command may take several minutes to complete. **Wait for the CLI command to fully execute** before proceeding.
4. **Analyze Results**: Review the output and provide insights based on the analysis results.

### Important Notes

- **Wait for Completion**: The CLI analysis may take 2-5 minutes. Ensure the command completes before continuing.
- **Error Handling**: If the analysis fails, check the error message and provide guidance.
- **Tool Configuration**: Use `/code-analyzer:tool` to configure preferred analysis tool (qwen or gemini).

### Example Execution

For authentication pattern analysis:
```bash
python scripts/analyze_codebase.py execute --scenario patterns --target authentication
```

**Wait for this command to complete** - it will provide comprehensive authentication pattern analysis.