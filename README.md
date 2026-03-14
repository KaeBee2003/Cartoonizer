<p align="center">
  <img width="625" height="213" alt="Cartoonizer Graphics" src="https://github.com/user-attachments/assets/57691de2-a858-4594-a7dc-72d6ffb552b2">
</p>

## Before & After

<p align="center">
  <img src="https://github.com/user-attachments/assets/2ea53bdb-792f-4d18-a5f9-caa6928f0ee3" width="400" />
  <img src="https://github.com/user-attachments/assets/57aca414-6429-4032-8b23-f56e9ab008d4" width="400" />
</p>

---

## How It Works

The application performs colour quantisation using the following steps:

1. The image is reshaped into a 2D array of pixel values.
2. User inputs K value, K-Means clustering groups similar colours.
3. Each pixel is replaced with its cluster centroid (the average color of the cluster).
4. The reduced colour palette produces a cartoon-style effect.

This reduces colour complexity while preserving major visual structures.

---

## 🛠️ Tech Stack

- Python
- OpenCV
- NumPy
- Tkinter
- K-Means Clustering

---

# For Windows Executable
<p align="Left">
  <a href="https://github.com/KaeBee2003/Cartoonizer/releases/download/v1.0.0/Cartoonizer.exe">
    <img src="https://img.shields.io/badge/Download-Cartoonizer%20v1.0.0-blue?style=for-the-badge&logo=windows" />
  </a>
</p>
