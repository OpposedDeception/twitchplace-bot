from setuptools import setup, find_packages

setup(
    name='twitchplace-bot',
    version='0.3,,
    description='A bot for TwitchPlace',
    author='OpposedDeception',
    author_email='noemail',
    url='https://github.com/OpposedDeception/twitchplace-bot',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyfiglet',
        'pillow'
        'numpy',
        'beautifulsoup4',
        'colorama',
        'webbrowser'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
