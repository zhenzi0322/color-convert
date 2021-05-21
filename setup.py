from setuptools import setup, find_packages

package = {
    "name": "color-convert",
    "version": "2.7",
    "description": "Color Conversion",
    "keywords": [
        "color",
        "color-convert",
        "convert"
    ],
    "homepage": "https://github.com/zhenzi0322/color-convert",
    "author": {
        "name": "Yu Zhen",
        "email": "82131529@qq.com"
    }
}

with open("README.md", encoding="utf-8") as data:
    long_description = data.read()

setup(
    name=package['name'],
    version=package["version"],
    url=package["homepage"],
    description=package["description"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    author=package["author"]["name"],
    author_email=package["author"]["email"],
    keywords=package["keywords"],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'
    ],
    zip_safe=False
)
