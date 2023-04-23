from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.6'],
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions>=4.3,<5',
    ],
    'speed': [
        'orjson>=3.5.4',
        'aiodns>=1.1',
        'Brotli',
        'cchardet==2.1.7; python_version < "3.10"',
    ],
    'test': [
        'coverage[toml]',
        'pytest',
        'pytest-asyncio',
        'pytest-cov',
        'pytest-mock',
        'typing-extensions>=4.3,<5',
    ],
}

packages = [
    'hypecord',
    'hypecord.types',
    'hypecord.ui',
    'hypecord.webhook',
    'hypecord.app_commands',
    'hypecord.ext.commands',
    'hypecord.ext.tasks',
    'hypecord.mobile',
]

setup(
    name='hypecord.py',
    author='nap',
    url='https://github.com/devliftz/hypecord.py',
    version=1.7,
    packages=packages,
    license='MIT',
    description='A Python wrapper for the Discord API',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
