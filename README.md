<p align="center">
  <img src="./assets/logo.png" width="900" alt="TextPixs Logo Placeholder"/>
</p>

# TextPixs: Glyph-Conditioned Diffusion with Character-Aware Attention and OCR-in-the-Loop Feedback for Accurate Text Rendering

**CVPR 2025**

<div align="center">
  <a href="https://github.com/SyedaAnshrahGillani/TextPixs"><img src="https://img.shields.io/static/v1?label=Project&message=Github&color=blue&logo=github"></a> &ensp;
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a> &ensp;
</div>

<p align="center">
  <img src="./assets/teaser.png" width="90%" alt="TextPixs Teaser Image"/>
</p>

## 💡 Introduction

We introduce TextPixs, a novel framework for generating images with accurate and legible text. While existing text-to-image models excel at creating stunning visuals, they struggle with rendering text, limiting their use in many applications. TextPixs addresses this by integrating a **Glyph-Conditioned Diffusion with Character-Aware Attention (GCDA)** model, which combines a deep understanding of both semantics and character-level details.

<p align="center">
  <img src="./assets/results.png" width="90%" alt="TextPixs Results Image"/>
</p>

## 🔥 Key Innovations

- **Dual-Stream Text Encoder**: Simultaneously processes the meaning of the text and the visual appearance of its characters.
- **Character-Aware Attention**: Ensures that individual letters are rendered distinctly and without distortion.
- **OCR-in-the-Loop Feedback**: A built-in OCR system reviews and refines the generated text for accuracy.

<p align="center">
  <img src="./assets/Single Stream vs Dual Stream.png" width="90%" alt="Single Stream vs Dual Stream"/>
</p>

<p align="center">
  <img src="./assets/Without and with segregation loss.png" width="90%" alt="Segregation Loss"/>
</p>

<p align="center">
  <img src="./assets/Attention Problem - why characters merge.png" width="90%" alt="Attention Problem"/>
</p>

## 📊 Performance

TextPixs significantly outperforms existing models in text rendering accuracy while maintaining high image quality.

<p align="center">
  <img src="./assets/GCDA Performance Breakthrough - Figure 9 from research paper.png" width="90%" alt="Performance Breakthrough"/>
</p>

| Model | FID (↓) | CER (↓) | WER (↓) | Exact Match (%) (↑) |
|---|---|---|---|---|
| DALL-E 2 | 13.9 | 0.45 | 0.58 | 18.5 |
| Stable Diffusion 1.5 | 15.2 | 0.65 | 0.82 | 5.2 |
| TextDiffuser-2 | 14.1 | 0.14 | 0.25 | 60.1 |
| **TextPixs (Ours)** | **14.3** | **0.08** | **0.15** | **75.4** |

## 🚀 Real-World Applications

TextPixs opens up new possibilities for AI-generated content in various fields.

<p align="center">
  <img src="./assets/GCDA's Real world applications.png" width="90%" alt="Real-World Applications"/>
</p>

## 🔮 Future Directions

We are exploring several exciting avenues for future research.

<p align="center">
  <img src="./assets/Future Research Directions Enabled by GCDA.png" width="90%" alt="Future Research"/>
</p>

## ⚙️ Technical Deep Dive

Our two-stage training process is key to TextPixs' success.

<p align="center">
  <img src="./assets/Stage 1 - Foundational Training.png" width="90%" alt="Stage 1 Training"/>
</p>

<p align="center">
  <img src="./assets/OCR in the loop Fine tuning Framework.png" width="90%" alt="OCR in the loop"/>
</p>

## 🏁 Getting Started

To run the Gradio demo:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/SyedaAnshrahGillani/TextPixs.git
    cd TextPixs
    ```
2.  **Navigate to the app directory**:
    ```bash
    cd app
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the app**:
    ```bash
    python app_textpixs.py
    ```

## 📖 Citation

```bibtex
@article{gillani2025textpixs,
  title={TextPixs: Glyph-Conditioned Diffusion with Character-Aware Attention and OCR-in-the-Loop Feedback for Accurate Text Rendering},
  author={Gillani, Syeda Anshrah and Baig, Mirza Samad Ahmed and Khan, Osama Ahmed and Shah, Shahid Munir and Mujeeb, Umema and Ali, Maheen},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2025}
}
```
