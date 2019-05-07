from python27
ADD battle /root/battle
RUN virtualenv --python2.7 ~/benv
RUN source ~/benv/bin/activate
RUN pip install requirements.txt
RUN chdir /root/battle
RUN export PYTHONPATH=/root/battle
Entrypoint ["python" "app.py"]

