# **AI-Powered Image Posting to Twitter**

This script automates the process of:  
1. **Generating images** using OpenAI's **DALL·E API**.  
2. **Saving the image locally** in a usable format (`PNG`).  
3. **Posting the image with a caption** to Twitter using Twitter's API v2.  

---

## **Features**
- Generate high-quality images from text prompts using OpenAI's **DALL·E**.
- Automatically save the image locally in a usable format.
- Post the saved image to Twitter with a custom caption.
- Easy to configure and extend for automation.

---

## **Requirements**
1. **APIs Needed**:
   - OpenAI API Key (for image generation).
   - Twitter API v2 credentials:
     - API Key  
     - API Key Secret  
     - Access Token  
     - Access Token Secret  
2. **Python Libraries**:
   - `requests`  
   - `tweepy`  
   - `openai`  
   - `python-dotenv`  

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-twitter-image-posting.git
cd ai-twitter-image-posting
```
### **2. Install Dependencies**
```bash
pip install requests tweepy openai python-dotenv
```

### **3. Set Up Environment Variables**
```python
# OpenAI API Key
OPENAI_API_KEY=your-openai-api-key

# Twitter API Credentials
TWITTER_API_KEY=your-twitter-api-key
TWITTER_API_SECRET=your-twitter-api-secret
TWITTER_ACCESS_TOKEN=your-twitter-access-token
TWITTER_ACCESS_SECRET=your-twitter-access-secret
```


### **4. Run the Script**
```bash
python main.py
```


### **5. Profit**
```bash
sudo print-money
```


