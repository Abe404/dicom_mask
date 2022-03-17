from setuptools import setup
from pathlib import Path

current_dir = Path(__file__).parent
long_description = (current_dir / "README.md").read_text()

setup(
  name = 'dicom_mask',
  packages = ['dicom_mask'],
  version = '0.0.20',
  license = 'BSD', 
  description = 'Export structure from dicom to numpy binary mask',
  long_description_content_type='text/markdown',
  long_description=long_description,
  author = 'Abraham George Smith',
  author_email = 'abe@abesmith.co.uk',
  url = 'https://github.com/Abe404/dicom_mask',
  download_url = 'https://github.com/Abe404/dicom_mask/archive/refs/tags/0.0.20.tar.gz',
  keywords = ['DICOM', 'NUMPY', 'RTSRUCT', 'MASK'],
  install_requires=[
      "dicompyler-core ==0.5.5",
      "numpy ==1.21.0",
      "pydicom ==2.2.0",
      "scikit-image ==0.18.2"
  ],
  classifiers=[
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent'
  ]
)
