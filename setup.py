from setuptools import setup

setup(name='romi',
      version='0.1.0',
      description='RObotic Movement Interface.',
      # url='https://samuelepolimi.github.io/DariasPy-Doc/',
      author='Samuele Tosatto',
      author_email='samuele.tosatto@gmail.com',
      license='MIT',
      packages=['romi'],
      zip_safe=False,
      install_requires=[
          'numpy>=1.15.4',
          'scipy>=1.2.2'
      ])
