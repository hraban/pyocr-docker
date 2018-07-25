#!/usr/bin/env python3

# Mostly just C&P from
# https://pythontips.com/2016/02/25/ocr-on-pdf-files-using-python/
#
# Could certainly use some improvement. Just a POC.

import io
import json
from PIL import Image as PI
import pyocr
import pyocr.builders
import sys
from wand.image import Image

LANG = 'eng'

def main(argv):
    tool = pyocr.get_available_tools()[0]

    if LANG not in tool.get_available_languages():
        print("ocr language '%s' not available" % (LANG,), file=sys.stderr)
        os.exit(1)
    if len(argv) <= 1:
        print("Usage: ./main.py <INPUT_PDF>", file=sys.stderr)
        os.exit(1)
    infile = argv[1]

    req_image = []
    final_text = []
    image_pdf = Image(filename=infile)
    image_jpeg = image_pdf.convert('png')
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('png'))
    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=LANG,
            builder=pyocr.builders.TextBuilder())
        final_text.append(txt)
    # is this really a good idea?
    print(json.dumps(final_text))

if __name__ == '__main__':
    main(sys.argv)
