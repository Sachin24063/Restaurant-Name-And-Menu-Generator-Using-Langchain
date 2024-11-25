# 🍽️ Restaurant Name & Menu Generator

Welcome to the **Restaurant Name & Menu Generator**! 🎉  
This application uses the power of **LangChain** and **OpenAI's GPT-3** to generate creative restaurant names and delicious menu items based on a cuisine of your choice.

## 📌 Overview

Are you dreaming of opening a new restaurant but need help coming up with a name and menu? This app will help you out! Select a cuisine from the sidebar, and the app will generate:

- A creative restaurant name
- A list of menu items that match the theme of the restaurant

The app is built with **Streamlit** and integrates with **LangChain** for seamless interaction with OpenAI's GPT-3.

## 🚀 Features

- **Choose Your Cuisine**: Select from a variety of cuisines like Indian, Mexican, Italian, and more.
- **Automatic Name Generation**: Get a fancy, unique name for your restaurant based on your chosen cuisine.
- **Menu Suggestions**: Receive a curated list of food items that would fit your restaurant’s concept.
- **Real-Time Updates**: Everything updates in real-time when you select a new cuisine.

## 📸 Layout

Here’s a preview of the app’s interface:

![Layout Preview](app.png)

## 🔧 Installation

To run the application locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/restaurant-name-generator.git
```

### 2. Install dependencies

```bash
cd restaurant-name-generator
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set your OpenAI API Key

Ensure your OpenAI API key is set as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"  # On Windows, use set instead of export
```

### 4. Run the app

```bash
streamlit run main.py
```
