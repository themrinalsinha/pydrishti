from setuptools import setup

setup(
    url              = 'https://github.com/TheMrinalSinha/drishti',
    name             = 'pydrishti',
    author           = 'Mrinal Sinha',
    version          = '0.1-alpha',
    zip_safe         = False,
    liscense         = 'MIT',
    packages         = ['pydrishti'],
    description      = 'Image process package',
    author_email     = 'mail@themrinalsinha.com',
    install_requires = [
        'dlib>=19.17.0',
        'pyocr>=0.7.2',
        'numpy>=1.17.0',
        'Pillow>=6.1.0',
        'imutils>=0.5.3',
        'ipython>=7.7.0',
        'matplotlib>=3.1.1',
        'opencv-contrib-python>=4.1.0.25',
    ],
)
