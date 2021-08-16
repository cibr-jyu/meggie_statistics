from setuptools import setup

setup(
    name='meggie_statistics',
    version='0.2.0',
    license='BSD',
    packages=['meggie_statistics'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'meggie>=1.2.0'
    ]
)
