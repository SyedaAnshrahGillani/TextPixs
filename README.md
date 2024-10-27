# TextPixs 🎨✨

Welcome to **TextPixs**, the AI-powered tool that allows users to create stunning, high-quality images directly from text prompts. **TextPixs** aims to redefine creativity by making professional-quality visuals accessible to everyone, regardless of artistic skills or experience.

## Table of Contents 📚

- [About TextPixs](#about-textpixs)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## About TextPixs 🖌️

**TextPixs** is a dynamic text-to-image generation platform built for users who want quick, compelling visuals. Using advanced AI models, TextPixs can generate images from a wide range of descriptive prompts. Its streamlined interface ensures ease of use for both newcomers and seasoned designers.

### Vision 🌟

TextPixs intends to bridge the gap between ideas and visuals, providing users with a creative playground for generating, modifying, and refining images.

## Features 🚀

- **Text-to-Image Generation**: Input a description, and TextPixs will create a high-quality image that matches your vision.
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
- **AI/ML Models**: Fine-Tuned, Stable Diffusion Model [This specification might change after R&D Phase]
- **Authentication**: Google OAuth

## Roadmap 🗺️

- **Phase 1**: Text-to-Image generation, Google sign-in/sign-out
- **Phase 2**: Image Modification with Text Prompts
- **Future Phase**: Text-to-Video Generation

## Contributing 🤝

We welcome contributions! If you’re interested in improving TextPixs, please fork the repository, create a new branch, and submit a pull request. 

1. Fork the repository
2. Create your feature branch (`git checkout -b origin/main`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin origin/main`)
5. Open a pull request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.
