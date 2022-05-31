# Sleep-disorder-Classification

A hierarchical approach for the diagnosis of sleep disorders and cyclic alternating pattern (CAP) sleep phases using 1-dimensional convolutional recurrent neural network (CRNN). The hierarcy has three stages, first stage classifies input signal into healthy and unhealthy. The next stage identifies sleep disorders from unhealthy input signals namely nsomnia, nfle, narcolepsy, rbd and plm. The third stage identifies CAP phase of input signal. Proposed models uses single-channel standardized electroencephalogram (EEG) recordings provided by the CAP sleep database. No manual feature extraction or pre/post processing is required making the approach completely autonomous. The healthy-unhealthy classification and disease classification have been studied using dataset of both phases (A & B), using dataset of only phase A, using dataset of only phase B seperately.

## Instructions
### Dataset preparation
* Follow instructions of our repository [CAP-Phase-Detection](https://github.com/Shrutii07/CAP-Phase-Detection) to create balanced CAP dataset for healthy as well as disordered subjects. You can download this data directly from [here](https://drive.google.com/drive/folders/1-DdLogc2Z7ck7KUrD6pmLUJdJ0QiPrqq?usp=sharing).
* Run the colab file [Dataset_preparation_disease_classification](https://github.com/Shrutii07/Sleep-disorder-Classification/blob/main/Dataset_preparation_disease_classification.ipynb). Give proper path of previously downloaded dataset and for folder in which dataset is to be strored.
* You can directly download dataset for healthy-unhealthy classification from [here](https://drive.google.com/drive/folders/1ai3kodudyjBxSH4zHm5dwUSmWSDUL2eB?usp=sharing) and dataset of disease classification from [here](https://drive.google.com/drive/folders/1tQHZx3aY3X9Us2UIJBVAjlLs15oIcgEF?usp=sharing)
### Model training
* Run the colab file [Healthy_Unhealthy_Classification.ipynb](https://github.com/Shrutii07/Sleep-disorder-Classification/blob/main/Healthy_Unhealthy_Classification.ipynb) for training model for first stage of hierarcy using dataset of both phases, phase A and phase B and observe result.
* You can observe results of our proposed models by downloadig our trained models, history and test datasets from [here](https://drive.google.com/drive/folders/1hYLAgwwlan1TR0Tfr66e19rsei0sgo44?usp=sharing). 
* Run the colab file [Disease_Classification.ipynb](https://github.com/Shrutii07/Sleep-disorder-Classification/blob/main/Disease_Classification.ipynb) for training model for second stage of hierarcy using dataset of both phases, phase A and phase B and observe result.
* You can observe results of our proposed models by downloadig our trained models and datasets from [here](https://drive.google.com/drive/folders/1tQHZx3aY3X9Us2UIJBVAjlLs15oIcgEF?usp=sharing).
* You can refer the colab file [Hyperparameter_optimization.ipynb](https://github.com/Shrutii07/Sleep-disorder-Classification/blob/main/Hyperparameter_optimization.ipynb) for optimizing the hyperparameters of models.
### GUI
* Download the folder [GUI](https://github.com/Shrutii07/Sleep-disorder-Classification/tree/main/GUI) to your local pc.
* Run the [run.py](https://github.com/Shrutii07/Sleep-disorder-Classification/blob/main/GUI/run.py) file using python interpreter.
* Open the generated link in any browser.
* Give the test samples provided in the folder [test](https://github.com/Shrutii07/Sleep-disorder-Classification/tree/main/GUI/test) or any C4A1 channel signal of 2s duration of 512Hz in csv format to see the result.
