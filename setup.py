from setuptools import setup, find_packages

setup(
    name='my_application',
    version='1.0',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    entry_points={
        'console_scripts': [
            'my_application=my_application.main:main'  # Adjust the entry point to your main function
        ]
    },
    test_suite='tests',
)
