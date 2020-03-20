import os

from setuptools import setup, find_packages

current_file_path = os.path.abspath(os.path.dirname(__file__))

readme_file_path = os.path.join(current_file_path, 'README.md')
with open(readme_file_path, 'r', encoding='utf-8') as f:
    readme = f.read()

version_file_path = os.path.join(current_file_path, 'poutyne-callbacks/version.py')
with open(version_file_path, 'rb') as f:
    # pylint: disable=exec-used,undefined-variable
    exec(compile(f.read(), version_file_path, 'exec'), globals(), locals())
    version = __version__

packages = find_packages()
setup(
    name='Poutyne-callbacks',
    version=version,
    author='Frédérik Paradis',
    author_email='fredy_14@live.fr',
    url='xxx',  # todo url
    download_url='https://github.com/GRAAL-Research/poutyne-callbacks/archive/v' + version + '.zip',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=packages,
    install_requires=['poutyne'],
    python_requires='>=3',
    description='A callbacks utilities for Poutyne.',
    long_description=readme,
    long_description_content_type='text/markdown',
)
