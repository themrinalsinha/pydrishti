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
        'dlib',
        'pyocr',
        'numpy',
        'Pillow',
        'imutils',
        'ipython',
        'matplotlib',
        'opencv-contrib-python',
    ],
)
