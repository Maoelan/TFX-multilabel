### Grade Multiclass Classification Pipeline with TensorFlow Extended

Dataset : [📚 Students Performance Dataset 📚](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)

This is a simple project to create a machine learning pipeline using TensorFlow Extended (TFX), consisting of the following components:

- **ExampleGen**: Used to convert the dataset into a format usable by TFX.
- **StatisticsGen**: Generates descriptive statistics about the dataset processed by ExampleGen, such as mean, variance,distribution, and others.
- **SchemaGen**: Produces a schema defining data types, value ranges, and expected features in the dataset, capable of validating whether the received dataset meets the pipeline's expectations.
- **ExampleValidator**: Validates data generated by SchemaGen for anomalies or errors, such as mismatched features or unexpected data types and ranges.
- **Transform**: Used for data preprocessing. In this project, numeric feature data is transformed into Z-score scale, and labels are converted to int64 format, as required by TFX.
Transform process : [Transform](https://github.com/Maoelan/TFX-grade-multiclass/blob/main/transform.py)
- **Tuner**: Performs automatic parameter search (hyperparameter tuning) to improve model performance, using random search in this project. Hyperparameter tunning strategy : [Hyperparameter tunning](https://github.com/Maoelan/TFX-grade-multiclass/blob/main/tuner.py)
- **Trainer**: Responsible for training the model based on data processed in the preceding pipeline steps. This involves model selection, training, and evaluation on the training data. Trainer process : [Trainer](https://github.com/Maoelan/TFX-grade-multiclass/blob/main/trainer.py)
- **Resolver**: Manages dependencies between artifacts, consuming trained model artifacts from training and evaluation.
- **Evaluator**: Evaluates the trained model's performance using specific metrics. This project uses metrics such as SparseCategoricalCrossentropy, SparseCategoricalAccuracy, Precision, Recall, and MulticlassConfusionMatrixPlot.
- **Pusher**: Deploys the trained model into production by sending it to accessible storage."

You can see the entire pipeline process here : [Pipeline](https://github.com/Maoelan/TFX-grade-multiclass/blob/main/classs-pipeline.ipynb)

### Model serving with Docker

Deploying a trained machine learning model using TFX in a Docker environment.

Dockerfile

```plaintext
FROM tensorflow/serving:latest

COPY ./serving_model_dir /models
ENV MODEL_NAME=grade-prediction-model
```

Build Docker Image

```plaintext
docker build -t grade-prediction-model-tf-serving .
```

Run docker container from docker image

```plaintext
docker run -p 8080:8501 grade-prediction-model-tf-serving
```

### Prediction
Making predictions using a model deployed in a Docker environment.

Prediction notebook : [Predict](https://github.com/Maoelan/TFX-grade-multiclass/blob/main/predict.ipynb)

### Problems encountered while creating a TFX pipeline

During the creation of this project, I encountered one unresolved issue: evaluator cannot generate bless even though the resolver and metrics used are correct.

### Documentation

TensorFlow Extended : [TFX](https://www.tensorflow.org/tfx)

TensorFlow Model Analysis Metrics : [TFMA](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/metrics)

Tensorflow Model Analysis Metrics and Plots : [TFMAP](https://www.tensorflow.org/tfx/model_analysis/metrics#multi-classmulti-label_classification_metrics)










