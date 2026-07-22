# Model Optimization Report

## Benchmark Results

| Model | Size (MB) | Mean Latency (ms) | Std Dev (ms) | FPS |
|--------|-----------|-------------------|--------------|-----|
| PyTorch (.pt) | 5.96 | 114.27 | N/A | 8.75 |
| Dynamic Quantized (.pt) | 11.64 | N/A | N/A | N/A |
| ONNX | 11.70 | 62.52 | 18.87 | 16.00 |

## Accuracy

The ONNX model was exported directly from the trained PyTorch model. Inference outputs matched the original model during testing, indicating that the export preserved detection performance.

## Observations

- ONNX Runtime significantly improved inference speed on CPU.
- The average latency decreased from **114.27 ms** to **62.52 ms**.
- FPS increased from **8.75** to **16.00**, making ONNX more suitable for real-time inference.
- Dynamic quantization did not reduce the model size because YOLOv8 is primarily composed of convolutional layers. PyTorch dynamic quantization mainly benefits models with Linear layers, so it was not an effective optimization technique for this architecture.

## Conclusion

For this project, exporting the trained YOLOv8 model to ONNX provided the most practical optimization. The ONNX model achieved substantially faster CPU inference while maintaining comparable detection performance. Dynamic quantization was explored as part of the optimization workflow, but it offered little benefit for this convolution-based object detection model.