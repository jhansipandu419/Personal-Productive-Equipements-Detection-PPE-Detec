# Personal Productive Equipements Detection (PPE Detec) 🚧🤖

![PPE Detection](https://img.shields.io/badge/PPE%20Detection-AI%20Powered-brightgreen)
![Releases](https://img.shields.io/badge/Releases-Latest%20Version-blue)

Welcome to the **Personal Productive Equipements Detection (PPE Detec)** repository! This project leverages artificial intelligence to detect personal protective equipment (PPE) and integrates face recognition for enhanced access control. With an Arduino-controlled system that uses a stepper motor and LEDs, this setup ensures safety and security in various environments.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [System Architecture](#system-architecture)
7. [How It Works](#how-it-works)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Project Overview

The PPE Detec project aims to create a reliable and efficient system for detecting PPE in real-time. This is especially important in workplaces where safety is a priority. The integration of face recognition technology allows for personalized access control, ensuring that only authorized personnel can enter specific areas.

### Key Components:

- **AI-Powered Detection**: Utilizes computer vision algorithms to identify PPE.
- **Face Recognition**: Ensures secure access based on user identification.
- **Arduino Control**: Manages hardware components like stepper motors and LEDs.
- **User Interface**: Provides feedback and control options.

For the latest version of the software, visit our [Releases](https://github.com/jhansipandu419/Personal-Productive-Equipements-Detection-PPE-Detec/releases) section.

## Features

- **Real-Time PPE Detection**: Quickly identifies whether individuals are wearing required protective gear.
- **Secure Access Control**: Uses face recognition to manage entry to restricted areas.
- **Arduino Integration**: Controls hardware components efficiently.
- **Visual Feedback**: LEDs indicate system status and user access.
- **User-Friendly Interface**: Simple interaction for users and administrators.

## Technologies Used

This project incorporates a variety of technologies to achieve its goals:

- **Artificial Intelligence**: For detecting PPE and recognizing faces.
- **Arduino**: For controlling hardware components.
- **Computer Vision**: To analyze video feeds and identify PPE.
- **Stepper Motor**: For mechanical movement.
- **LEDs**: For visual indications.
- **YOLO (You Only Look Once)**: A real-time object detection system.

## Installation

To set up the PPE Detec system, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jhansipandu419/Personal-Productive-Equipements-Detection-PPE-Detec.git
   cd Personal-Productive-Equipements-Detection-PPE-Detec
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Arduino**:
   - Open the Arduino IDE.
   - Load the provided Arduino sketch from the `arduino` folder.
   - Connect your Arduino board and upload the sketch.

4. **Configure the System**:
   - Modify the configuration files as needed.
   - Set up the camera for video input.

5. **Run the Application**:
   Execute the main script:
   ```bash
   python main.py
   ```

For additional details on installation, refer to the documentation in the repository.

## Usage

After installation, the system is ready to use. Follow these steps:

1. **Start the Application**: Run the main script as shown above.
2. **Approach the Camera**: The system will detect your face and check for PPE.
3. **Access Control**: If recognized and compliant with PPE requirements, access will be granted.
4. **Visual Feedback**: LEDs will indicate whether access is granted or denied.

## System Architecture

The architecture of the PPE Detec system consists of several components working together:

- **Camera Module**: Captures video feed for analysis.
- **Processing Unit**: Runs the AI algorithms for PPE detection and face recognition.
- **Arduino Board**: Controls the stepper motor and LEDs based on input from the processing unit.
- **User Interface**: Displays status and logs activities.

```plaintext
+-------------------+
|    Camera Module   |
+-------------------+
          |
          v
+-------------------+
| Processing Unit    |
| (AI Algorithms)    |
+-------------------+
          |
          v
+-------------------+
|    Arduino Board   |
| (Control Hardware) |
+-------------------+
          |
          v
+-------------------+
|    User Interface   |
+-------------------+
```

## How It Works

1. **Face Detection**: The camera captures video frames and sends them to the processing unit.
2. **PPE Detection**: The AI model analyzes the frames to check for PPE compliance.
3. **Face Recognition**: The system identifies the individual using face recognition algorithms.
4. **Access Control**: Based on the recognition and PPE status, the Arduino controls the stepper motor to unlock or lock access.
5. **Feedback**: LEDs provide visual feedback on access status.

## Contributing

We welcome contributions to improve the PPE Detec project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

Please ensure your code follows the existing style and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out:

- **Author**: [Jhansi Pandu](https://github.com/jhansipandu419)
- **Email**: jhansipandu@example.com

For the latest updates and releases, check our [Releases](https://github.com/jhansipandu419/Personal-Productive-Equipements-Detection-PPE-Detec/releases) section.

Thank you for your interest in the PPE Detec project!