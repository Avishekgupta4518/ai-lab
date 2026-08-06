# 🧠 Lab 6: Image Classification using CNN

A complete implementation of **multi-class image classification** using **PyTorch**, featuring both a **Custom Convolutional Neural Network (CNN)** and **Transfer Learning with EfficientNet-B0**. The project also includes a **Streamlit-based web application** for real-time image classification using the trained models.

---

## 📖 Overview

This lab demonstrates the complete workflow of building an image classification system:

- Building a CNN from scratch using PyTorch
- Training and evaluating a custom neural network
- Applying transfer learning with EfficientNet-B0
- Comparing model performance
- Saving trained models
- Deploying the classifier using Streamlit

The project uses the **Imagenette** dataset, a simplified subset of ImageNet containing 10 image classes.

---

## ✨ Features

- Custom CNN implementation from scratch
- Transfer Learning with EfficientNet-B0
- Modular training pipeline
- Training & validation accuracy/loss visualization
- GPU support (CUDA)
- Model checkpoint saving/loading
- Interactive Streamlit GUI
- Real-time image prediction
- Confidence score visualization

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Torchvision
- TorchInfo
- Timm
- Streamlit
- Matplotlib
- NumPy

---

## 📂 Project Structure

```text
Lab6/
│
├── GUII.py                              # Initial GUI implementation
├── updated_GUI.py                       # Streamlit deployment application
├── best_model.pth
├── best_model_efficientnet.pth                      
├── helper_functions.py                  # Utility functions for plotting
├── model.py                             # Custom CNN architecture
├── trainNN.py                           # Training & validation functions
├── ImageClassificationusingCNN.ipynb    # Custom CNN notebook
├── TransferLearning.ipynb               # Transfer Learning notebook
├── Lab6AI.pdf                           # Lab instructions
│
├── data/
│   ├── train/
│   └── val/
│
└── README.md
```

---

# 📁 Dataset

The project uses the **Imagenette** dataset.

Directory structure:

```text
data/
│
├── train/
│   ├── class_1/
│   ├── class_2/
│   └── ...
│
└── val/
    ├── class_1/
    ├── class_2/
    └── ...
```

---

# 🧩 Part A — Custom CNN

The custom CNN is implemented in:

```text
model.py
```

The architecture consists of:

- Convolution Layers
- ReLU Activation
- Max Pooling
- Fully Connected Layers
- Softmax Classification

### Training Steps

- Import required libraries
- Load dataset
- Apply image transforms
- Create DataLoaders
- Build CustomCNN model
- Print model summary
- Define loss function
- Define optimizer
- Train model
- Validate model
- Save trained weights
- Plot training curves

---

## Training

Run the notebook:

```text
ImageClassificationusingCNN.ipynb
```

Training configuration:

| Parameter | Value |
|-----------|-------|
| Epochs | 30 |
| Batch Size | 32 |
| Optimizer | Adam |
| Loss | CrossEntropyLoss |

---

# 🚀 Part B — Transfer Learning

Transfer learning uses the pretrained:

**EfficientNet-B0**

from the **timm** library.

Notebook:

```text
TransferLearning.ipynb
```

Training pipeline:

- Load pretrained EfficientNet-B0
- Replace classifier layer
- Freeze feature extractor (optional)
- Train classifier
- Fine-tune model
- Save trained weights

Training configuration:

| Parameter | Value |
|-----------|-------|
| Epochs | 5 |
| Batch Size | 32 |
| Optimizer | Adam |
| Loss | CrossEntropyLoss |

---

# 🖥️ Streamlit Deployment

Launch the GUI:

```bash
streamlit run updated_GUI.py
```

The application allows users to:

- Upload an image
- Select the trained model
- Predict image class
- Display confidence score
- Perform real-time inference

---

# 📌 Experiments Performed

- Custom CNN Training
- EfficientNet-B0 Fine-tuning
- Loss & Accuracy Visualization
- Adam Optimizer
- SGD Optimizer Comparison
- Batch Size Comparison (16, 32, 64)
- Data Augmentation
- Model Saving & Loading
- Real-time Image Classification
- Misclassification Analysis

---

# 📈 Expected Results

### Custom CNN

- Successfully learns image features
- Good baseline performance
- Demonstrates CNN architecture design

### EfficientNet-B0

- Faster convergence
- Higher validation accuracy
- Better feature extraction
- Improved generalization

---

# 📊 Performance Comparison

| Model | Epochs | Accuracy | Speed |
|--------|---------|----------|-------|
| Custom CNN | 30 | Good | Moderate |
| EfficientNet-B0 | 5 | Higher | Faster |

---

# 📷 GUI Features

The Streamlit application includes:

- Image Upload
- Model Selection
- Image Preview
- Predicted Class
- Confidence Score
- User-friendly Interface

---

# 📚 Learning Outcomes

After completing this lab, students will understand:

- CNN architecture
- Image preprocessing
- PyTorch training pipeline
- Transfer Learning
- EfficientNet
- Model evaluation
- Streamlit deployment
- Deep Learning workflow

---

# 📚 Dataset

**Imagenette Dataset**

---
