<p align="center">
  <img src="./assets/logo.png" width="250" alt="TextPixs Logo Placeholder"/>
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

## Abstract / Executive Summary

Text-to-image generation has made significant strides with advancements in deep learning, particularly with GANs and transformers. However, accurate text rendering within generated images remains a challenge, impeding applications such as educational tools, design automation, and digital art. This paper introduces a novel framework for enhancing text rendering in images, integrating state-of-the-art techniques and innovative mathematical models. Extensive experiments demonstrate that the proposed approach significantly improves text fidelity and visual quality.

## 🔥🔥 News

- (🔥 New) [2025/07/03] README updated to professional standards, inspired by leading research projects.
- (🔥 New) [2025/07/03] FYP1 deliverables organized and integrated into the repository.
- [2025/06/30] Initial project setup and repository creation.

## Table of Contents 📚

- [Abstract / Executive Summary](#abstract--executive-summary)
- [News](#-news)
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
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

Text-to-image generation has gained widespread attention in fields such as content creation, advertising, and human-computer interaction. Recent models like DALL-E and Imagen have achieved remarkable image synthesis capabilities. However, the accurate rendering of textual content remains a bottleneck due to:

- Ambiguity in text prompts.
- Challenges in maintaining textual structure within complex visual scenes.
- Lack of robust loss functions focused on textual fidelity.

To address these challenges, this research proposes a novel hybrid architecture incorporating semantic alignment, multimodal embeddings, and a custom loss function. Our primary objectives include:
- Enhancing the rendering of images via text-to-image generation using state-of-the-art techniques.
- Improving text fidelity and visual quality in generated images.
- Developing a novel hybrid architecture with semantic alignment and text rendering loss.

TextPixs intends to bridge the gap between ideas and visuals, providing users with a creative playground for generating, modifying, and refining images. Our purpose is to research and contribute breakthroughs in achieving excellence in text-to-image generation, with a focus on text fidelity improvements to advance applications in content creation, advertising, and human-computer interactions.

## Features 🚀

- **Text-to-Image Generation**: Input a description, and TextPixs will create a high-quality image that matches your vision. This feature leverages a novel hybrid architecture incorporating:
    - **Semantic Alignment Module**: Aligns textual embeddings with visual features using cross-modal transformers, ensuring semantic coherence between text and image.
    - **Text Rendering Loss**: A custom loss function penalizes textual inaccuracies by incorporating OCR-based feedback loops, ensuring generated text matches the input.
    - **Dual-Stage Refinement**: A two-step generation pipeline for coarse-to-fine text rendering, enhancing fine-grained details.
- **Image Modifications** (Phase 2): Modify existing images using text prompts for further customization and creativity.
- **Text-to-Video Capabilities** (Future Phase): Generate short videos from descriptive prompts.

Our model also incorporates additional enhancements for improved performance:
- **Dynamic Learning Rate Adjustment**: Adapts the learning rate based on validation performance.
- **Multilingual Training Support**: Extends capabilities to generate text in multiple languages with diverse scripts.
- **Attention Map Visualization**: Provides insights into which parts of the image are most influenced by specific textual prompts.

## Technologies Used 🛡️

- **Backend**: Flask, Python (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary.)
- **Frontend**: React.js, HTML, CSS (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary.)
- **Database**: PostgreSQL (Note: This is based on FYP1 deliverables. Actual implementation details for FYP2 may vary.)
- **AI/ML Models**: Fine-Tuned Stable Diffusion Model, Generative Adversarial Networks (GANs) with PyTorch.
- **Datasets**: COCO-Text, TextCaps, Custom Multilingual Dataset.

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

**Internal Supervisor**: Sir Osama Ahmed Khan
**External Supervisor & Sponsor**: **Mirza Samad Ahmed Baig** (mirzasamadahmedbaig@gmail.com)

**Team Members**:
- **Syeda Anshrah Gillani (Group Leader)** (1337-2021)
- Umema Mujeeb (2396-2021)
- Maheen Ali (1589-2021)

## FYP1 Deliverables 📦

The following key deliverables from FYP1 are available in the `docs/fyp1` directory:

- **FYP 1 Details**: `fyp1_details.pdf`
- **Project Plan (Gantt Chart)**: `project_plan.pdf`
- **Gap Analysis**: `gap_analysis.pdf`
- **Demo Notebook**: `demo.ipynb`
- **FYP1 Presentation**: `fyp1_presentation.pptx`
- **Presentation Template**: `presentation_template.pptx`
- **Model Training Recording**: `model_training_recording.mov`
- **Standee Design**: `standee.pdf`
- **Image Asset**: `image.png`

## Project Structure 📁

The repository is organized as follows:

```
TextPixs/
├── docs/                 # Project documentation and deliverables
│   ├── assets/           # Images and other assets for README and documentation
│   └── fyp1/             # Contains all deliverables from FYP1
├── .github/              # GitHub Actions workflows and configurations
├── LICENSE               # Project license
└── README.md             # This README file
```
*(Note: Additional directories for code (e.g., `src/`, `backend/`, `frontend/`) will be added as the implementation phase of FYP2 progresses.)*

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
