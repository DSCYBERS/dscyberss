#!/usr/bin/env python3
"""
DSCYBERS v1.2 - Standalone Script
Multi-Tool Web Vulnerability Scanner

This is a standalone version that can be run without installation.
For full features, use the package version.
"""

import argparse
import subprocess
import sys
import time
from datetime import datetime

def print_banner():
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                    DSCYBERS v1.2                             ║
║            Multi-Tool Web Vulnerability Scanner              ║
║                 Advanced Security Assessment                 ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def run_basic_scan(target, tools):
    """Basic scanning functionality for standalone script"""
    print(f"🎯 Target: {target}")
    print(f"🔧 Tools: {', '.join(tools)}")
    print("\n" + "="*60)
    print("STARTING BASIC SECURITY SCAN")
    print("="*60)
    
    results = {}
    
    for tool in tools:
        try:
            print(f"\n[*] Running {tool}...")
            start_time = time.time()
            
            if tool == 'nmap':
                cmd = ['nmap', '-sV', '-sC', '--script=vuln', '-T4', target]
            elif tool == 'nikto':
                cmd = ['nikto', '-h', target]
            elif tool == 'sslyze':
                cmd = ['sslyze', '--regular', target]
            elif tool == 'wafw00f':
                cmd = ['wafw00f', target]
            else:
                cmd = [tool, target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                print(f"[+] {tool} completed in {execution_time:.2f}s")
                results[tool] = result.stdout
            else:
                print(f"[!] {tool} failed or returned warnings")
                results[tool] = f"Error: {result.stderr}"
                
        except subprocess.TimeoutExpired:
            print(f"[!] {tool} timed out")
        except FileNotFoundError:
            print(f"[!] {tool} not found - please install it")
        except Exception as e:
            print(f"[!] Error running {tool}: {e}")
    
    # Basic result summary
    print(f"\n{'='*60}")
    print("SCAN SUMMARY")
    print(f"{'='*60}")
    
    for tool, output in results.items():
        if output and not output.startswith("Error:"):
            print(f"\n--- {tool.upper()} RESULTS ---")
            # Show first 500 characters of output
            print(output[:500] + "..." if len(output) > 500 else output)
        else:
            print(f"\n--- {tool.upper()} ---")
            print("No results or error occurred")

def main():
    parser = argparse.ArgumentParser(
        description='DSCYBERS v1.2 — Multi-Tool Web Vulnerability Scanner (Standalone)',
        epilog='Note: This is a basic standalone version. Install the full package for advanced features.'
    )
    
    parser.add_argument('target', help='Target domain or IP address')
    parser.add_argument('--tools', nargs='+', 
                       choices=['nmap', 'nikto', 'sslyze', 'wafw00f'],
                       default=['nmap', 'nikto'],
                       help='Tools to run (default: nmap, nikto)')
    
    args = parser.parse_args()
    
    print_banner()
    print("Standalone Mode - For full features, install the package:")
    print("pip install dscybers")
    print()
    
    run_basic_scan(args.target, args.tools)

if __name__ == '__main__':
    main()
