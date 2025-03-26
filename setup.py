from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith('#')]

setup(
    name='openmanus',
    version='0.1.0',
    author='Xinbin Liang',
    author_email='mannaandpoem@gmail.com',
    description='An open-source framework for building general AI agents',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LearnHD/OpenManus',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.4.3',
            'pytest-asyncio>=0.21.1',
            'pytest-cov>=4.1.0',
            'pytest-mock>=3.12.0',
            'pytest-xdist>=3.5.0',
            'black>=23.11.0',
            'isort>=5.12.0',
            'flake8>=6.1.0',
            'pylint>=3.0.2',
            'mypy>=1.7.1',
        ],
        'docs': [
            'sphinx>=7.2.6',
            'sphinx-rtd-theme>=1.3.0',
            'sphinx-autodoc-typehints>=1.24.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'openmanus=app.main:main',
        ],
    },
)