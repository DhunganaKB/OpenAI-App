FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
EXPOSE 80
CMD ["main.py"]
