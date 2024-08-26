from setuptools import setup, find_packages

setup(
    name='server_app',
    version='1.0.0',
    description='A FastAPI-based server application for balance sheet reporting',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Binyam Atnafu',
    author_email='binasisayet8790@gmail.com',
    url='https://github.com/Bina-man/code-drills.git',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'server-app=server_app.main:app',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
