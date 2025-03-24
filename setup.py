import glob
from distutils.core import setup

# get all of the scripts
scripts = glob.glob('bin/*')

setup(
    name='docx2txt-setuptools-hotfix',
    packages=['docx2txt'],
    version='0.8.1',
    description='Fork of docx2txt with a hotfix applied. A pure python-based utility to extract text and images from docx files.',
    author='Gabriel Melo (forked from Ankush Shah)',
    author_email='gabrielmelo1992@gmail.com',
    url='https://github.com/gkmelo-dev/python-docx2txt',
    download_url='https://github.com/gkmelo-dev/python-docx2txt/archive/refs/tags/0.8.0-hotfix1.tar.gz',
    keywords=['python', 'docx', 'text', 'images', 'extract', 'hotfix'],
    scripts=scripts,
    classifiers=[],
    license='MIT',
)
