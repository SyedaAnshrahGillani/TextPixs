<p align="center">
  <img src="./assets/logo.png" width="900" alt="TextPixs Logo Placeholder"/>
</p>

# 🎨✨ TextPixs: Enhancing Text Rendering in Text-to-Image Generation: A Novel Approach

### <div align="center"> Your Project Status/Affiliation (e.g., FYP 2025) <div>

<div align="center">
  <a href="https://github.com/SyedaAnshrahGillani/TextPixs"><img src="https://img.shields.io/static/v1?label=Project&message=Github&color=blue&logo=github"></a> &ensp;
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a> &ensp;
  <!-- Add more badges as needed, e.g., demo link, Hugging Face Space -->
</div>

<p align="center" border-radius="10px">
  <img src="./assets/teaser.png" width="90%" alt="TextPixs Teaser Image Placeholder"/>
</p>

## 🎥 Demo Video

[Watch the demo video on Google Drive](https://drive.google.com/file/d/1409aJytWW4xUxZkxs1JREmj1nK0RTI2E/view?usp=sharing)

## Abstract / Executive Summary

Text-to-image generation has revolutionized digital content creation, yet a critical challenge persists: accurately rendering text within generated images. This limitation significantly impacts applications ranging from educational tools and design automation to digital art. TextPixs introduces a groundbreaking framework designed to overcome this hurdle. By integrating cutting-edge techniques and innovative mathematical models, our approach dramatically enhances text fidelity and overall visual quality in generated images. This paper presents the methodology, experimental results, and the profound implications of TextPixs for the future of text-to-image synthesis.

## 🔥 Changelog

- **[2025-07-06] - Current Update**
    - Updated README with comprehensive details, including author sequence, demo video link, and refined project structure.
    - Renamed `image_generator` to `textpixs_image_generator` for clarity and branding.
    - Ensured `.env` files are ignored by Git and removed from repository history.
    - Re-added `gradio_demo` folder to ensure its presence on the remote branch.
- **[2025-07-03]**
    - README updated to professional standards, inspired by leading research projects.
    - FYP1 deliverables organized and integrated into the repository.
- **[2025-06-30]**
    - Initial project setup and repository creation.

## Table of Contents 📚

- [Abstract / Executive Summary](#abstract--executive-summary)
- [Changelog](#-changelog)
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Roadmap](#roadmap)
- [Performance](#performance)
- [Team](#team)
- [FYP1 Deliverables](#fyp1-deliverables)
- [Project Structure](#project-structure)
- [To-Do List](#to-do-list)
- [Contact](#contact)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Citation](#citation)

## 💡 Introduction

The field of text-to-image generation has witnessed exponential growth, with models like DALL-E and Imagen achieving unprecedented levels of image synthesis. Despite these advancements, the precise and legible rendering of textual content within complex visual scenes remains a significant bottleneck. This challenge stems from several factors:

- **Ambiguity in Text Prompts**: Current models often struggle to interpret nuanced textual instructions, leading to distorted or nonsensical text in the output.
- **Structural Integrity**: Maintaining the correct spatial arrangement and visual coherence of text within diverse image contexts is inherently difficult.
- **Lack of Text-Specific Loss Functions**: Traditional loss functions primarily focus on overall image quality, neglecting the critical aspect of textual fidelity.

TextPixs directly addresses these limitations by proposing a novel hybrid architecture. Our research focuses on:
- **Revolutionizing Text Rendering**: Developing state-of-the-art techniques to ensure accurate and high-quality text integration within generated images.
- **Achieving Unprecedented Fidelity**: Significantly improving both textual accuracy and the aesthetic quality of synthesized images.
- **Pioneering a Hybrid Architecture**: Introducing a unique framework that combines semantic alignment with a custom text rendering loss function.

TextPixs aims to bridge the gap between conceptual ideas and their visual realization, offering users an intuitive and powerful platform for generating, modifying, and refining images with perfect text. Our mission is to push the boundaries of text-to-image generation, with a steadfast commitment to enhancing text fidelity and advancing its applications across content creation, advertising, and human-computer interaction.

## Features 🚀

TextPixs is engineered with a suite of powerful features designed to push the boundaries of text-to-image generation:

- **Advanced Text-to-Image Generation**: At its core, TextPixs transforms textual descriptions into high-quality, visually stunning images. This is achieved through a novel hybrid architecture that integrates:
    - **Semantic Alignment Module**: This module employs sophisticated cross-modal transformers to meticulously align textual embeddings with visual features. The result is an unparalleled semantic coherence, ensuring that every generated image precisely reflects the nuances of the input text.
    - **Intelligent Text Rendering Loss**: We've developed a custom loss function that leverages OCR-based feedback loops. This innovative approach actively penalizes textual inaccuracies, guaranteeing that the text within the generated image is not only present but also perfectly legible and accurate to the input.
    - **Dual-Stage Refinement Pipeline**: Our two-step generation process allows for a coarse-to-fine approach to text rendering. This ensures that even the most intricate textual details are captured with exceptional clarity and precision.

- **Image Modifications (Phase 2 - Upcoming)**: Beyond initial generation, TextPixs will empower users to modify existing images using intuitive text prompts, unlocking new levels of customization and creative freedom.

- **Text-to-Video Capabilities (Future Phase - Visionary)**: Looking ahead, we envision TextPixs generating short, dynamic videos from descriptive prompts, further expanding the horizons of AI-driven content creation.

Our model is continuously enhanced with cutting-edge optimizations for superior performance and versatility:
- **Dynamic Learning Rate Adjustment**: Adapts the learning rate based on real-time validation performance, ensuring optimal model training and convergence.
- **Multilingual Training Support**: Extends TextPixs' capabilities to generate text in a multitude of languages and diverse scripts, fostering global accessibility and application.
- **Attention Map Visualization**: Provides invaluable insights into the model's decision-making process, illustrating precisely which parts of the image are most influenced by specific textual prompts.

## Technologies Used 🛡️

TextPixs leverages a robust stack of technologies to deliver its advanced capabilities:

- **Backend**: Primarily developed with Python, utilizing frameworks like Flask for API services (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary, potentially incorporating more scalable solutions).
- **Frontend**: Built with modern web technologies such as React.js, HTML, and CSS, ensuring a responsive and intuitive user interface (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary).
- **Database**: PostgreSQL is used for efficient data management and storage (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary).
- **AI/ML Models**: At the heart of TextPixs are fine-tuned Stable Diffusion Models and Generative Adversarial Networks (GANs), implemented using PyTorch for high-performance deep learning.
- **Datasets**: Training and evaluation are conducted using comprehensive datasets like COCO-Text, TextCaps, and a custom multilingual dataset, ensuring broad applicability and robust performance.

## 🚀 Getting Started

To set up and run the Gradio demo for TextPixs, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/SyedaAnshrahGillani/TextPixs.git
    cd TextPixs
    ```

2.  **Navigate to the Gradio demo directory**:
    ```bash
    cd gradio_demo/textpixs_image_generator
    ```

3.  **Create and activate a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Gradio application**:
    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:7860/` or a similar local address. You can access the demo through your web browser.

    *(Note: Ensure you have Python 3.8+ installed on your system.)*

## Roadmap 🗺️

Our project roadmap is structured into phases, with iterative progress on deliverables:

- **Initiation Phase (July - August 2024)**: Project setup and initial planning.
- **Literature Review (August - September 2024)**: Comprehensive review of existing research.
- **Gap Analysis (September - November 2024)**: Identification of research gaps and unique contributions.
- **Research Design and Planning (November 2024 - January 2025)**: Detailed design of the hybrid architecture and experimental setup.
- **Data Collection (January - April 2025)**: Gathering and preparing datasets for model training.
- **Data Analysis and Interpretation (March - May 2025)**: Analyzing experimental results and drawing conclusions.
- **Drafting Research Paper (November 2024 - May 2025)**: Writing the final research paper.
- **Final Review & Submission on Selected Journal (May - June 2025)**: Preparing for submission to a journal like CVPR.
- **Documentations & FYP Report (June - July 2025)**: Finalizing all project documentation and the FYP report.

## Performance 📊

Our proposed method demonstrates significant improvements over existing models in text-to-image generation, particularly in text fidelity and visual quality. The following table summarizes the performance comparison based on FID (Fréchet Inception Distance), BLEU, and OCR Accuracy.

| Model | FID (↓) | BLEU (↑) | OCR Accuracy (↑) |
|---|---|---|---|
| DALL-E | 12.34 | 0.72 | 65% |
| Imagen | 10.56 | 0.81 | 72% |
| **Proposed** | **9.12** | **0.89** | **85%** |

## Team 👥

**Authors**:
Syeda Anshrah Gillani<sup>1*</sup>, Mirza Samad Ahmed Baig<sup>3</sup>, Osama Ahmed Khan<sup>1</sup>, Shahid Munir Shah<sup>1</sup>, Umeema Mujeeb<sup>1</sup>, Maheen Ali<sup>1</sup>

## FYP1 Deliverables 📦

The following key deliverables from FYP1 are available in the `docs/fyp1` directory:

- **FYP 1 Details**: `FYP 1 Details - TextPixs.pdf`
- **Gap Analysis**: `Gap Analysis - Text Pixs.pdf`
- **Project Plan (Gantt Chart)**: `Project Plan - Text Pixs - GANTT CHART ~ FYP ~ Anshrah.pdf`
- **Report - Latex - 3 Chapters**: `Report - Latex - 3 Chapters - TextPixs .pdf`
- **Research Paper Draft - Latex**: `Research Paper Draft - Latex - Text Pixs.pdf`
- **Selection of Publication Venue**: `Selection of Publication Venue - TextPixs - Latex.pdf`
- **Sign Off Sheet**: `Sign Off Sheet - Text Pixs.pdf`
- **FYP1 Presentation**: `TextPixs FYP1.pdf`
- **Standee Design**: `Textpixs-STANDEE-3.pdf`

## Project Structure 📁

The repository is organized as follows:

```
TextPixs/
├── assets/                 # Images for README and documentation
├── Demo recording/         # Demo videos
├── docs/                   # Project documentation and deliverables
│   ├── fyp1/               # Contains all deliverables from FYP1
│   └── proposal/           # Contains project proposal documents
├── gradio_demo/            # Gradio demo application
│   └── textpixs_image_generator/ # TextPixs image generator demo
├── .github/                # GitHub Actions workflows and configurations
├── LICENSE                 # Project license
└── README.md               # This README file
```

## 💪 To-Do List

We are actively working on and planning the following:

- [ ] Refine and optimize the Semantic Alignment Module.
- [ ] Further develop and evaluate the Text Rendering Loss function.
- [ ] Enhance the Dual-Stage Refinement pipeline for improved image quality.
- [ ] Conduct more extensive experiments with dynamic learning rate adjustment.
- [ ] Expand multilingual training support to additional languages.
- [ ] Develop advanced Attention Map Visualization techniques.
- [ ] Explore new datasets for training and evaluation.
- [ ] Prepare the final research paper for submission to a top-tier conference (e.g., CVPR).
- [ ] Implement and integrate the image modification feature (Phase 2).
- [ ] Explore and develop text-to-video capabilities (Future Phase).
- [ ] Prepare comprehensive documentation and the final FYP report.

## Contact 📧

For any inquiries or collaborations, please contact:

- **Syeda Anshrah Gillani (Group Leader)**: syedaanshrah16@gmail.com

## Contributing 🤝

We welcome contributions! If you’re interested in improving TextPixs, please fork the repository, create a new branch, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a pull request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## 🤗 Acknowledgements

We extend our gratitude to the following:

- Our supervisors, Sir Osama Ahmed Khan and Mirza Samad Ahmed Baig, for their invaluable guidance and support.
- Mirza Samad Ahmed Baig for his sponsorship and continued commitment to the project.
- All researchers and open-source contributors whose work has inspired and facilitated this project.

## 📖 Citation

If you find this research project helpful, please consider citing our work (details to be provided upon paper submission).

```bibtex
@article{gillani2025enhancing,
  title={Enhancing Text Rendering in Text-to-Image Generation: A Novel Approach},
  author={Gillani, Syeda Anshrah and Mujeeb, Umema and Ali, Maheen and Baig, Mirza Samad Ahmed},
  journal={DRAFT SUBMITTED ON 17 JANUARY 2025 TO FYP COMMITTEE FOR FYP1 EVALUATION PURPOSES},
  year={2025}
}
```
