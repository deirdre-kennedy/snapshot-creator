from setuptools import setup

setup(
    name='snapshot-creator',
    version='0.1',
    author='Deirdre Kennedy',
    description='Snapshot Creator is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['snappy'],
    url='https://github.com/deirdre-kennedy/snapshot-creator',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.snappy:cli
    ''',
)