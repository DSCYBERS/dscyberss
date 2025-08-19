#!/usr/bin/env python3
"""
DSCYBERS Demo Script

This script demonstrates the enhanced DSCYBERS capabilities including:
- Interactive configuration
- Advanced vulnerability detection
- AI-powered payload generation
- Professional reporting

Usage:
    python demo_dscybers.py
"""

import asyncio
import sys
import os
from pathlib import Path

# Add the current directory to path for imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from dscybers.interactive_config import ScanConfiguration, get_scan_configuration
    from dscybers.vulnerability_detector import run_advanced_scan
    from dscybers.reporting import generate_comprehensive_report
except ImportError:
    print("❌ Error: DSCYBERS modules not found. Please install the package or run from the correct directory.")
    sys.exit(1)

def print_demo_banner():
    """Print demo banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                   DSCYBERS v2.0 DEMO                        ║
║               Next-Gen Vulnerability Scanner                 ║
║                                                              ║
║  This demo shows the enhanced capabilities of DSCYBERS      ║
║  including interactive configuration and AI-powered         ║
║  vulnerability detection.                                    ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def create_demo_configuration():
    """Create a demo configuration for testing"""
    config = ScanConfiguration(
        target_url="https://httpbin.org",
        target_type="web",
        auth_type="none",
        scan_intensity="light",
        max_threads=5,
        request_timeout=15,
        rate_limit_delay=0.2,
        enable_ai_payloads=True,
        enable_exploit_chaining=False,
        enable_zero_day_simulation=False,
        compliance_frameworks=["owasp"]
    )
    return config

async def run_demo_scan():
    """Run a demonstration scan"""
    print("🚀 Running demonstration scan...")
    print("Target: https://httpbin.org (safe test target)")
    
    # Create demo configuration
    config = create_demo_configuration()
    
    print(f"Configuration:")
    print(f"  • Target: {config.target_url}")
    print(f"  • Type: {config.target_type}")
    print(f"  • Intensity: {config.scan_intensity}")
    print(f"  • AI Payloads: {'Enabled' if config.enable_ai_payloads else 'Disabled'}")
    print(f"  • Max Threads: {config.max_threads}")
    
    print("\n🔍 Starting vulnerability scan...")
    
    try:
        # Run the advanced scan
        findings = await run_advanced_scan(config)
        
        print(f"\n✅ Scan completed!")
        print(f"📊 Results: {len(findings)} vulnerabilities found")
        
        # Display summary
        if findings:
            severity_counts = {}
            for finding in findings:
                severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1
            
            print("\n📋 Vulnerability Summary:")
            severity_emojis = {
                "Critical": "🔴", "High": "🟠", "Medium": "🟡", 
                "Low": "🔵", "Info": "⚪"
            }
            
            for severity in ["Critical", "High", "Medium", "Low", "Info"]:
                count = severity_counts.get(severity, 0)
                if count > 0:
                    emoji = severity_emojis.get(severity, "🔍")
                    print(f"  {emoji} {severity}: {count}")
            
            print("\n🔍 Sample Findings:")
            for i, finding in enumerate(findings[:3], 1):  # Show first 3 findings
                print(f"  {i}. {finding.title} ({finding.severity})")
                print(f"     {finding.description}")
        else:
            print("🎉 No vulnerabilities detected in this demo scan!")
        
        # Generate reports
        print("\n📄 Generating reports...")
        
        # HTML Report
        html_file = "dscybers_demo_report.html"
        generate_comprehensive_report(findings, config.target_url, html_file, "html")
        
        # JSON Report
        json_file = "dscybers_demo_report.json"
        generate_comprehensive_report(findings, config.target_url, json_file, "json")
        
        print(f"✅ Reports generated:")
        print(f"  📊 HTML: {html_file}")
        print(f"  📋 JSON: {json_file}")
        
        return findings
        
    except Exception as e:
        print(f"❌ Error during scan: {e}")
        return []

def show_demo_menu():
    """Show demo menu options"""
    print("\n" + "="*60)
    print("DSCYBERS DEMO OPTIONS")
    print("="*60)
    print("1. Run Quick Demo Scan (recommended)")
    print("2. Interactive Configuration Setup")
    print("3. Show Vulnerability Types Detected")
    print("4. Show Reporting Capabilities")
    print("5. Exit Demo")
    print()

def show_vulnerability_types():
    """Show the types of vulnerabilities DSCYBERS can detect"""
    print("\n🔍 VULNERABILITIES DETECTED BY DSCYBERS:")
    print("="*60)
    
    vuln_categories = {
        "🔥 OWASP Top 10 (2021 & 2024)": [
            "• Injection (SQL, NoSQL, Command, LDAP)",
            "• Broken Authentication & Session Management",
            "• Sensitive Data Exposure",
            "• XML External Entities (XXE)",
            "• Broken Access Control",
            "• Security Misconfigurations",
            "• Cross-Site Scripting (XSS)",
            "• Insecure Deserialization",
            "• Using Components with Known Vulnerabilities",
            "• Insufficient Logging & Monitoring"
        ],
        "🚀 Advanced Vulnerabilities": [
            "• Server-Side Request Forgery (SSRF)",
            "• GraphQL Injection & Introspection",
            "• JWT Attacks (None algorithm, weak secrets)",
            "• Business Logic Flaws",
            "• API Security Issues",
            "• HTTP/2 & HTTP/3 Vulnerabilities",
            "• Template Injection (SSTI)",
            "• Web Cache Poisoning",
            "• CORS Misconfigurations",
            "• Directory Traversal & Path Manipulation"
        ],
        "🤖 AI-Powered Features": [
            "• Context-aware payload generation",
            "• Zero-day vulnerability simulation",
            "• Intelligent exploit chaining",
            "• Custom fuzzing patterns",
            "• Behavioral anomaly detection",
            "• Advanced evasion techniques"
        ]
    }
    
    for category, vulns in vuln_categories.items():
        print(f"\n{category}")
        print("-" * 50)
        for vuln in vulns:
            print(f"  {vuln}")

def show_reporting_capabilities():
    """Show reporting capabilities"""
    print("\n📊 DSCYBERS REPORTING CAPABILITIES:")
    print("="*60)
    
    capabilities = {
        "📋 Report Formats": [
            "• Executive Summary (for management)",
            "• Technical Details (for security teams)", 
            "• HTML Reports (interactive web format)",
            "• JSON Reports (machine-readable)",
            "• CSV Reports (spreadsheet format)",
            "• PDF Reports (coming soon)"
        ],
        "📈 Risk Assessment": [
            "• Automated risk scoring (0-100)",
            "• Risk level categorization",
            "• Business impact analysis",
            "• Compliance framework mapping",
            "• Remediation prioritization",
            "• Executive dashboards"
        ],
        "🎯 Compliance Mapping": [
            "• OWASP Top 10 (2021 & 2024)",
            "• PCI DSS Requirements",
            "• NIST Cybersecurity Framework",
            "• ISO 27001 Controls",
            "• GDPR Privacy Requirements",
            "• Custom compliance frameworks"
        ]
    }
    
    for category, items in capabilities.items():
        print(f"\n{category}")
        print("-" * 40)
        for item in items:
            print(f"  {item}")

async def main():
    """Main demo function"""
    print_demo_banner()
    
    while True:
        show_demo_menu()
        
        try:
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                await run_demo_scan()
            
            elif choice == "2":
                print("\n🔧 Interactive Configuration Setup")
                print("This would normally run the full interactive setup wizard.")
                print("For demo purposes, we're using a pre-configured setup.")
                config = create_demo_configuration()
                print(f"Demo configuration created for target: {config.target_url}")
            
            elif choice == "3":
                show_vulnerability_types()
            
            elif choice == "4":
                show_reporting_capabilities()
            
            elif choice == "5":
                print("\n👋 Thank you for trying DSCYBERS!")
                print("For full functionality, install with: pip install -r requirements.txt")
                break
            
            else:
                print("❌ Invalid choice. Please select 1-5.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Demo interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
