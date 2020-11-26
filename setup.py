from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
        name='piepd',
        version='0.0.1.2',
        description='Buzzer utility for pi',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author_email='william.wyatt@cgu.edu',
        url='https://github.com/Tsangares/epd',
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            'Pillow',
            ],
        entry_points={
            'console_scripts': [
                'beep = src.beep:main',
                ]
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',
)
