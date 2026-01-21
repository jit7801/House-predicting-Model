# 🏠 House Price Prediction Web App (Predict.in)

A machine learning–powered **House Price Prediction** project with a clean and responsive **web UI** built using **Flask, HTML, and CSS**. Users can enter house details and instantly get an estimated price based on a trained ML model.

This project combines **data science + web development**, making it ideal for learning full-stack ML deployment.

---

## 🚀 Features

* 📊 Machine Learning–based house price prediction
* 🌐 Web UI built with HTML & CSS
* ⚡ Fast predictions using a pre-trained model
* 🎨 Clean and responsive design
* 📄 Multiple pages (Home, Models, Sign In, About Us)

---

## 🛠️ Tech Stack

* **Python**
* **Flask** (Backend & Routing)
* **Machine Learning** (Scikit-learn)
* **HTML5 & CSS3** (Frontend)
* **Jinja2** (Template Rendering)

---

## 📁 Project Structure

```
House-predicting-Model/
│
├── app.py                  # Flask backend
│
├── static/
│   ├── style.css           # Main UI styles
│   ├── about.css           # About page styles
│   ├── modals.css          # Models page styles
│   ├── sign.css            # Sign In / Sign Up styles
│   └── web_logo.jpeg       # Project logo
│
├── templates/
│   ├── index.html          # Home / Prediction page
│   ├── aboutme.html        # About Us page
│   ├── modals.html         # Model info page
│   └── sign.html           # Login / Signup page
│
├── Home_price_predictor.py # Trained ML model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jit7801/House-predicting-Model.git
cd House-predicting-Model
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app.py
```

After running the command, open your browser and go to:

👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🧠 How It Works

1. User enters house details in the web form
2. Data is sent to the Flask backend
3. Backend loads the trained ML model
4. Model predicts the house price
5. Result is displayed instantly on the UI

---

## 📸 Screenshots
<img width="1710" height="1112" alt="Screenshot 2026-01-21 at 9 58 42 PM" src="https://github.com/user-attachments/assets/2a6171f5-36e7-45ce-8123-67171367d400" />
<img width="541" height="577" alt="Screenshot 2026-01-21 at 10 00 59 PM" src="https://github.com/user-attachments/assets/83ae770b-aef8-4fe6-a9d3-4855142fb40f" />
<img width="521" height="609" alt="Screenshot 2026-01-21 at 10 01 22 PM" src="https://github.com/user-attachments/assets/f15243df-b3f9-4796-96a2-9da6dfa50ace" />
<img width="1710" height="1112" alt="Screenshot 2026-01-21 at 9 59 09 PM" src="https://github.com/user-attachments/assets/273ca439-fc96-471d-ac91-04d437a67ce0" />
<img width="1710" height="1112" alt="Screenshot 2026-01-21 at 9 59 26 PM" src="https://github.com/user-attachments/assets/6c26c445-4e69-4ccd-ae93-035173dc000c" />



---

## 📌 Future Improvements

* 🔐 User authentication with database
* 📈 Model performance comparison page
* ☁️ Cloud deployment (Render / Railway / AWS)
* 🗺️ Location-based price visualization

---

## 👨‍💻 Author

**Jitesh Vishnoi**
Founder & Developer
Linkedin: **www.linkedin.com/in/hello-jitesh-vishnoi-381a04370**

---

## ⭐ Support

If you like this project, give it a **⭐ star** on GitHub — it really helps!

Feel free to fork, improve, and use it for learning purposes.

---

> *Built with passion for Machine Learning & Web Development.* 💙
