# TextPixs 🎨✨

Welcome to **TextPixs**, a research-based, AI-powered tool designed to generate stunning, high-quality images directly from text prompts. TextPixs aims to redefine creativity by making professional-quality visuals accessible to everyone, regardless of artistic skills or experience, while addressing critical challenges in text-to-image generation.

## Table of Contents 📚

- [About TextPixs](#about-textpixs)
- [Vision](#vision)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Roadmap](#roadmap)
- [Team](#team)
- [FYP1 Deliverables](#fyp1-deliverables)
- [Contributing](#contributing)
- [License](#license)

## About TextPixs 🖌️

**TextPixs** is a dynamic text-to-image generation platform built for users who want quick, compelling visuals. It is a research-based project focused on turning text into vibrant, detailed images, powered by cutting-edge generative AI technology.

The project addresses the significant challenge of accurate image generation and text rendering within images, which currently limits applications in educational tools, design automation, and digital art. Existing issues include ambiguity in text prompts, alignment challenges, and a lack of robust loss functions for text fidelity.

Our primary objectives include:
- Enhancing the rendering of images via text-to-image generation using state-of-the-art techniques.
- Improving text fidelity and visual quality in generated images.
- Developing a novel hybrid architecture with semantic alignment and text rendering loss.

## Vision 🌟

TextPixs intends to bridge the gap between ideas and visuals, providing users with a creative playground for generating, modifying, and refining images. Our purpose is to research and contribute breakthroughs in achieving excellence in text-to-image generation, with a focus on text fidelity improvements to advance applications in content creation, advertising, and human-computer interactions.

## Features 🚀

- **Text-to-Image Generation**: Input a description, and TextPixs will create a high-quality image that matches your vision. This feature leverages a hybrid architecture incorporating Generative Adversarial Networks (GANs) with a Generator and Discriminator, and integrates a fine-tuned Stable Diffusion model for robust image synthesis.
- **Image Modifications** (Phase 2): Modify existing images using text prompts for further customization and creativity.
- **Text-to-Video Capabilities** (Future Phase): Generate short videos from descriptive prompts.
- **User Authentication**: Google sign-in/sign-out options for a seamless login experience.

## Getting Started ⚙️

To start creating with TextPixs, follow these steps to get the project running locally.

### Prerequisites ✅

- Python 3.8 or higher
- Node.js and npm
- Git

## Installation 🛠️

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SyedaAnshrahGillani/textpixs.git
   cd textpixs
   ```

2. **Install Backend Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies:**

   ```bash
   cd frontend
   npm install
   ```

4. **Configure Environment Variables**:
   Set up the required API keys and environment variables in the `.env` file.

## Usage 💻

1. **Start the Backend Server**:

   ```bash
   python app.py
   ```

2. **Run the Frontend**:

   ```bash
   cd frontend
   npm start
   ```

3. Open your browser and go to `http://localhost:3000` to start creating images with TextPixs!

## Technologies Used 🛡️

- **Backend**: Flask, Python
- **Frontend**: React.js, HTML, CSS
- **Database**: PostgreSQL
- **AI/ML Models**: Fine-Tuned Stable Diffusion Model, Generative Adversarial Networks (GANs) with PyTorch.
- **Authentication**: Google OAuth

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

## Team 👥

**Internal Supervisor**: Sir Osama Ahmed Khan
**External Supervisor**: Mirza Samad Ahmed Baig

**Team Members**:
- Syeda Anshrah Gillani (1337-2021)
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

## Contributing 🤝

We welcome contributions! If you’re interested in improving TextPixs, please fork the repository, create a new branch, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b origin/main`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin origin/main`)
5. Open a pull request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.