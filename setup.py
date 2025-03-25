from setuptools import setup, find_packages

setup(
    name="xfce4-xr-desktop",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'gi>=3.38.0',
        'numpy>=1.21.0',
        'pygobject>=3.38.0',
        'python-xlib>=0.33',
        'evdev>=1.6.1'
    ],
    entry_points={
        'console_scripts': [
            'xfce4-xr-desktop=main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="XR desktop integration for XFCE4",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rebroad/xfce4-xr-desktop",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Desktop Environment :: XFCE",
    ],
    python_requires='>=3.8',
) 