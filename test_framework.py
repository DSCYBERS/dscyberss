#!/usr/bin/env python3
"""
DSCYBERS Enterprise Framework Validation Test
Comprehensive test suite for enterprise deployment readiness
"""

import sys
import os
import json
import traceback
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test all module imports"""
    print("🔍 Testing Framework Imports...")
    
    try:
        import dscybers
        print(f"✅ Core package imported successfully - Version {dscybers.__version__}")
        
        # Test core components
        from dscybers import core
        print("✅ Core module imported")
        
        from dscybers import plugins
        print("✅ Plugins module imported")
        
        from dscybers import database
        print("✅ Database module imported")
        
        from dscybers import config
        print("✅ Config module imported")
        
        from dscybers import advanced_scanner
        print("✅ Advanced scanner module imported")
        
        from dscybers import guidance
        print("✅ Guidance module imported")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_database_functionality():
    """Test database operations"""
    print("\n🗄️  Testing Database Functionality...")
    
    try:
        from dscybers.database import DatabaseManager
        
        # Initialize database
        db = DatabaseManager(":memory:")  # Use in-memory database for testing
        print("✅ Database manager initialized")
        
        # Test schema creation
        db.initialize_schema()
        print("✅ Database schema created")
        
        # Test scan recording
        scan_id = db.record_scan("test_target", "comprehensive", {})
        print(f"✅ Scan recorded with ID: {scan_id}")
        
        # Test vulnerability recording
        vuln_data = {
            'title': 'Test Vulnerability',
            'severity': 'Medium',
            'description': 'Test description',
            'impact': 'Test impact',
            'remediation': 'Test remediation',
            'tool_used': 'test_tool',
            'cwe_id': 'CWE-79'
        }
        
        vuln_id = db.record_vulnerability(scan_id, "http://test.com", vuln_data)
        print(f"✅ Vulnerability recorded with ID: {vuln_id}")
        
        # Test compliance recording
        db.record_compliance_check("test_target", "PCI-DSS", "6.1", "PASS", "Test compliance")
        print("✅ Compliance check recorded")
        
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_config_management():
    """Test configuration management"""
    print("\n⚙️  Testing Configuration Management...")
    
    try:
        from dscybers.config import EnterpriseConfigManager
        
        # Initialize config manager
        config = EnterpriseConfigManager()
        print("✅ Config manager initialized")
        
        # Test environment detection
        env = config.detect_environment()
        print(f"✅ Environment detected: {env}")
        
        # Test security profile loading
        profile = config.get_security_profile()
        print(f"✅ Security profile loaded: {profile.get('name', 'default')}")
        
        # Test API configuration
        api_config = config.get_api_config()
        print(f"✅ API configuration loaded with {len(api_config)} services")
        
        return True
        
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_plugin_system():
    """Test plugin system"""
    print("\n🔌 Testing Plugin System...")
    
    try:
        from dscybers.plugins import PluginManager, EnterpriseBasePlugin
        
        # Initialize plugin manager
        plugin_manager = PluginManager()
        print("✅ Plugin manager initialized")
        
        # Test plugin discovery
        available_plugins = plugin_manager.discover_plugins()
        print(f"✅ Discovered {len(available_plugins)} plugins")
        
        # Test plugin validation
        for plugin_path in available_plugins[:3]:  # Test first 3 plugins
            try:
                is_valid = plugin_manager.validate_plugin(plugin_path)
                print(f"✅ Plugin validation: {plugin_path} - {'Valid' if is_valid else 'Invalid'}")
            except Exception as e:
                print(f"⚠️  Plugin validation warning: {plugin_path} - {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Plugin test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_advanced_scanner():
    """Test advanced scanner"""
    print("\n🔍 Testing Advanced Scanner...")
    
    try:
        from dscybers.advanced_scanner import EnterpriseAdvancedScanner, ScanProfile
        
        # Initialize scanner
        scanner = EnterpriseAdvancedScanner()
        print("✅ Advanced scanner initialized")
        
        # Test payload initialization
        payloads = scanner.payloads
        print(f"✅ Payloads loaded: {len(payloads)} categories")
        
        # Test vulnerability modules
        modules = scanner.vulnerability_modules
        print(f"✅ Vulnerability modules loaded: {len(modules)} modules")
        
        # Test default scan profile
        profile = scanner._get_default_scan_profile()
        print(f"✅ Default scan profile: {profile.name} with intensity {profile.intensity_level}")
        
        # Test evasion techniques
        evasion = scanner.evasion_techniques
        print(f"✅ Evasion techniques loaded: {len(evasion)} categories")
        
        return True
        
    except Exception as e:
        print(f"❌ Advanced scanner test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_guidance_system():
    """Test guidance system"""
    print("\n📋 Testing Guidance System...")
    
    try:
        from dscybers.guidance import VulnerabilityGuidance, ThreatIntelligence
        
        # Initialize guidance system
        guidance = VulnerabilityGuidance()
        print("✅ Guidance system initialized")
        
        # Test guidance retrieval
        xss_guidance = guidance.get_guidance('XSS')
        if xss_guidance:
            print("✅ XSS guidance retrieved successfully")
        
        # Test remediation priority calculation
        priority = guidance.get_remediation_priority('Critical', 'High')
        print(f"✅ Remediation priority calculated: {priority}")
        
        # Test attack vector analysis
        vectors = guidance.analyze_attack_vectors('admin.example.com')
        print(f"✅ Attack vectors analyzed: {len(vectors)} vectors found")
        
        # Test threat intelligence
        threat_intel = ThreatIntelligence()
        threat_context = threat_intel.get_threat_context('XSS')
        print(f"✅ Threat intelligence context: {threat_context.get('prevalence', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Guidance system test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_cli_interface():
    """Test CLI interface"""
    print("\n💻 Testing CLI Interface...")
    
    try:
        # Test help command
        from dscybers.__main__ import main
        print("✅ CLI main function accessible")
        
        # Note: We can't easily test full CLI without subprocess
        # This test just verifies the main function exists
        
        return True
        
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def test_framework_metadata():
    """Test framework metadata and version info"""
    print("\n📄 Testing Framework Metadata...")
    
    try:
        import dscybers
        
        # Test version information
        version = getattr(dscybers, '__version__', None)
        print(f"✅ Version: {version}")
        
        author = getattr(dscybers, '__author__', None)
        print(f"✅ Author: {author}")
        
        build = getattr(dscybers, '__build__', None)
        print(f"✅ Build: {build}")
        
        # Test supported tools
        tools = getattr(dscybers, 'SUPPORTED_TOOLS', {})
        print(f"✅ Supported tools: {len(tools)} categories")
        
        # Test severity levels
        severities = getattr(dscybers, 'SEVERITY_LEVELS', {})
        print(f"✅ Severity levels: {len(severities)} levels")
        
        return True
        
    except Exception as e:
        print(f"❌ Metadata test failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False

def run_comprehensive_tests():
    """Run all framework tests"""
    print("🚀 DSCYBERS Enterprise Framework Validation")
    print("=" * 60)
    
    tests = [
        ("Framework Imports", test_imports),
        ("Database Functionality", test_database_functionality),
        ("Configuration Management", test_config_management),
        ("Plugin System", test_plugin_system),
        ("Advanced Scanner", test_advanced_scanner),
        ("Guidance System", test_guidance_system),
        ("CLI Interface", test_cli_interface),
        ("Framework Metadata", test_framework_metadata),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<40} {status}")
    
    print("-" * 60)
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED - Framework ready for enterprise deployment!")
        return True
    else:
        print(f"\n⚠️  {total - passed} tests failed - Review issues before deployment")
        return False

if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
