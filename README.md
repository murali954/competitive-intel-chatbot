# 🕵️ Competitive Intelligence Chatbot

This is an AI-powered chatbot built with LangChain and Gemini 1.5 Pro that helps business professionals track and analyze competitors. It provides insights like product launches, market share, trends, and strategic moves — while remembering your industry, competitors of interest, and goals, even across sessions.

## ⚙️ How to Set It Up

1. **Clone this repo**  
   `git clone https://github.com/murali954/competitive-intel-chatbot.git && cd competitive-intel-chatbot`

2. **Install dependencies**  
   `pip install -r requirements.txt`

3. **Add your API key**  
   Create a `.env` file in the root folder with this line:  
   `GOOGLE_API_KEY=your_google_gemini_api_key`

4. **Run the app**  
   `streamlit run app.py`

## 💬 What You Can Ask

- What are the latest product launches by Company X?
- How does Company Y's market share compare to competitors?
- Based on my industry, what are the trends in competitive strategies?
- What are the latest news articles about Company Z?
- Can you summarize Company A’s recent business moves?

## 🧠 Memory Features

The chatbot remembers:
- Your industry focus
- Competitors you’ve mentioned
- Research goals from past sessions  
It uses this + real-time data to provide personalized, relevant responses — even after clearing the chat.

## 📁 Project Structure

competitive-intel-chatbot/ ├── app.py # Streamlit app interface ├── agent.py # LangChain agent logic ├── .env # API keys (not committed) ├── requirements.txt # Python dependencies └── README.md 

markdown
Copy
Edit

## 📌 Tech Stack

- Python
- LangChain
- Gemini 1.5 Pro (via Google Generative AI)
- Streamlit

## 👨‍💻 Author

**Murali Krishna**  
Frontend Dev & AI Enthusiast  
GitHub: [@murali954](https://github.com/murali954)
