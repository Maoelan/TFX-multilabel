
import tensorflow as tf
import tensorflow_transform as tft

NUMERICAL_FEATURES = [
    "StudyTimeWeekly",
    "Absences",
    "Tutoring",
    "ParentalSupport",
    "GPA"
]

LABEL_KEY = "GradeClass"

def transformed_name(key):
    return key + '_xf'

def preprocessing_fn(inputs):
    outputs = {}

    for feature in NUMERICAL_FEATURES:
        outputs[transformed_name(feature)] = tft.scale_to_z_score(inputs[feature])
    
    # Transform the label
    outputs[transformed_name(LABEL_KEY)] = inputs[LABEL_KEY]
    
    return outputs