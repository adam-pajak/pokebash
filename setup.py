from setuptools import setup, find_packages

setup(
    name="pokebash",
    version="0.1.0",
    description="Pokebash game ... ",
    author="Your Name",
    packages=find_packages(),  # Automatically find packages in the directory
    python_requires='>=3.0',
    install_requires=[
        # Add any dependencies here, e.g., "pygame>=2.0.0"
    ],
    entry_points={
        'console_scripts': [
            'pokebash=game.__main__:main',  # Adjust if your main function is elsewhere
        ],
    },
)