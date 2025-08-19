#!/usr/bin/env python3
"""
DSCYBERS System Integration Test & Validation Script

This script performs comprehensive testing of all DSCYBERS modules,
validates imports, checks dependencies, and ensures the system is
fully functional and integrated.

Author: Kashyap Divyansh - Cyber Security Researcher
"""

import sys
import os
import asyncio
import traceback
import importlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any

# Add the dscybers directory to Python path
current_dir = Path(__file__).parent
dscybers_dir = current_dir / "dscybers"
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(dscybers_dir))

class DSCYBERSValidator:
    """Comprehensive DSCYBERS system validator"""
    
    def __init__(self):
        self.test_results = {
            'module_imports': {},
            'dependencies': {},
            'functionality': {},
            'integration': {},
            'errors': []
        }
        self.total_tests = 0
        self.passed_tests = 0
        
    def print_header(self):
        """Print validation header"""
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DSCYBERS SYSTEM VALIDATION                                ║
║              AI-Powered Offensive Security Framework                        ║
║                                                                              ║
║  Author: Kashyap Divyansh - Cyber Security Researcher                       ║
║  Date: {datetime.now().strftime('%B %d, %Y %H:%M:%S')}                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
    
    def test_module_import(self, module_name: str, from_package: str = None) -> bool:
        """Test if a module can be imported successfully"""
        self.total_tests += 1
        try:
            if from_package:
                module = importlib.import_module(f".{module_name}", from_package)
            else:
                module = importlib.import_module(module_name)
            
            self.test_results['module_imports'][module_name] = {
                'status': 'SUCCESS',
                'module': module,
                'error': None
            }
            self.passed_tests += 1
            print(f"✅ Module import: {module_name}")
            return True
            
        except Exception as e:
            self.test_results['module_imports'][module_name] = {
                'status': 'FAILED',
                'module': None,
                'error': str(e)
            }
            self.test_results['errors'].append(f"Import error for {module_name}: {e}")
            print(f"❌ Module import: {module_name} - {e}")
            return False
    
    def test_core_modules(self):
        """Test all core DSCYBERS modules"""
        print("\n🔍 TESTING CORE MODULE IMPORTS")
        print("=" * 60)
        
        core_modules = [
            'core',
            'reporting', 
            'interactive_config',
            'vulnerability_detector',
            'ai_offensive_engine',
            'exploit_chains',
            'zero_day_simulation',
            'live_attack_demo',
            'enhanced_cli_v2',
            'config',
            'database',
            'guidance',
            'plugins',
            'ai_chains',
            'advanced_scanner'
        ]
        
        for module in core_modules:
            self.test_module_import(module, 'dscybers')
    
    def test_package_structure(self):
        """Test package structure and files"""
        print("\n📁 TESTING PACKAGE STRUCTURE")
        print("=" * 60)
        
        required_files = [
            'dscybers/__init__.py',
            'dscybers/__main__.py',
            'dscybers/core.py',
            'dscybers/reporting.py',
            'dscybers/live_attack_demo.py',
            'requirements.txt',
            'setup.py'
        ]
        
        for file_path in required_files:
            self.total_tests += 1
            full_path = current_dir / file_path
            if full_path.exists():
                print(f"✅ File exists: {file_path}")
                self.passed_tests += 1
            else:
                print(f"❌ File missing: {file_path}")
                self.test_results['errors'].append(f"Missing file: {file_path}")
    
    def test_dependencies(self):
        """Test required dependencies"""
        print("\n📦 TESTING DEPENDENCIES")
        print("=" * 60)
        
        required_packages = [
            'asyncio',
            'aiohttp', 
            'cryptography',
            'dataclasses',
            'json',
            'datetime',
            'typing',
            'pathlib',
            'argparse'
        ]
        
        for package in required_packages:
            self.total_tests += 1
            try:
                importlib.import_module(package)
                print(f"✅ Dependency: {package}")
                self.test_results['dependencies'][package] = 'AVAILABLE'
                self.passed_tests += 1
            except ImportError as e:
                print(f"❌ Dependency: {package} - {e}")
                self.test_results['dependencies'][package] = f'MISSING: {e}'
                self.test_results['errors'].append(f"Missing dependency: {package}")
    
    async def test_functionality(self):
        """Test core functionality"""
        print("\n⚡ TESTING CORE FUNCTIONALITY")
        print("=" * 60)
        
        # Test configuration creation
        self.total_tests += 1
        try:
            from dscybers.interactive_config import ScanConfiguration
            config = ScanConfiguration(
                target_url="https://example.com",
                target_type="web",
                scan_intensity="moderate"
            )
            print("✅ Configuration creation")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ Configuration creation - {e}")
            self.test_results['errors'].append(f"Configuration error: {e}")
        
        # Test vulnerability detector initialization
        self.total_tests += 1
        try:
            from dscybers.vulnerability_detector import AdvancedVulnerabilityDetector
            detector = AdvancedVulnerabilityDetector(config)
            print("✅ Vulnerability detector initialization")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ Vulnerability detector - {e}")
            self.test_results['errors'].append(f"Detector error: {e}")
        
        # Test AI engine initialization
        self.total_tests += 1
        try:
            from dscybers.ai_offensive_engine import AIOffensiveEngine
            ai_engine = AIOffensiveEngine(config)
            print("✅ AI offensive engine initialization")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ AI offensive engine - {e}")
            self.test_results['errors'].append(f"AI engine error: {e}")
    
    async def test_integration(self):
        """Test module integration"""
        print("\n🔗 TESTING MODULE INTEGRATION")
        print("=" * 60)
        
        # Test live demo initialization
        self.total_tests += 1
        try:
            from dscybers.live_attack_demo import LiveAttackDemonstrator
            demo = LiveAttackDemonstrator()
            print("✅ Live attack demo integration")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ Live demo integration - {e}")
            self.test_results['errors'].append(f"Demo integration error: {e}")
        
        # Test CLI integration
        self.total_tests += 1
        try:
            from dscybers.enhanced_cli_v2 import main as cli_main
            print("✅ CLI integration")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ CLI integration - {e}")
            self.test_results['errors'].append(f"CLI integration error: {e}")
    
    def test_launch_methods(self):
        """Test different launch methods"""
        print("\n🚀 TESTING LAUNCH METHODS")
        print("=" * 60)
        
        # Test launcher script
        self.total_tests += 1
        launcher_path = current_dir / "launch_dscybers.py"
        if launcher_path.exists():
            print("✅ Launcher script available")
            self.passed_tests += 1
        else:
            print("❌ Launcher script missing")
            self.test_results['errors'].append("Launcher script missing")
        
        # Test package main
        self.total_tests += 1
        try:
            from dscybers.__main__ import main as package_main
            print("✅ Package main available")
            self.passed_tests += 1
        except Exception as e:
            print(f"❌ Package main - {e}")
            self.test_results['errors'].append(f"Package main error: {e}")
    
    def generate_report(self):
        """Generate validation report"""
        print(f"\n📊 VALIDATION REPORT")
        print("=" * 60)
        
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        print(f"🎯 Total Tests: {self.total_tests}")
        print(f"✅ Passed: {self.passed_tests}")
        print(f"❌ Failed: {self.total_tests - self.passed_tests}")
        print(f"📈 Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 90:
            status = "🟢 EXCELLENT"
        elif success_rate >= 75:
            status = "🟡 GOOD"
        elif success_rate >= 50:
            status = "🟠 NEEDS WORK"
        else:
            status = "🔴 CRITICAL ISSUES"
        
        print(f"🏆 System Status: {status}")
        
        if self.test_results['errors']:
            print(f"\n⚠️  ISSUES FOUND:")
            for i, error in enumerate(self.test_results['errors'], 1):
                print(f"   {i}. {error}")
        
        # Generate fixes if needed
        if success_rate < 100:
            self.generate_fixes()
    
    def generate_fixes(self):
        """Generate fixes for common issues"""
        print(f"\n🔧 RECOMMENDED FIXES")
        print("=" * 60)
        
        fixes = [
            "1. Install missing dependencies: pip install -r requirements.txt",
            "2. Ensure Python 3.8+ is installed: python --version",
            "3. Check file permissions and directory structure",
            "4. Run from the correct directory containing dscybers/ folder",
            "5. Use: python launch_dscybers.py or python -m dscybers",
            "6. Check for syntax errors in Python files",
            "7. Verify all modules are in the dscybers/ directory"
        ]
        
        for fix in fixes:
            print(f"   {fix}")
    
    async def run_comprehensive_validation(self):
        """Run complete validation suite"""
        self.print_header()
        
        # Run all tests
        self.test_package_structure()
        self.test_dependencies()
        self.test_core_modules()
        await self.test_functionality()
        await self.test_integration()
        self.test_launch_methods()
        
        # Generate report
        self.generate_report()
        
        return self.passed_tests / self.total_tests >= 0.9

async def main():
    """Main validation function"""
    validator = DSCYBERSValidator()
    
    try:
        success = await validator.run_comprehensive_validation()
        
        if success:
            print(f"\n🎉 DSCYBERS SYSTEM VALIDATION COMPLETE!")
            print("✅ System is ready for deployment and testing")
            
            # Offer to run demo
            print(f"\n🚀 Ready to launch DSCYBERS Live Demo?")
            response = input("Launch demo now? (y/N): ").strip().lower()
            
            if response in ['y', 'yes']:
                print("\n🎮 Launching DSCYBERS Live Attack Demo...")
                try:
                    from dscybers.live_attack_demo import main as demo_main
                    await demo_main()
                except Exception as e:
                    print(f"❌ Demo launch failed: {e}")
                    print("🔧 Try: python dscybers/live_attack_demo.py")
        else:
            print(f"\n⚠️  SYSTEM NEEDS ATTENTION")
            print("Please address the issues above before using DSCYBERS")
    
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
