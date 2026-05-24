FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r app/requirements.txt
CMD bash -c "sleep 10 && python app/event_generator.py && python app/analysis.py && python app/visualize.py"
