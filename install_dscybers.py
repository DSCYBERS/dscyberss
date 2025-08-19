#!/usr/bin/env python3
"""
DSCYBERS Installation and Setup Script

Automated installation, configuration, and validation for the
DSCYBERS AI-Powered Offensive Security Framework.

Author: Kashyap Divyansh - Cyber Security Researcher
"""

import sys
import os
import subprocess
import platform
import urllib.request
from pathlib import Path
from datetime import datetime

class DSCYBERSInstaller:
    """DSCYBERS installation and setup manager"""
    
    def __init__(self):
        self.platform = platform.system()
        self.python_version = sys.version_info
        self.install_dir = Path(__file__).parent
        
    def print_banner(self):
        """Print installation banner"""
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                      DSCYBERS INSTALLATION WIZARD                           ║
║              AI-Powered Offensive Security Framework                        ║
║                                                                              ║
║  Author: Kashyap Divyansh - Cyber Security Researcher                       ║
║  Version: 2.0.0 Enterprise Edition                                          ║
║  Date: {datetime.now().strftime('%B %d, %Y')}                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

🖥️  Platform: {self.platform}
🐍 Python: {self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}
📁 Install Directory: {self.install_dir}
        """)
    
    def check_prerequisites(self):
        """Check system prerequisites"""
        print("🔍 CHECKING PREREQUISITES")
        print("=" * 50)
        
        # Check Python version
        if self.python_version < (3, 8):
            print("❌ Python 3.8+ required")
            print(f"   Current version: {self.python_version.major}.{self.python_version.minor}")
            return False
        else:
            print("✅ Python version compatible")
        
        # Check pip
        try:
            import pip
            print("✅ pip available")
        except ImportError:
            print("❌ pip not found")
            print("   Please install pip first")
            return False
        
        # Check internet connectivity
        try:
            urllib.request.urlopen('https://pypi.org', timeout=5)
            print("✅ Internet connectivity")
        except:
            print("⚠️  Limited internet connectivity")
            print("   Some features may not work")
        
        return True
    
    def install_dependencies(self):
        """Install required dependencies"""
        print("\n📦 INSTALLING DEPENDENCIES")
        print("=" * 50)
        
        requirements_file = self.install_dir / "requirements.txt"
        
        if not requirements_file.exists():
            print("⚠️  requirements.txt not found, installing core dependencies...")
            core_packages = [
                "requests>=2.25.0",
                "aiohttp>=3.8.0", 
                "cryptography>=3.4.0",
                "colorama>=0.4.4"
            ]
            
            for package in core_packages:
                self.install_package(package)
        else:
            print(f"📋 Installing from {requirements_file}")
            try:
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
                ], capture_output=True, text=True, timeout=300)
                
                if result.returncode == 0:
                    print("✅ Dependencies installed successfully")
                else:
                    print(f"⚠️  Some dependencies failed to install:")
                    print(result.stderr)
            except subprocess.TimeoutExpired:
                print("⚠️  Installation timeout - some packages may be missing")
            except Exception as e:
                print(f"❌ Installation failed: {e}")
    
    def install_package(self, package):
        """Install a single package"""
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", package
            ], capture_output=True, check=True)
            print(f"✅ Installed: {package}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Failed to install {package}: {e}")
    
    def setup_directories(self):
        """Set up required directories"""
        print("\n📁 SETTING UP DIRECTORIES")
        print("=" * 50)
        
        directories = [
            "reports",
            "logs",
            "configs",
            "temp",
            "data"
        ]
        
        for dir_name in directories:
            dir_path = self.install_dir / dir_name
            try:
                dir_path.mkdir(exist_ok=True)
                print(f"✅ Directory: {dir_name}")
            except Exception as e:
                print(f"⚠️  Failed to create {dir_name}: {e}")
    
    def create_config_file(self):
        """Create default configuration file"""
        print("\n⚙️  CREATING CONFIGURATION")
        print("=" * 50)
        
        config_content = f"""# DSCYBERS Configuration File
# Author: Kashyap Divyansh - Cyber Security Researcher
# Generated: {datetime.now().isoformat()}

[general]
version = 2.0.0
author = Kashyap Divyansh - Cyber Security Researcher
debug = false
log_level = INFO

[scanning]
default_timeout = 30
max_threads = 10
rate_limit = 0.1
user_agent = DSCYBERS-v2.0-SecurityScanner

[ai_engine]
enable_ai_payloads = true
enable_exploit_chaining = true
enable_zero_day_simulation = true
confidence_threshold = 0.7

[reporting]
default_format = html
include_charts = true
executive_summary = true

[security]
encrypt_credentials = true
secure_storage = true
audit_logging = true
"""
        
        config_path = self.install_dir / "configs" / "dscybers.conf"
        try:
            config_path.parent.mkdir(exist_ok=True)
            config_path.write_text(config_content)
            print(f"✅ Configuration file created: {config_path}")
        except Exception as e:
            print(f"⚠️  Failed to create config: {e}")
    
    def validate_installation(self):
        """Validate the installation"""
        print("\n🔍 VALIDATING INSTALLATION")
        print("=" * 50)
        
        # Test imports
        test_modules = [
            'dscybers',
            'dscybers.core',
            'dscybers.live_attack_demo'
        ]
        
        success_count = 0
        
        for module in test_modules:
            try:
                __import__(module)
                print(f"✅ Module: {module}")
                success_count += 1
            except ImportError as e:
                print(f"❌ Module: {module} - {e}")
        
        success_rate = success_count / len(test_modules)
        
        if success_rate >= 0.8:
            print(f"\n🎉 Installation successful! ({success_count}/{len(test_modules)} modules)")
            return True
        else:
            print(f"\n⚠️  Installation incomplete ({success_count}/{len(test_modules)} modules)")
            return False
    
    def create_launchers(self):
        """Create launcher scripts for different platforms"""
        print("\n🚀 CREATING LAUNCHERS")
        print("=" * 50)
        
        # Windows batch file
        if self.platform == "Windows":
            batch_content = f"""@echo off
echo Starting DSCYBERS AI-Powered Offensive Security Framework
echo Author: Kashyap Divyansh - Cyber Security Researcher
echo.
cd /d "{self.install_dir}"
python launch_dscybers.py
pause
"""
            batch_path = self.install_dir / "start_dscybers.bat"
            batch_path.write_text(batch_content)
            print("✅ Windows launcher: start_dscybers.bat")
        
        # Linux/Mac shell script
        else:
            shell_content = f"""#!/bin/bash
echo "Starting DSCYBERS AI-Powered Offensive Security Framework"
echo "Author: Kashyap Divyansh - Cyber Security Researcher"
echo ""
cd "{self.install_dir}"
python3 launch_dscybers.py
"""
            shell_path = self.install_dir / "start_dscybers.sh"
            shell_path.write_text(shell_content)
            shell_path.chmod(0o755)
            print("✅ Unix launcher: start_dscybers.sh")
    
    def print_usage_instructions(self):
        """Print usage instructions"""
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        INSTALLATION COMPLETE!                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

🚀 LAUNCH DSCYBERS:

Method 1 - Simple Launcher:
   python launch_dscybers.py

Method 2 - Module Execution:
   python -m dscybers

Method 3 - Platform Launcher:
""")
        
        if self.platform == "Windows":
            print("   start_dscybers.bat")
        else:
            print("   ./start_dscybers.sh")
        
        print(f"""
Method 4 - Direct Demo:
   python dscybers/live_attack_demo.py

📚 FEATURES:
   ✅ 94 Attack Vectors across 10 categories
   ✅ AI-Powered vulnerability detection  
   ✅ Real-time exploit chain generation
   ✅ Zero-day simulation engine
   ✅ APT-level attack patterns
   ✅ Interactive live demonstrations
   ✅ Professional reporting system

⚠️  SECURITY NOTICE:
   🔒 For authorized penetration testing only
   📋 Ensure proper permissions before testing
   ⚖️  Unauthorized access is illegal

💡 SUPPORT:
   📧 Author: Kashyap Divyansh - Cyber Security Researcher
   🌐 Documentation: See README.md
   🐛 Issues: Check logs/ directory

🎉 Ready to begin your security assessment!
        """)
    
    def run_installation(self):
        """Run the complete installation process"""
        try:
            self.print_banner()
            
            if not self.check_prerequisites():
                print("\n❌ Prerequisites not met. Installation aborted.")
                return False
            
            self.install_dependencies()
            self.setup_directories() 
            self.create_config_file()
            self.create_launchers()
            
            if self.validate_installation():
                self.print_usage_instructions()
                
                # Offer to start DSCYBERS
                print("\n🎮 Start DSCYBERS now?")
                response = input("Launch DSCYBERS Live Demo? (y/N): ").strip().lower()
                
                if response in ['y', 'yes']:
                    print("\n🚀 Launching DSCYBERS...")
                    try:
                        import asyncio
                        from dscybers.live_attack_demo import main as demo_main
                        asyncio.run(demo_main())
                    except Exception as e:
                        print(f"❌ Launch failed: {e}")
                        print("🔧 Try: python launch_dscybers.py")
                
                return True
            else:
                print("\n⚠️  Installation completed with issues")
                print("   Some features may not work correctly")
                return False
        
        except KeyboardInterrupt:
            print("\n⚠️  Installation interrupted by user")
            return False
        except Exception as e:
            print(f"\n❌ Installation failed: {e}")
            return False

def main():
    """Main installation function"""
    installer = DSCYBERSInstaller()
    success = installer.run_installation()
    
    if success:
        print("\n✅ DSCYBERS installation successful!")
    else:
        print("\n❌ DSCYBERS installation failed!")
        print("   Please check error messages above")
    
    return success

if __name__ == "__main__":
    main()
