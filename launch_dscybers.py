#!/usr/bin/env python3
"""
DSCYBERS Launcher

Quick launcher for the DSCYBERS AI-Powered Offensive Security Framework

Author: Kashyap Divyansh - Cyber Security Researcher
"""

import sys
import os
import asyncio

# Add the current directory to Python path for module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main launcher function"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                            DSCYBERS LAUNCHER                                 ║
║          AI-Powered Offensive Security Framework                            ║
║                                                                              ║
║  Author: Kashyap Divyansh - Cyber Security Researcher                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Import and run the live demo
        from dscybers.live_attack_demo import main as demo_main
        asyncio.run(demo_main())
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("🔧 Trying alternative import...")
        try:
            # Try running from current directory
            import sys
            sys.path.append('dscybers')
            from live_attack_demo import main as demo_main
            asyncio.run(demo_main())
        except Exception as e2:
            print(f"❌ Failed to launch DSCYBERS: {e2}")
            print("\n🛠️  TROUBLESHOOTING:")
            print("   1. Ensure you're in the correct directory")
            print("   2. Check Python version (3.8+ required)")
            print("   3. Install dependencies: pip install -r requirements.txt")
            print("   4. Run: python -m dscybers.live_attack_demo")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
