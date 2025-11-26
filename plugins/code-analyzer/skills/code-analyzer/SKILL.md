---
name: code-analyzer
description: AI-powered code analysis with Qwen/Gemini CLI tools. Pattern detection, architecture review, quality assessment, code reviews. Configure with /code-analyzer:tool
allowed-tools:
  - Bash
---

# Code Analyzer

Advanced AI-powered code analysis for comprehensive codebase understanding, pattern detection, and quality assessment.

## 🚀 Quick Start

Simply express your analysis needs:

```
Analyze authentication patterns in this codebase
Provide architectural overview of the application
Review code quality and identify technical debt
Scan for security vulnerabilities
Find React hooks usage patterns
```

## ⚡ Key Features

- **Smart Pattern Detection**: Authentication, API usage, data flow, component structures
- **Architecture Insights**: System overview, data architecture, integration patterns
- **Quality Assessment**: Performance, security, maintainability analysis
- **Code Review**: Systematic reviews, technical debt identification
- **Tool Flexibility**: Switch between Qwen CLI (default) and Gemini CLI
- **Optimized Output**: Returns concise summaries + full report paths
- **Auto-Retry**: Built-in retry mechanism for reliability

## ⚠️ IMPORTANT: Wait for Completion

Analysis takes 2-5 minutes. You MUST:
1. Execute command
2. **WAIT for full completion** (do NOT timeout)
3. Process results only after completion

## 🔧 Configuration

```bash
/code-analyzer:tool qwen      # Use Qwen CLI (default)
/code-analyzer:tool gemini    # Use Gemini CLI
/code-analyzer:status         # Check current configuration
```

## 🎯 Execution

```bash
python scripts/analyze_codebase.py execute-optimized \
  --scenario <patterns|architecture|quality|review|audit|features|documentation> \
  --target <specific-target>
```

**Returns:**
- ✅ **Summary**: ~500 tokens of key findings (saves 90% tokens!)
- 📁 **Full Report**: File path for complete analysis
- 🔍 **Use Read tool** to access full report if user needs details

## 📊 Analysis Scenarios

### 🔍 Pattern Detection
- **authentication**: Login flows, session management, access control
- **data-flow**: State management, data propagation patterns
- **api-usage**: API design, integration patterns, error handling
- **component-structure**: Component hierarchies, module organization

### 🏗️ Architecture Analysis
- **overview**: System architecture, component relationships
- **data-architecture**: Data models, database schemas, access patterns
- **integration**: External services, message systems, protocols

### 🔎 Quality Assessment
- **performance**: Bottlenecks, optimization opportunities
- **security**: Vulnerabilities, data protection, access control
- **maintainability**: Code complexity, coupling, readability

### 📝 Code Review
- **systematic**: Code smells, anti-patterns, technical debt
- **security**: Security vulnerabilities, data handling issues
- **performance**: Performance bottlenecks, optimization areas
- **architecture**: Design decisions, technology choices

### 🔧 Technology Audit
- **dependencies**: Third-party libraries, security vulnerabilities
- **testing**: Test coverage, testing patterns, quality gates
- **migration**: Technology stack assessment, upgrade readiness

### 🚀 Feature Analysis
- **trace**: Feature implementation tracking across files
- **api-endpoints**: REST routes, GraphQL resolvers, authentication
- **react-hooks**: useState, useEffect, useContext patterns
- **database-queries**: SQL queries, ORM usage, connection handling

### 📚 Documentation
- **onboarding**: Key concepts, setup requirements, learning paths
- **architecture**: System components, data flow, design decisions
- **api-reference**: Endpoints, parameters, responses, examples

## 📖 Resources

Detailed analysis patterns: `references/analysis_patterns.md` (loaded on demand)