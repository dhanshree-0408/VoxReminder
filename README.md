# 🎙️ VoxReminder AI: Voice-Activated Notification Engine

VoxReminder is a high-performance **multimodal AI assistant** that leverages **OpenAI Whisper** and custom NLP logic to convert natural language voice commands into scheduled email alerts. Built with a **platform-agnostic architecture**, it is designed to run seamlessly in Dockerized cloud environments or locally across macOS, Windows, and Linux.

## 🚀 Key Features

  * **Local AI Inference:** Utilizes **OpenAI's Whisper (base model)** for high-accuracy Speech-to-Text (STT) processing with zero API latency.
  * **Dynamic NLU Engine:** Employs a custom parsing layer using `dateparser` and regular expressions to interpret complex temporal intent (e.g., "in 15 minutes", "tomorrow at 5 PM").
  * **Asynchronous Scheduling:** Powered by `APScheduler` to manage non-blocking background tasks, ensuring the UI remains responsive while handling multiple reminder threads.
  * **Secure SMTP Integration:** Automated email delivery system utilizing **Gmail SMTP** and secure environment variable management.
  * **Containerized Architecture:** Fully **Dockerized** to ensure consistent environment parity across development and production stages.

## 🛠️ Tech Stack

  * **Language:** Python 3.10+
  * **AI/ML:** OpenAI Whisper
  * **Backend & UI:** Streamlit
  * **Automation:** APScheduler, Dateparser
  * **DevOps:** Docker, python-dotenv

## 📦 Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/dhanshree-0408/VoxReminder.git
    cd VoxReminder
    ```

2.  **Set up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory:

    ```text
    SENDER_EMAIL=your-email@gmail.com
    SENDER_PASSWORD=your-16-character-app-password
    ```

5.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## 🐳 Docker Deployment

To run the application in a containerized environment:

```bash
docker build -t voxreminder-ai .
docker run -p 8501:8501 --env-file .env voxreminder-ai
```

## 🗺️ Roadmap

  - [ ] **Multi-Channel Alerts:** Integration with Twilio API for WhatsApp and SMS notifications.
  - [ ] **Persistent Storage:** Migration from in-memory scheduling to SQLite/PostgreSQL for task persistence.
  - [ ] **User Authentication:** Secure login for personalized reminder histories.

-----

**Developer:** [Dhanshree Patel](https://www.linkedin.com/in/dhanshree-patel-94b500190/)
