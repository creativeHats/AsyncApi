# Pull the latest version of the Python container.
FROM python:3.7
# Add the requirements.txt file to the image.
COPY requirements.txt /
COPY scripts/* /
COPY src /etc/asyncapi/src/
COPY resources /etc/asyncapi/resources/
# Install Python dependencies.
RUN pip install -r requirements.txt

WORKDIR /etc/asyncapi/src

ENV PYTHONPATH "/etc/asyncapi/src"
RUN chmod +x /run.sh
CMD /run.sh
