import tritonclient.http as httpclient
import numpy as np

# Load preprocessed inputs
image_data = np.load("image_input.npy")
text_data = np.load("text_input.npy")

# Triton client
client = httpclient.InferenceServerClient(url="localhost:8000")
image_input = httpclient.InferInput("image", image_data.shape, "FP32")
image_input.set_data_from_numpy(image_data)
text_input = httpclient.InferInput("text", text_data.shape, "INT32")
text_input.set_data_from_numpy(text_data)

result = client.infer(model_name="clip", inputs=[image_input, text_input])
embeddings = result.as_numpy("embeddings")
print("Embeddings shape:", embeddings.shape)  # Should be (1, 512)