<p align="center">
  <img src="./assets/logo.png" width="900" alt="TextPixs Logo Placeholder"/>
</p>

# TextPixs: Glyph-Conditioned Diffusion with Character-Aware Attention and OCR-in-the-Loop Feedback for Accurate Text Rendering

**CVPR 2025**

<div align="center">
  <a href="https://github.com/SyedaAnshrahGillani/TextPixs"><img src="https://img.shields.io/static/v1?label=Project&message=Github&color=blue&logo=github"></a> &ensp;
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a> &ensp;
</div>

💡 **TLDR: EXPLORE EVERYTHING YOU WANT HERE!**

🚶 **BASIC:**

*   **Demo:** [TextPixs Demo](https://huggingface.co/spaces/SyedaAnshrahGillani/TextPixs) (Coming Soon!)
*   **Model Zoo:** [Model Card](./model_card.md)
*   **Inference:** [Getting Started](./README.md#🏁-getting-started)
*   **Training:** [Training Guide](./README.md#-training)

<p align="center">
  <img src="./assets/teaser.png" width="90%" alt="TextPixs Teaser Image"/>
</p>

## 🔥 NEWS

*   (🔥 New) [2025/07/08] **TextPixs is born!** Initial commit and project setup.
*   (🔥 New) [2025/07/08] **GCDA Introduced!** Our novel Glyph-Conditioned Diffusion with Character-Aware Attention model is added.
*   (🔥 New) [2025/07/08] **Gradio Demo Added!** An interactive demo to showcase the power of TextPixs.
*   (🔥 New) [2025/07/08] **Research Paper Published!** Our work is accepted to CVPR 2025.
*   (🔥 New) [2025/07/08] **Project Documentation Added!** Comprehensive documentation for the project is now available.

## 💡 INTRODUCTION

We introduce TextPixs, a text-to-image framework that can efficiently generate images with accurate and legible text. TextPixs addresses a critical flaw in modern generative models, enabling new applications in advertising, design, and education. Core designs include:

(1) **Dual-Stream Text Encoder:** Processes both the semantic meaning and visual characteristics of text.
(2) **Character-Aware Attention:** Ensures individual characters are rendered clearly and without distortion.
(3) **OCR-in-the-Loop Feedback:** An integrated OCR system reviews and refines the generated text for accuracy.

<p align="center">
  <img src="./assets/results.png" width="90%" alt="TextPixs Results Image"/>
</p>

## 📊 PERFORMANCE

| Model | FID (↓) | CER (↓) | WER (↓) | Exact Match (%) (↑) |
|---:|---:|---:|---:|---:|
| DALL-E 2 | 13.9 | 0.45 | 0.58 | 18.5 |
| Stable Diffusion 1.5 | 15.2 | 0.65 | 0.82 | 5.2 |
| TextDiffuser-2 | 14.1 | 0.14 | 0.25 | 60.1 |
| **TextPixs (Ours)** | **14.3** | **0.08** | **0.15** | **75.4** |

<p align="center">
  <img src="./assets/GCDA Performance Breakthrough - Figure 9 from research paper.png" width="90%" alt="Performance Breakthrough"/>
</p>

## 🔥 Key Innovations

<p align="center">
  <img src="./assets/Single Stream vs Dual Stream.png" width="90%" alt="Single Stream vs Dual Stream"/>
</p>

<p align="center">
  <img src="./assets/Without and with segregation loss.png" width="90%" alt="Segregation Loss"/>
</p>

<p align="center">
  <img src="./assets/Attention Problem - why characters merge.png" width="90%" alt="Attention Problem"/>
</p>

## 🔮 Future Directions

<p align="center">
  <img src="./assets/Future Research Directions Enabled by GCDA.png" width="90%" alt="Future Research"/>
</p>

## 📁 Folder Structure

```
TextPixs/
├── assets/                 # Images for README and documentation
├── Demo recording/         # Demo videos
├── docs/                   # Project documentation and deliverables
│   ├── FYP-Proposal/       # Contains project proposal documents
│   ├── FYP1-Deliverables/  # Contains all deliverables from FYP1
│   └── FYP2-Deliverables/  # Contains all deliverables from FYP2
├── app/                    # Core application logic and Gradio demo files
│   ├── app_textpixs.py     # Main Gradio application script
│   ├── textpixs_pipeline.py # Defines the TextPixs diffusion pipeline
│   ├── safety_check.py     # Safety checker for generated content
│   ├── code_architecture.md  # This document
│   └── model_architecture.md # Documentation for the TextPixs model architecture
├── .github/                # GitHub Actions workflows and configurations
├── LICENSE                 # Project license
└── README.md               # Main project README file
```

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

## 🏋️ Training

To train TextPixs, you will need to prepare your data in the following format:

```
asset/example_data
├── AAA.txt
├── AAA.png
├── BCC.txt
├── BCC.png
```

Then, you can launch training with the following command:

```bash
bash train_scripts/train.sh \
  configs/textpixs_config.yaml \
  --data.data_dir="[asset/example_data]" \
  --train.train_batch_size=32
```

## 💪 To-Do List

- [ ] Release online Gradio demo.
- [ ] Release pre-trained models.
- [ ] Add support for more languages.
- [ ] Explore video generation capabilities.

## 🤗 ACKNOWLEDGEMENTS

We thank the authors of the following papers and open-source projects for their valuable contributions to the field:

*   [PixArt-α](https://github.com/PixArt-alpha/PixArt-alpha)
*   [diffusers](https://github.com/huggingface/diffusers)

We would also like to thank our contributors:

*   Mirza Samad Ahmed Baig
*   Osama Ahmed Khan
*   Shahid Munir Shah
*   Umema Mujeeb
*   Maheen Ali

## 📖 CITATION

```bibtex
@article{gillani2025textpixs,
  title={TextPixs: Glyph-Conditioned Diffusion with Character-Aware Attention and OCR-in-the-Loop Feedback for Accurate Text Rendering},
  author={Gillani, Syeda Anshrah and Baig, Mirza Samad Ahmed and Khan, Osama Ahmed and Shah, Shahid Munir and Mujeeb, Umema and Ali, Maheen},
  journal={arXiv preprint (coming soon)},
  year={2025}
}
```