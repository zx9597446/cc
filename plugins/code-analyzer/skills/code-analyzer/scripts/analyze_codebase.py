#!/usr/bin/env python3
"""
Advanced code analysis script

This script provides template commands for using various code analysis tools.
Supports Gemini CLI, Qwen Code, and other analysis tools.

Can be used as:
1. Command generator: Returns CLI command strings
2. CLI wrapper: Actually executes analysis commands
"""

import sys
import os
import subprocess
import argparse

# Add config manager to path
sys.path.append(os.path.dirname(__file__))
from config_manager import ConfigManager

# Shared analysis prompts dictionary
ANALYSIS_PROMPTS = {
    "patterns": {
        "authentication": "Analyze this codebase and identify all authentication and authorization patterns. Focus on login flows, session management, token handling, access control mechanisms, and security policies.",
        "data-flow": "Analyze data flow and state management patterns throughout the codebase. Identify how data is stored, updated, shared, and propagated across components or modules.",
        "api-usage": "Catalog all API usage patterns in this application. Include API design, integration patterns, error handling, and how different parts of the system communicate.",
        "component-structure": "Examine component and module organization patterns. Identify component hierarchies, module boundaries, reusable patterns, and code organization strategies."
    },
    "architecture": {
        "overview": "Analyze the overall system architecture. Identify the main components, data flow, service boundaries, integration patterns, and key architectural decisions.",
        "data-architecture": "Examine the data architecture including data models, data access patterns, database schemas, and data transformation processes.",
        "integration": "Analyze integration patterns with external services, message systems, and communication protocols used throughout the application."
    },
    "quality": {
        "performance": "Analyze this codebase for potential performance issues. Look for bottlenecks, optimization opportunities, resource usage patterns, and scalability considerations.",
        "security": "Scan this codebase for potential security vulnerabilities. Look for authentication issues, input validation problems, data protection gaps, and security best practices violations.",
        "maintainability": "Assess code maintainability by examining code complexity, coupling, cohesion, readability, and adherence to coding standards."
    },
    "review": {
        "systematic": "Perform a systematic code review. Identify code smells, anti-patterns, technical debt, improvement areas, and adherence to best practices.",
        "security": "Conduct a security-focused code review. Look for potential security vulnerabilities, data handling issues, and access control weaknesses.",
        "performance": "Perform a performance-focused code review. Identify performance bottlenecks, optimization opportunities, and resource usage patterns.",
        "architecture": "Conduct an architecture review. Evaluate architectural decisions, design patterns, service boundaries, and technology choices."
    },
    "audit": {
        "dependencies": "Analyze all third-party dependencies and libraries. Assess usage patterns, security vulnerabilities, version management, and maintenance considerations.",
        "testing": "Examine the testing strategy and test coverage. Identify testing patterns, quality gates, and areas that might need more comprehensive testing.",
        "migration": "Assess migration readiness by evaluating the current technology stack, dependency compatibility, and code health for potential upgrades."
    },
    "features": {
        "trace": "Trace the implementation of a specific feature throughout the codebase. Show all files involved, data flow, API endpoints, UI components, and how the feature integrates with the rest of the system.",
        "api-endpoints": "Catalog all API endpoints in this application. Include REST routes, GraphQL resolvers, tRPC procedures, their request/response patterns, authentication requirements, and how they're consumed by the frontend.",
        "react-hooks": "Analyze this codebase and identify all React hooks usage patterns. Show how useState, useEffect, useContext, and custom hooks are being used. Include examples of best practices and potential issues.",
        "database-queries": "Find all database query patterns in this codebase. Include SQL queries, ORM usage, connection handling, and any database-related utilities. Show the different approaches used."
    },
    "documentation": {
        "onboarding": "Analyze this codebase to help create onboarding documentation. Identify key concepts developers need to understand, important files and directories, setup requirements, and the most critical patterns to learn first.",
        "architecture": "Generate comprehensive architecture documentation. Identify the main components, data flow, service boundaries, key design decisions, and how different parts of the system interact.",
        "api-reference": "Generate API reference documentation. Document all endpoints, their parameters, responses, authentication requirements, and usage examples."
    }
}

def get_analysis_command(analysis_scenario, target=None, context=None):
    """
    Generate code analysis commands for different analysis scenarios.
    Uses configured tool selection.

    Args:
        analysis_scenario: Analysis scenario (patterns, architecture, quality, review, audit)
        target: Specific target for analysis (optional)
        context: Additional context for the analysis (optional)

    Returns:
        Analysis command string
    """

    # Get the analysis prompt
    if analysis_scenario in ANALYSIS_PROMPTS:
        if target and target in ANALYSIS_PROMPTS[analysis_scenario]:
            prompt = ANALYSIS_PROMPTS[analysis_scenario][target]
        else:
            prompt = f"Perform {analysis_scenario} analysis on this codebase. Provide comprehensive insights and identify key patterns."
    else:
        prompt = f"Analyze this codebase focusing on {analysis_scenario}. Provide comprehensive insights and identify key patterns."

    # Add context if provided
    if context:
        prompt = f"{prompt} Context: {context}"

    # Get configured tool
    config = ConfigManager()
    preferred_tool = config.get_preferred_tool()

    # Tool-specific command construction
    if preferred_tool == "gemini":
        return f"geminicli --all-files --yolo -p \"{prompt}\""
    else:  # qwen (default)
        return f"qwen --all-files --yolo -p \"{prompt}\""

def get_tool_specific_commands(analysis_scenario, target=None):
    """
    Get analysis commands for all supported tools.
    """
    # Force specific tools for comparison
    return {
        "gemini": _get_analysis_command_for_tool(analysis_scenario, target, "gemini"),
        "qwen": _get_analysis_command_for_tool(analysis_scenario, target, "qwen"),
        "configured": get_analysis_command(analysis_scenario, target)
    }

def _get_analysis_command_for_tool(analysis_scenario, target=None, tool="auto"):
    """
    Generate command for specific tool (for comparison purposes).
    """
    # Get the analysis prompt using shared dictionary
    if analysis_scenario in ANALYSIS_PROMPTS:
        if target and target in ANALYSIS_PROMPTS[analysis_scenario]:
            prompt = ANALYSIS_PROMPTS[analysis_scenario][target]
        else:
            prompt = f"Perform {analysis_scenario} analysis on this codebase. Provide comprehensive insights and identify key patterns."
    else:
        prompt = f"Analyze this codebase focusing on {analysis_scenario}. Provide comprehensive insights and identify key patterns."

    # Tool-specific command construction
    if tool == "gemini":
        return f"geminicli --all-files --yolo -p \"{prompt}\""
    elif tool == "qwen":
        return f"qwen --all-files --yolo -p \"{prompt}\""
    else:
        return f"code-analyzer --all-files --comprehensive -p \"{prompt}\""

def execute_analysis(analysis_scenario, target=None, context=None, timeout=300):
    """
    Execute code analysis using configured CLI tool.

    Args:
        analysis_scenario: Analysis scenario (patterns, architecture, quality, review, audit)
        target: Specific target for analysis (optional)
        context: Additional context for the analysis (optional)
        timeout: Command timeout in seconds (default: 300)

    Returns:
        dict: Execution result with stdout, stderr, and returncode
    """
    try:
        # Get the analysis command
        command = get_analysis_command(analysis_scenario, target, context)

        print(f"Executing analysis command: {command}")
        print("This may take several minutes...")

        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "command": command
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": f"Command timed out after {timeout} seconds",
            "command": command
        }
    except Exception as e:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": f"Execution failed: {str(e)}",
            "command": command
        }

def execute_analysis_optimized(analysis_scenario, target=None, context=None, timeout=300):
    """
    Optimized execution that returns summary + file path instead of full output.

    Args:
        analysis_scenario: Analysis scenario (patterns, architecture, quality, review, audit)
        target: Specific target for analysis (optional)
        context: Additional context for the analysis (optional)
        timeout: Command timeout in seconds (default: 300)

    Returns:
        dict: Optimized execution result with summary, file path, and metadata
    """
    import time

    # Execute the analysis
    result = execute_analysis(analysis_scenario, target, context, timeout)

    if not result["success"]:
        return result

    # Save full output to temporary file
    timestamp = int(time.time())
    output_file = f"/tmp/code-analysis-{timestamp}.txt"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Command: {result['command']}\n")
            f.write(f"Timestamp: {time.ctime()}\n")
            f.write("=" * 80 + "\n\n")
            f.write(result["stdout"])
            if result["stderr"]:
                f.write("\n\n" + "=" * 80 + "\n")
                f.write("STDERR:\n")
                f.write(result["stderr"])
    except Exception as e:
        return {
            "success": False,
            "returncode": -1,
            "stdout": "",
            "stderr": f"Failed to save output file: {str(e)}",
            "command": result["command"]
        }

    # Extract summary (first 30 lines or ~500 tokens)
    lines = result["stdout"].split('\n')
    summary_lines = []

    # Smart extraction of key content
    for i, line in enumerate(lines[:50]):  # Look at first 50 lines
        # Keep headers, summaries, and important markers
        if (line.startswith('#') or
            'Summary' in line or
            'Key' in line or
            'Important' in line or
            '##' in line or
            i < 5):  # Always keep first 5 lines
            summary_lines.append(line)
            if len(summary_lines) >= 30:
                break

    summary = '\n'.join(summary_lines)

    # If summary is too short, add more context
    if len(summary_lines) < 10:
        summary_lines.extend(lines[:20])
        summary = '\n'.join(summary_lines[:30])

    return {
        "success": True,
        "summary": summary,  # Only return summary
        "full_output_path": output_file,  # Full output file path
        "total_lines": len(lines),
        "command": result["command"],
        "returncode": result["returncode"]
    }

def execute_analysis_with_retry(analysis_scenario, target=None, context=None, timeout=300, max_retries=2):
    """
    Execute analysis with automatic retry mechanism.

    Args:
        analysis_scenario: Analysis scenario
        target: Specific target for analysis (optional)
        context: Additional context for the analysis (optional)
        timeout: Command timeout in seconds (default: 300)
        max_retries: Maximum number of retry attempts (default: 2)

    Returns:
        dict: Execution result with retry information
    """
    import time

    for attempt in range(max_retries + 1):
        try:
            result = execute_analysis_optimized(analysis_scenario, target, context, timeout)

            if result["success"]:
                if attempt > 0:
                    result["retry_info"] = f"Succeeded after {attempt} retry{'s' if attempt > 1 else ''}"
                return result
            elif attempt < max_retries:
                print(f"Analysis failed, retrying... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(2)  # Wait 2 seconds before retry
        except Exception as e:
            if attempt < max_retries:
                print(f"Analysis error, retrying... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(2)
            else:
                # Final attempt failed
                return {
                    "success": False,
                    "returncode": -1,
                    "stdout": "",
                    "stderr": f"Analysis failed after {max_retries} retries: {str(e)}",
                    "command": "unknown"
                }

    # If we get here, all retries failed
    return {
        "success": False,
        "returncode": -1,
        "stdout": "",
        "stderr": f"Analysis failed after {max_retries} retries",
        "command": "unknown"
    }

def main():
    """Main function for CLI execution"""
    parser = argparse.ArgumentParser(description="Code Analysis CLI Wrapper")
    parser.add_argument(
        "action",
        choices=["generate", "execute", "execute-optimized", "execute-retry"],
        help="Action to perform: generate command, execute analysis, execute with optimization, or execute with retry"
    )
    parser.add_argument(
        "--scenario",
        required=True,
        help="Analysis scenario (patterns, architecture, quality, review, audit, features, documentation)"
    )
    parser.add_argument(
        "--target",
        help="Specific target for analysis"
    )
    parser.add_argument(
        "--context",
        help="Additional context for the analysis"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Command timeout in seconds (default: 300)"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=2,
        help="Maximum retry attempts for execute-retry action (default: 2)"
    )

    args = parser.parse_args()

    if args.action == "generate":
        # Generate and print command
        command = get_analysis_command(args.scenario, args.target, args.context)
        print(f"Generated command: {command}")

    elif args.action == "execute":
        # Execute analysis (original behavior)
        result = execute_analysis(args.scenario, args.target, args.context, args.timeout)

        if result["success"]:
            print("✅ Analysis completed successfully!")
            print("\nAnalysis Results:")
            print("=" * 50)
            print(result["stdout"])
        else:
            print("❌ Analysis failed!")
            print(f"Error: {result['stderr']}")
            print(f"Command: {result['command']}")

    elif args.action == "execute-optimized":
        # Execute analysis with optimization
        result = execute_analysis_optimized(args.scenario, args.target, args.context, args.timeout)

        if result["success"]:
            print("✅ Analysis completed successfully!")
            print(f"\nSummary ({result['total_lines']} lines total):")
            print("=" * 50)
            print(result["summary"])
            print(f"\n📁 Full analysis saved to: {result['full_output_path']}")
            print("💡 Use 'Read' tool to access full analysis if needed")
        else:
            print("❌ Analysis failed!")
            print(f"Error: {result['stderr']}")
            print(f"Command: {result['command']}")

    elif args.action == "execute-retry":
        # Execute analysis with retry mechanism
        result = execute_analysis_with_retry(args.scenario, args.target, args.context, args.timeout, args.max_retries)

        if result["success"]:
            print("✅ Analysis completed successfully!")
            if "retry_info" in result:
                print(f"\n🔄 {result['retry_info']}")
            print(f"\nSummary ({result['total_lines']} lines total):")
            print("=" * 50)
            print(result["summary"])
            print(f"\n📁 Full analysis saved to: {result['full_output_path']}")
            print("💡 Use 'Read' tool to access full analysis if needed")
        else:
            print("❌ Analysis failed after retries!")
            print(f"Error: {result['stderr']}")
            print(f"Command: {result['command']}")

if __name__ == "__main__":
    main()