from setuptools import setup, find_packages

pkgs = find_packages('src')

setup_kwds = dict(
    name='engine_ACC_TRB_2023',
    version="1.0.0",
    zip_safe=False,
    packages=pkgs,
    package_dir={'': 'src'},
    entry_points={},
    )

setup(**setup_kwds)