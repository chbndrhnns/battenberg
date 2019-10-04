import io
import re
from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with io.open("milhoja/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


install_requires = [
    'Click>=6.0',
    'cookiecutter>=1.6.0',
    'six>=1.12.0',
    # You'll also need to install libgit2 to get this to work.
    # See instructions here: https://www.pygit2.org/install.html
    'pygit2>=0.28.0'
]

setup(
    name='milhoja',
    version=version,
    description="Mixing Cookiecutter and Git to ends up sticking to your finger.",
    long_description=readme + '\n\n' + history,
    author="Raphael Medaer",
    author_email='raphael@medaer.me',
    url='https://github.com/rmedaer/milhoja',
    packages=[
        'milhoja',
    ],
    package_dir={'milhoja': 'milhoja'},
    entry_points={
        'console_scripts': [
            'milhoja=milhoja.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='milhoja',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    python_requires=">=3.6*",
    extras_require={
        'dev': ['pytest', 'flake8']
    }
)
