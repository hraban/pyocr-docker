FROM debian:latest

RUN apt-get update && \
    apt-get install -y \
        dumb-init \
        python3-pyocr \
        python3-wand \
        tesseract-ocr && \
    mkdir /app && \
    useradd myuser

WORKDIR /app
COPY main.py ./

USER myuser

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["./main.py"]
