from setuptools import setup, find_packages
setup(
    name="MySimpleBlog",
    version="0.1",
    packages=['myblog'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Pavel Shastin",
    author_email="pavelshastin@yandex.ru",
    description="World's Cusine Blog",
    license="PSF",
    url="https://pavelshastin.pythonanywhere.com/",

    # could also include long_description, download_url, classifiers, etc.
)