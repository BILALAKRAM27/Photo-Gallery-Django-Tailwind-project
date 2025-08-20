
# 🖼️ Photo Gallery – Museum-like Experience  

![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)  
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38B2AC?logo=tailwind-css&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)  

---

## 🌟 Project Idea  
The **Photo Gallery** project is a web application where users can upload and manage their pictures in a **museum-like environment**.  

✨ Each photo can be:  
- 🔒 **Private** → Only visible to the uploader.  
- 🌍 **Public** → Visible to everyone, where users can **like** 👍 and **comment** 💬.  

The experience is inspired by a museum:  
- 🖼️ Photos act like exhibits.  
- 👥 Visitors can discuss (comments) and show appreciation (likes).  
- 🎨 Users can curate their own personal or public collections.  

---

## 🚀 Features  
✅ User authentication (sign up, login, logout)  
✅ Upload pictures with **privacy settings** (private/public)  
✅ Like ❤️ and comment 💬 on public photos  
✅ Responsive & modern UI with **Tailwind CSS**  
✅ Django-based backend for secure and scalable photo management  

---

## 📸 Screenshots (Demo)  
> *(Add screenshots of your project here once you run it, e.g. upload page, gallery page, comments section)*  

| Upload Page | Gallery Page | Comments |
|-------------|--------------|----------|
| ![upload](docs/screenshots/upload.png) | ![gallery](docs/screenshots/gallery.png) | ![comments](docs/screenshots/comments.png) |

---

## 🛠️ Tech Stack  
- **Backend:** [Django](https://www.djangoproject.com/) (Python)  
- **Frontend:** [Tailwind CSS](https://tailwindcss.com/)  
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)  
- **Version Control:** Git + GitHub  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/BILALAKRAM27/Photo-Gallery-Django-Tailwind-project.git
cd Photo-Gallery-Django-Tailwind-project
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the server

```bash
python manage.py runserver
```

Now open 👉 `http://127.0.0.1:8000/` in your browser.

---

## 🧩 Project Structure

```
Photo-Gallery-Django-Tailwind-project/
│── photogallery/         # Main Django project
│── gallery/              # App for handling photos
│── templates/            # HTML templates
│── static/               # CSS, JS, images
│── media/                # Uploaded photos
│── requirements.txt      # Dependencies
│── manage.py             # Django manager
```

---

## 🌍 Future Improvements

* 🔑 OAuth login (Google, GitHub)
* 🏷️ Tags & categories for photos
* 🔔 Real-time notifications for likes & comments
* 📤 Share photos via link or social media
* 🏆 "Most liked photos" leaderboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new branch (`feature-new`)
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

### 💡 Inspiration

> *"Just like in a museum, every picture tells a story. Some are shared with the world, some remain personal treasures."*

```
