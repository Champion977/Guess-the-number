from setuptools import setup

setup(
    name="guess-the-number",
    version="0.1",
    py_modules=["game"],
    description="Gra: zgadnij liczbę",
    author="Łukasz",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'guess=game:main',
        ],
    },
)
