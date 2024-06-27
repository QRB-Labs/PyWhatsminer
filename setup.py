from distutils.core import setup


setup(
  name = 'pywhatsminer',
  packages = ['pywhatsminer'],
  version = '0.1.3',
  license='MIT',
  description = 'Unofficial Python based Api-Client (Wrapper) for MicroBT Whatsminer ASIC's',
  long_description="See full README at https://github.com/DAAMCS/PyWhatsminer",
  author = 'DAAMCS | Forked from Satoshi Anonymoto',
  author_email = 'me@daamcs.ru',
  url = 'https://github.com/DAAMCS/PyWhatsminer',
  download_url = 'https://github.com/DAAMCS/PyWhatsminer',
  keywords = ['whatsminer', 'microbt', 'api', 'btc', 'asic'],
  install_requires=[
          'passlib',
          'pycryptodome',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)