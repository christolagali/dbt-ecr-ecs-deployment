FROM python
RUN mkdir -p /sourcecode
WORKDIR /sourcecode
COPY . .
RUN pip install -r requirements.txt
CMD python run_program.py