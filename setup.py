from setuptools import setup, find_packages

setup(
    name = "image_processing",
    version = "0.0.1",
    author = "Igor_Ferrer",
    author_email = "igori83@gmail.com",
    description= "pacote de processamento de imagens",
    long_description_content_type = "text/markdown",
    url = "https://github.com/igorferrer-data/image-processing-package",
    packages = find_packages(),
    install_requires=[
    'requests',
    'jupyterlab>=4.0.0,<5.0.0'
    ],

    python_requires='>=3.8',
)
