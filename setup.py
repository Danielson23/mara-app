from setuptools import setup, find_packages

setup(
    name='mara-app',
    version='1.5.2',

    description="Framework for distributing flask apps across separate packages with minimal dependencies",

    install_requires=[
        'mara-page>=1.2.3',
        'mara-db>=3.0.0',
        'mara-config>=0.2',
        'flask>=1.0'
    ],

    dependency_links=[
        'git+https://github.com/mara/mara-page.git@1.2.3#egg=mara-page-1.2.3',
        'git+https://github.com/mara/mara-db.git@3.0.0#egg=mara-db-3.0.0',
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={
    }
)
