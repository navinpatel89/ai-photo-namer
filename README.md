# AI Image Captioning App

An AI-powered image captioning web application built with **Python, Hugging Face Transformers, BLIP, PyTorch, PIL, NumPy, and Gradio**.

The application allows users to upload an image through a simple web interface and automatically generates a natural-language description of the image using the pretrained **Salesforce BLIP image-captioning model**.

## 🚀 Project Overview

This project demonstrates how to integrate a pretrained Vision-Language Model (VLM) into a Python application and expose it through an interactive Gradio web interface.

### Workflow

```text
User uploads image
        ↓
     Gradio
        ↓
   Image input
        ↓
    PIL / NumPy
        ↓
 BLIP Processor
        ↓
   BLIP Model
        ↓
Generated caption
        ↓
   Gradio output
```

## ✨ Features

* Upload an image through a web interface
* Automatically analyze the uploaded image
* Generate an AI-powered image caption
* Uses a pretrained BLIP Vision-Language Model
* Simple and intuitive Gradio interface
* Runs locally on your computer
* No model training required
* Demonstrates practical Hugging Face Transformers usage

## 🛠️ Technologies Used

* **Python**
* **PyTorch**
* **Hugging Face Transformers**
* **BLIP**
* **Gradio**
* **Pillow (PIL)**
* **NumPy**

### AI Model

This project uses:

```text
Salesforce/blip-image-captioning-base
```

BLIP stands for **Bootstrapping Language-Image Pre-training** and is designed for vision-language tasks such as image captioning.

## 📁 Project Structure

```text
ai-photo-namer/
│
├── my_env/
│
├── image_cap.py
├── hello.py
├── image_captioning_app.py
├── app.py
├── requirements.txt
├── README.md
│
└── .gitignore
```

### Main Files

| File                      | Description                                |
| ------------------------- | ------------------------------------------ |
| `image_cap.py`            | Basic BLIP image-captioning implementation |
| `hello.py`                | Simple Gradio demonstration                |
| `app.py`                  | Gradio-based BLIP application              |
| `image_captioning_app.py` | Final image-captioning exercise            |
| `requirements.txt`        | Python dependencies                        |
| `README.md`               | Project documentation                      |
| `.gitignore`              | Files excluded from Git                    |

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/navinpatel89/ai-photo-namer.git
```

Navigate into the project:

```bash
cd ai-photo-namer
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv my_env
```

Activate it:

```powershell
.\my_env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install the main packages:

```bash
pip install gradio transformers Pillow numpy torch
```

## ▶️ Run the Application

Run:

```bash
python image_captioning_app.py
```

The terminal should display a local URL similar to:

```text
http://127.0.0.1:7860
```

Open the URL in your web browser.

## 🖼️ Using the Application

1. Start the application.
2. Open the Gradio URL in your browser.
3. Upload an image.
4. Submit the image.
5. The BLIP model analyzes the image.
6. The application generates a descriptive caption.
7. The caption is displayed in the Gradio interface.

### Example

**Input:**

```text
A photograph containing a person standing next to a car.
```

**Possible AI-generated output:**

```text
a man standing next to a car
```

The generated caption will vary depending on the image.

## 🧠 How It Works

### 1. Load the BLIP Processor

```python
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
```

The processor prepares the image for the BLIP model.

### 2. Load the BLIP Model

```python
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
```

This loads the pretrained image-captioning model.

### 3. Process the Image

```python
inputs = processor(
    raw_image,
    return_tensors="pt"
)
```

The image is converted into the tensor representation required by the PyTorch model.

### 4. Generate the Caption

```python
out = model.generate(
    **inputs,
    max_length=50
)
```

BLIP generates a sequence of tokens describing the image.

### 5. Decode the Result

```python
caption = processor.decode(
    out[0],
    skip_special_tokens=True
)
```

The generated tokens are converted into human-readable text.

### 6. Display Through Gradio

```python
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)
```

Gradio provides the interactive web interface around the Python function.

## 📦 Generate Requirements File

After installing the dependencies, you can create the requirements file with:

```bash
pip freeze > requirements.txt
```

Then another developer can recreate the environment using:

```bash
pip install -r requirements.txt
```

## 🔒 Git and Environment

The Python virtual environment should not be committed to Git.

Example `.gitignore`:

```gitignore
my_env/
venv/
.venv/
__pycache__/
*.pyc
.env
models/
```

## 📚 Learning Objectives

This project demonstrates practical experience with:

* Python development
* Virtual environments
* Hugging Face Transformers
* Pretrained AI models
* Vision-Language Models
* BLIP image captioning
* PyTorch inference
* Image preprocessing
* NumPy
* PIL/Pillow
* Gradio application development
* Building an AI model into a web application
* Git and GitHub project management

## 🔮 Future Improvements

The application can be extended with additional AI functionality.

Potential improvements include:

* Generate more detailed image descriptions
* Generate keywords and tags
* Automatically create meaningful image filenames
* Allow users to edit generated captions
* Process multiple images
* Add image classification
* Add visual question answering
* Add multilingual captions
* Add downloadable results
* Store caption history
* Deploy the application to Hugging Face Spaces
* Add a REST API using FastAPI
* Add authentication
* Containerize the application using Docker

## 🎯 Portfolio Value

This project demonstrates how a pretrained AI model can be integrated into a practical application rather than being used only from a Python script.

It combines:

```text
Python
   +
Hugging Face Transformers
   +
Vision-Language AI
   +
PyTorch
   +
Gradio
   +
Web Application
```

This makes it a useful foundational project for exploring **AI Engineering, Generative AI, Computer Vision, and LLM/VLM application development**.

## 👨‍💻 Author

**Navin Patel**

GitHub:

```text
https://github.com/navinpatel89
```

## 📄 License

This project is intended for learning, experimentation, and portfolio development.
