from setuptools import setup

setup(
    url              = 'https://github.com/TheMrinalSinha/drishti',
    name             = 'pydrishti',
    author           = 'Mrinal Sinha',
    version          = '0.0.0',
    packages         = ['pydrishti'],
    description      = 'Image processing simplified',
    author_email     = 'mail@themrinalsinha.com',
    install_requires = [pkg for pkg in open('requirements.txt').read().split('\n') if pkg],
    classifiers      = [
        "Programming Language :: Python :: 3"
    ],
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
)
