from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dscybers',
    version='1.2.0',
    description='DSCYBERS v1.2 — Multi-Tool Web Vulnerability Scanner',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='DSCYBERS Team',
    author_email='contact@dscybers.com',
    url='https://github.com/DSCYBERS/dscyberss',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
    ],
    install_requires=[
        'requests>=2.25.0',
        'colorama>=0.4.0',
        'beautifulsoup4>=4.9.0',
        'lxml>=4.6.0',
        'python-dateutil>=2.8.0',
        'urllib3>=1.26.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
        ],
        'reporting': [
            'reportlab>=3.5.0',
            'matplotlib>=3.3.0',
            'jinja2>=2.11.0',
        ],
        'ai': [
            'scikit-learn>=0.24.0',
            'numpy>=1.19.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'dscybers = dscybers.__main__:main',
        ],
    },
    python_requires='>=3.6',
    keywords='security vulnerability scanner penetration-testing web-security',
    project_urls={
        'Bug Reports': 'https://github.com/DSCYBERS/dscyberss/issues',
        'Source': 'https://github.com/DSCYBERS/dscyberss',
        'Documentation': 'https://github.com/DSCYBERS/dscyberss/wiki',
    },
)
