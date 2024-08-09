# FaceLogin Calendar App

**FaceLogin Calendar App** is a web application that combines facial recognition technology with a robust calendar management system. Users can log in securely using facial recognition, manage their events with a customizable calendar, and receive notifications for upcoming events. This app aims to enhance event management while leveraging modern authentication technologies.

## Features

- **Facial Recognition Login:** Secure login using facial recognition technology.
- **Customizable Calendar:** Manage and track events with customizable colors.
- **Event Management:** Create, edit, and delete events easily.
- **Notifications:** Receive reminders for upcoming events.
- **User-Specific Data Storage:** Personalized calendar and event data storage.

## Prerequisites

To run the FaceLogin Calendar App locally, you'll need the following:

- **Python 3.12**: The application is developed with Python 3.12.
- **Required Python Packages**: Ensure the following packages are installed:
  - `Flask`
  - `Flask-Session`
  - `CS50`
  - `face_recognition`
  - `Pillow`
  - `playsound`
  - `requests`
- **Webcam**: Required for facial recognition functionality.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PJR23/facelogin-calendar-app.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd facelogin-calendar-app
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    Create a `requirements.txt` file with the following content:

    ```plaintext
    Flask
    Flask-Session
    cs50
    face_recognition
    Pillow
    playsound
    requests
    ```

    Install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

## Running the App

1. **Start the application:**

    Execute the following command to start the Flask application:

    ```bash
    python application.py
    ```

2. **Access the app:**

    Open a web browser and navigate to `http://localhost:5000` to use the FaceLogin Calendar App.

## Troubleshooting

- **Dependencies:** Ensure all required packages are installed. Use `pip` to install any missing dependencies.
- **Facial Recognition Issues:** Verify that your webcam is operational and that the `face_recognition` library can access it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


