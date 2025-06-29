FROM python:3.11
ADD requirements.txt .
ADD main.py .
ADD history.ndjson .
RUN touch /history.ndjson
RUN chmod 755 /history.ndjson
RUN pip install -r requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "80"]