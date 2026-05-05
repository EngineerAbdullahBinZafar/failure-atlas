from setuptools import setup, find_packages

setup(
    name="failure-atlas",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'failure_atlas': ['../data/*.json'],
    },
    install_requires=[],
    author="Engineer Abdullah Bin Zafar",
    description="A structured database of engineering failures with causal factor tagging.",
    license="MIT",
    keywords="engineering, failure-analysis, safety, research, dataset",
    url="https://github.com/EngineerAbdullahBinZafar/failure-atlas",
)
