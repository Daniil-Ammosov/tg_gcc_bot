from setuptools import setup
import os

version = (('version' in os.environ) and os.environ['version'] or "0.0.1")

with open("tg_gcc_bot/version.py", "w") as f:
    f.write("__version__ = '{0}'\n".format(version))


if __name__ == "__main__":
    with open("requirements.txt") as f:
        setup(
            name='bot',
            version=version,
            author='ammosov',
            author_email='ammosov@tbdd.ru',

            packages=[
                "tg_gcc_bot",
            ],

            scripts=[
                "scripts/main_bot",
            ],

            description='Package for GCC telegram bot',
            install_requires=f.readlines()
        )
