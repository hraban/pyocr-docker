# Dockerized Python OCR

Simple POC for OCR using Python in Docker.

## Usage

Assuming your current directory has a file in it called `input.pdf`:

    $ docker run --rm -v "$PWD:/files" luyat/pyocr /files/input.pdf

This will output a JSON object for every page in the PDF on stdout.
