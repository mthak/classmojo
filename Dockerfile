from python:2
COPY * /root/
COPY battle /root/battle/
RUN virtualenv  ~/benv
RUN . ~/benv/bin/activate
RUN pip install -r /root/requirements.txt
RUN chdir /root/battle
RUN export PYTHONPATH=/root/battle
Entrypoint [ "python", "/root/app.py"]
EXPOSE 5000 5000/tcp

