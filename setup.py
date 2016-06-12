from setuptools import find_packages, setup


version = '0.0.1'


setup(
    author='Charlie Denton',
    author_email='charlie@meshy.co.uk',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    description='A rich content field for django based on SirTrevorJS.',
    include_package_data=True,
    install_requires=[],
    name='django-sirtrevor-field',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/meshy/django-sirtrevor-field/',
    version=version,
)
