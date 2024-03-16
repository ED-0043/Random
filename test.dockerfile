FROM Python:3.7

WORKDIR /ML_pipeline

ADD ./ML_pipeline

RUN pip install --no-cache-dir -r requirements

EXPOSE 80

ENV NAME zaworldo

CMD ['Python', 'ML_pipeline.py']

#in cmdline docker build -t heart_disease_model .
#tagging the image docker tag heart_disease:latest heart_disease_model:1.0