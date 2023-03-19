from setuptools import find_packages, setup

with open("README.md", "r") as fh:
	description = fh.read()
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
	name="api_key_detector",
	version="1.0.4",
	author="Siddharth Saxena",
	author_email="sidds020@gmail.com",
	packages=find_packages(),
    include_package_data=True,
	description="ML Based API Key Detector",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/alessandrodd/apk_api_key_extractor",
	license='MIT',
	python_requires='>=3.8',
	install_requires=REQUIREMENTS
)

