# 🧠 Handwritten Digit Recognition Using CNN (MNIST)

This project is a deep learning-based solution to recognize handwritten digits using the **MNIST dataset** and a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras**.

![Model Architecture](model.jpg)

## 📌 Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation & Run](#installation--run)
- [Results](#results)
- [Improvements & Future Work](#improvements--future-work)
- [License](#license)

---

## ✅ Overview

The goal of this project is to classify grayscale 28x28 pixel images of handwritten digits (0 through 9) using a CNN. The model achieves over **99% accuracy** on the test set and serves as a strong baseline for image classification problems.

---

## 💻 Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- MNIST Dataset

---

## 📁 Project Structure

```
├── model.jpg               # CNN architecture plot
├── download.png            # Sample prediction output
├── digit_recognition.ipynb # Main notebook with code
├── README.md               # Project documentation
```

---

## ⚙️ How It Works

1. **Load Data**: Load the MNIST dataset.
2. **Preprocessing**: Normalize pixel values and reshape the input for the CNN.
3. **Build CNN Model**:
   - Conv2D + MaxPooling
   - Conv2D + MaxPooling
   - Flatten + Dropout
   - Dense (Softmax)
4. **Compile & Train**:
   - Optimizer: Adam
   - Loss Function: Sparse Categorical Crossentropy
   - Metrics: Accuracy
5. **Evaluate & Predict**: Test the model on unseen data.

---

## 🚀 Installation & Run

1. Clone this repo:
```bash
git clone https://github.com/Hemasai1/digit-recognition-cnn.git
cd digit-recognition-cnn
```

2. Install requirements:
```bash
pip install tensorflow numpy matplotlib
```

3. Run the notebook or script:
```bash
jupyter notebook digit_recognition.ipynb
```

---

## 📊 Results

- **Test Accuracy**: ~99.0%
- **Training Time**: ~7 minutes on CPU (varies by system)

Example Predictions:
![Prediction Samples](download.png)

---

## 🔧 Improvements & Future Work

- 🔄 Use real-world handwritten data (e.g., EMNIST)
- ✍️ Add live drawing input using OpenCV or Tkinter
- 📱 Deploy as a web/mobile app
- ☁️ Build a REST API using Flask or FastAPI
- 🎯 Integrate multi-digit sequence recognition

---

## 📄 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

**Your Name**  
Final Year CSE (AI & ML) Student  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)