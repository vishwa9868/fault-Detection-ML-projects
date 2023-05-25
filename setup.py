from setuotools import find_packages,setup


setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="vishwa@ineuron.ai",
    packages = find_packages(),
    install_requires=get_requirements(),

)