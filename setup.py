import setuptools


setuptools.setup(
    name='rimo_utils',
    version='1.3.1',
    author='RimoChan',
    author_email='the@librian.net',
    description='RimoChan util.',
    long_description='喵喵喵！',
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/rimo_utils',
    packages=['rimo_utils'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=open('requirement.txt').read().splitlines(),
    python_requires='>=3.6',
)
