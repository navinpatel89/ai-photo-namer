from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration


# Load the pretrained BLIP processor and model
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


# Load image
img_path = "test.jpeg"

image = Image.open(img_path).convert("RGB")


# Prepare image for BLIP
inputs = processor(
    images=image,
    return_tensors="pt"
)


# Generate caption
outputs = model.generate(
    **inputs,
    max_length=50
)


# Convert generated tokens into text
caption = processor.decode(
    outputs[0],
    skip_special_tokens=True
)


# Display result
print("Image Caption:")
print(caption)