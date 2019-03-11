from setuptools import setup

setup(
    name='cleverwrap2',
    packages=['cleverwrap'],
    license='MIT',
    install_requires=['requests'],
    version='0.1.0',
    url='https://github.com/snoonetIRC/cleverwrap2',
    description='A wrapper for the official cleverbot.com API',
    author='linuxdemon',
    author_email='linuxdaemon@snoonet.org',
    keywords=['cleverbot', 'wrapper', 'clever'],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
