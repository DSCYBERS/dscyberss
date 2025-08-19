# 🔥 DSCYBERS v2.0 - Next-Gen Web Vulnerability Scanner

DSCYBERS is an AI-powered web application security testing toolkit designed to scan, detect, and help exploit critical web vulnerabilities in modern web applications. It automates security checks across **OWASP Top 10 (2021 & 2024 updates)** + advanced real-world attack vectors that are commonly exploited by penetration testers, bug bounty hunters, and security researchers.

![Badge](https://img.shields.io/badge/DSCYBERS-v2.0-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Professional-orange)

## ✨ New in v2.0

- 🤖 **AI-Powered Payload Generation** - Context-aware exploit generation
- 🔧 **Interactive Configuration Wizard** - User-friendly setup for API keys and credentials
- 📊 **Professional Reporting** - Executive summaries, technical details, compliance mapping
- ⚡ **Advanced Vulnerability Detection** - 50+ vulnerability types including OWASP 2024
- 🛡️ **Zero-Day Simulation** - AI-assisted fuzzing for unknown vulnerabilities
- 🔗 **Exploit Chaining** - Automated combination of vulnerabilities
- 🌐 **Multi-Protocol Support** - HTTP/1.1, HTTP/2, HTTP/3, GraphQL, REST APIs

## 🎯 Vulnerabilities Detected

### 🔹 OWASP Top 10 (2021 & 2024)
- **Injection** (SQL, NoSQL, Command, LDAP)
- **Broken Authentication** & Session Management
- **Sensitive Data Exposure** & Cryptographic Failures
- **XML External Entities (XXE)**
- **Broken Access Control** & Authorization
- **Security Misconfigurations**
- **Cross-Site Scripting (XSS)** - Reflected, Stored, DOM-based
- **Insecure Deserialization**
- **Using Components with Known Vulnerabilities**
- **Insufficient Logging & Monitoring**

### 🔹 Advanced & Emerging Threats
- **Server-Side Request Forgery (SSRF)** - Advanced payload automation
- **GraphQL Exploits** - Introspection leakage, injection attacks
- **JWT & Token Attacks** - None algorithm, weak signing keys
- **Business Logic Flaws** - AI-assisted workflow bypass detection
- **API Security Risks** - Broken object level auth, mass assignment
- **HTTP/2 & HTTP/3 Vulnerabilities** - HPACK bomb, rapid reset DoS
- **Template Injection (SSTI)** - Flask/Jinja/Django exploitation
- **Web Cache Poisoning** & Cache Deception
- **CORS Misconfigurations** leading to account takeover
- **Exposed Debug Panels** & Admin Consoles

### 🔹 AI-Enhanced Detection
- **Zero-Day Payload Simulation** - Self-learning fuzzing engine
- **Chained Attack Detection** - SSRF → RCE → Privilege Escalation
- **Context-Aware Payloads** - Dynamic payload generation based on target
- **Behavioral Anomaly Detection** - ML-powered unusual response analysis

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/dscybers.git
cd dscybers

# Install dependencies
pip install -r requirements.txt

# Install DSCYBERS package
pip install -e .
```

### Basic Usage

```bash
# Quick scan with minimal setup
python -m dscybers https://example.com

# Interactive configuration wizard
python -m dscybers --interactive

# Use configuration file
python -m dscybers --config myconfig.json

# Aggressive scan with AI features
python -m dscybers https://api.example.com --intensity aggressive
```

### Demo Mode

```bash
# Run the comprehensive demo
python demo_dscybers.py
```

## 🔧 Interactive Configuration

DSCYBERS v2.0 includes an interactive configuration wizard that guides you through setting up:

- **Target Configuration** - URL, type (web/API/GraphQL/mobile/cloud)
- **Authentication** - Basic, Bearer tokens, API keys, OAuth, custom headers
- **API Integrations** - Shodan, VirusTotal, Censys, SecurityTrails
- **Cloud Credentials** - AWS, Azure, GCP for cloud misconfiguration testing
- **Scanning Parameters** - Intensity, threads, rate limiting
- **Advanced Features** - AI payloads, exploit chaining, zero-day simulation

### Sample Configuration

```json
{
  "target_url": "https://api.example.com",
  "target_type": "api",
  "auth_type": "bearer",
  "bearer_token": "your-api-token",
  "scan_intensity": "medium",
  "enable_ai_payloads": true,
  "compliance_frameworks": ["owasp", "pci_dss"]
}
```

## 📊 Professional Reporting

Generate comprehensive security assessment reports:

### Report Formats
- **HTML** - Interactive web reports with charts and metrics
- **JSON** - Machine-readable for integration with other tools
- **CSV** - Spreadsheet-compatible for data analysis
- **PDF** - Executive presentations (coming soon)

### Report Features
- **Executive Summary** - High-level overview for management
- **Risk Assessment** - Automated scoring and risk levels
- **Technical Details** - Detailed findings for security teams
- **Compliance Mapping** - OWASP, PCI DSS, NIST, ISO 27001
- **Remediation Guide** - Prioritized action items

```bash
# Generate HTML report
python -m dscybers https://example.com --format html --output report.html

# Generate JSON report with compliance mapping
python -m dscybers https://example.com --format json --output results.json
```

## 🤖 AI-Powered Features

### Intelligent Payload Generation
- Context-aware SQL injection payloads
- Advanced XSS bypass techniques
- Custom command injection vectors
- GraphQL-specific exploits
- JWT manipulation attacks

### Zero-Day Simulation
- ML-powered fuzzing engine
- Behavioral response analysis
- Pattern recognition for unknown vulnerabilities
- Adaptive payload mutation

### Exploit Chaining
- Automatic vulnerability combination
- Multi-stage attack simulation
- Privilege escalation detection
- Lateral movement analysis

## 🛡️ Security & Ethics

**⚠️ IMPORTANT: Legal Use Only**

DSCYBERS is designed for:
- ✅ Authorized penetration testing
- ✅ Security research and education
- ✅ Vulnerability assessment with permission
- ✅ Bug bounty hunting (with proper authorization)

**Prohibited Uses:**
- ❌ Unauthorized scanning of systems you don't own
- ❌ Malicious attacks or actual exploitation
- ❌ Violation of computer fraud and abuse laws
- ❌ Bypassing security controls without permission

## 📚 Documentation

### Command Line Options

```bash
dscybers [OPTIONS] [TARGET]

Options:
  -i, --interactive           Run interactive configuration wizard
  -c, --config FILE          Use configuration file
  -o, --output FILE          Output file for results
  -f, --format FORMAT        Output format (json, csv, html, pdf)
      --intensity LEVEL      Scan intensity (light, medium, aggressive)
      --threads NUM          Number of concurrent threads
      --timeout SECONDS      Request timeout
      --delay SECONDS        Delay between requests
      --examples             Show detailed usage examples
      --create-demo-config   Create demo configuration file
```

### Configuration File Schema

```json
{
  "target_url": "string (required)",
  "target_type": "web|api|graphql|mobile|cloud",
  "auth_type": "none|basic|bearer|api_key|oauth|custom",
  "scan_intensity": "light|medium|aggressive",
  "max_threads": "integer (1-50)",
  "enable_ai_payloads": "boolean",
  "enable_exploit_chaining": "boolean",
  "compliance_frameworks": ["owasp", "pci_dss", "gdpr"]
}
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test categories
python -m pytest tests/test_dscybers.py -v

# Run with coverage
python -m pytest tests/ --cov=dscybers --cov-report=html
```

## 📈 Performance

DSCYBERS v2.0 is optimized for:
- **Concurrent Scanning** - Multi-threaded vulnerability detection
- **Rate Limiting** - Respectful scanning to avoid service disruption
- **Memory Efficiency** - Streaming responses for large targets
- **Caching** - Intelligent caching of reconnaissance data

### Benchmark Results
- **Small Target (< 50 pages)**: 2-5 minutes
- **Medium Target (50-200 pages)**: 5-15 minutes  
- **Large Target (200+ pages)**: 15-45 minutes
- **API Endpoints**: 1-10 minutes depending on complexity

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/your-org/dscybers.git
cd dscybers

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

DSCYBERS is a security testing tool intended for authorized use only. Users are responsible for ensuring they have explicit permission to test any systems they scan. The developers assume no liability for misuse of this tool.

## 🌟 Star History

If you find DSCYBERS useful, please consider giving it a star! ⭐

## 📞 Support

- 📧 **Email**: security@dscybers.com
- 💬 **Discord**: [Join our community](https://discord.gg/dscybers)
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-org/dscybers/issues)
- 📖 **Documentation**: [Full Documentation](https://docs.dscybers.com)

---

**Made with ❤️ for the security community**
