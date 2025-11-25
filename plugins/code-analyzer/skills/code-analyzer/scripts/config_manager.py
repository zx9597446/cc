#!/usr/bin/env python3
"""
Configuration manager for code analyzer

Handles tool selection through command-based configuration.
"""

import os
import json
from pathlib import Path

class ConfigManager:
    """
    Manages configuration for code analysis tools.
    """

    def __init__(self):
        self.config_file = Path.home() / ".claude" / "code_analyzer_config.json"
        self.default_tool = "qwen"  # Default to Qwen

    def get_preferred_tool(self):
        """
        Get the preferred analysis tool from configuration.

        Returns:
            str: Tool name (gemini, qwen)
        """
        # Check config file
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    if "preferred_tool" in config and config["preferred_tool"] in ["gemini", "qwen"]:
                        return config["preferred_tool"]
            except (json.JSONDecodeError, KeyError, IOError) as e:
                print(f"Warning: Failed to read configuration file: {e}")

        # Return default
        return self.default_tool

    def set_preferred_tool(self, tool):
        """
        Set the preferred analysis tool.

        Args:
            tool: Tool name (gemini, qwen)
        """
        if tool not in ["gemini", "qwen"]:
            raise ValueError("Tool must be 'gemini' or 'qwen'")

        # Ensure config directory exists
        self.config_file.parent.mkdir(parents=True, exist_ok=True)

        # Load existing config or create new
        config = {}
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to read existing configuration: {e}")

        # Update config
        config["preferred_tool"] = tool

        # Save config
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save configuration: {e}")

    def detect_available_tools(self):
        """
        Detect which analysis tools are available in the system.

        Returns:
            dict: Available tools and their status
        """
        import shutil

        available_tools = {}

        # Check for Gemini CLI
        gemini_available = shutil.which("gemini") is not None or shutil.which("geminicli") is not None
        available_tools["gemini"] = {
            "available": gemini_available,
            "command": shutil.which("geminicli") or shutil.which("gemini") or "Not found"
        }

        # Check for Qwen CLI
        qwen_command = shutil.which("qwen")
        available_tools["qwen"] = {
            "available": qwen_command is not None,
            "command": qwen_command or "Not found"
        }

        return available_tools

    def get_status(self):
        """
        Get current configuration status.

        Returns:
            dict: Status information
        """
        preferred = self.get_preferred_tool()
        available = self.detect_available_tools()

        # Check if preferred tool is available
        effective_tool = preferred if available.get(preferred, {}).get("available", False) else None

        return {
            "preferred_tool": preferred,
            "available_tools": available,
            "effective_tool": effective_tool
        }

def get_configuration_help():
    """
    Get help text for configuring the code analyzer.

    Returns:
        str: Configuration help text
    """
    return """
Code Analyzer Configuration
===========================

Use the /code-analyzer command to configure which CLI tool to use:

Commands:
  /code-analyzer:tool gemini    # Use Gemini CLI
  /code-analyzer:tool qwen      # Use Qwen CLI (default)
  /code-analyzer:status         # Check current configuration
  /code-analyzer:help           # Show this help

Default: Qwen CLI

Available Tools:
  - gemini: Google Gemini CLI
  - qwen: Alibaba Qwen Code CLI

Note: The configured tool must be installed and available in your PATH.
"""

if __name__ == "__main__":
    import sys

    config = ConfigManager()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--check-availability":
            available = config.detect_available_tools()
            print("Available tools:")
            for tool, is_available in available.items():
                status = "✓ Available" if is_available else "✗ Not available"
                print(f"  {tool}: {status}")

        elif sys.argv[1] == "--set-tool" and len(sys.argv) > 2:
            try:
                config.set_preferred_tool(sys.argv[2])
                print(f"✓ Set preferred tool to: {sys.argv[2]}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif sys.argv[1] == "--get-tool":
            preferred = config.get_preferred_tool()
            print(f"Preferred tool: {preferred}")

        elif sys.argv[1] == "--status":
            status = config.get_status()
            print(f"Preferred tool: {status['preferred_tool']}")
            print("Available tools:")
            for tool, info in status['available_tools'].items():
                status_icon = "✓" if info['available'] else "✗"
                print(f"  {tool}: {status_icon} Available - Command: {info['command']}")
            print(f"Effective tool: {status['effective_tool']}")

        elif sys.argv[1] == "--help":
            print(get_configuration_help())

    else:
        # Show current configuration
        status = config.get_status()
        print("Current Configuration:")
        print(f"  Preferred tool: {status['preferred_tool']}")
        print("  Available tools:")
        for tool, info in status['available_tools'].items():
            status_icon = "✓" if info['available'] else "✗"
            print(f"    {tool}: {status_icon} Available - Command: {info['command']}")
        print(f"  Effective tool: {status['effective_tool']}")