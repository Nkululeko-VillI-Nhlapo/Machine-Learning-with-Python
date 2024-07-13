# Cat and Dog Image Classifier
### Nhlapo Nkululeko
## Introduction
Welcome to the Cat and Dog Image Classifier project! This project aims to build a convolutional neural network (CNN) to classify images of cats and dogs with high accuracy.

## Problem Statement
Image classification of cats and dogs is a fundamental problem in computer vision that involves automatically identifying whether an image contains a cat or a dog.

## Dataset
The dataset is sourced from [FreeCodeCamp](https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip). It contains 25,000 labeled images of cats and dogs, split into training, validation, and test sets. Each image is resized to 150x150 pixels and normalized to the range [0, 1].

## Methodology

### Data Preprocessing
- Images were resized to 150x150 pixels, normalized, and augmented with techniques such as horizontal and vertical flipping, rotation, and zooming.

### Model Architecture
- The CNN model consists of three convolutional layers followed by max pooling layers, a flatten layer, and two dense layers. ReLU activation is used for hidden layers, and softmax activation is used for the output layer.

### Training
- The model was trained using the Adam optimizer with a learning rate of 0.001, binary cross-entropy loss, and a batch size of 128 for 20 epochs.

### Evaluation
- The model was evaluated using accuracy and loss on the validation set. A confusion matrix, precision, recall, and F1-score were also calculated to assess performance.

## Results
The model achieved a training accuracy of **78%** and a validation accuracy of **74%**. Plots of training and validation accuracy and loss over epochs were generated, and sample predictions were visualized with images and their predicted labels.

## Conclusion
The CNN model effectively classifies images of cats and dogs, achieving a validation accuracy of **74%**. Data augmentation and careful tuning of hyperparameters were crucial for improving performance. Future work could involve using more advanced architectures like ResNet or Inception, or fine-tuning pre-trained models on the dataset to further improve accuracy.

## Installation and Usage

### Prerequisites
- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib
- wget (for downloading the dataset)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cat-and-dog-image-classifier.git
    ```
2. Navigate to the project directory:
    ```bash
    cd cat-and-dog-image-classifier
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Download and unzip the dataset:
    ```bash
    !wget https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip
    !unzip cats_and_dogs.zip
    ```
2. Run the Jupyter Notebook:
   On googlecolab



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- FreeCodeCamp for providing the dataset.
- TensorFlow and Keras for their excellent deep learning frameworks.
- Everyone who has contributed to open-source libraries and tools.

## Contact
For any inquiries or feedback, please contact 079 736 7550.
Email: nongimbhilinkululeko.19@gmail.com


