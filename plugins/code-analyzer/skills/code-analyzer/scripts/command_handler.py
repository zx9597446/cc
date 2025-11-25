#!/usr/bin/env python3
"""
Command handler for code-analyzer slash commands
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from config_manager import ConfigManager

def handle_command(args):
    """
    Handle code-analyzer commands

    Args:
        args: Command arguments
    """
    config = ConfigManager()

    if not args:
        print("Usage: /code-analyzer:tool <gemini|qwen> | /code-analyzer:status | /code-analyzer:help")
        return

    command = args[0]

    if command == "tool" and len(args) > 1:
        tool = args[1]
        try:
            config.set_preferred_tool(tool)
            print(f"✓ Successfully set preferred tool to: {tool}")

            # Show updated status
            status = config.get_status()
            print(f"\nCurrent configuration:")
            print(f"  Preferred tool: {status['preferred_tool']}")
            print(f"  Effective tool: {status['effective_tool']}")

        except ValueError as e:
            print(f"✗ Error: {e}")
        except Exception as e:
            print(f"✗ Failed to set tool: {e}")

    elif command == "status":
        status = config.get_status()
        print("Current Configuration:")
        print(f"  Preferred tool: {status['preferred_tool']}")
        print("  Available tools:")
        for tool, info in status['available_tools'].items():
            status_icon = "✓" if info['available'] else "✗"
            print(f"    {tool}: {status_icon} Available - Command: {info['command']}")
        print(f"  Effective tool: {status['effective_tool']}")

    elif command == "help":
        print("""
Code Analyzer Configuration Help
================================

Commands:
  /code-analyzer:tool gemini    - Use Gemini CLI for analysis
  /code-analyzer:tool qwen      - Use Qwen CLI for analysis (default)
  /code-analyzer:status         - Show current configuration
  /code-analyzer:help           - Show this help

Default: Qwen CLI

After configuration, use the code analyzer skill normally:
  "Analyze authentication patterns in this codebase"
  "Provide architectural overview of the application"
  "Perform systematic code review"
""")
    else:
        print(f"Unknown command: {command}")
        print("Use /code-analyzer:help for available commands")

if __name__ == "__main__":
    # Get command line arguments (skip script name)
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    handle_command(args)