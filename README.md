# 🚀 LinkedIn AI Consultant

> AI-powered LinkedIn consulting chatbot that helps professionals optimize their profiles, develop content strategies, and accelerate career growth.

**Meet Hayek** - Your intelligent LinkedIn growth consultant powered by Google Gemini AI.

## 👥 Developers

**Built with ❤️ by Acile and Shawn**

## ✨ Features

- **Profile Optimization**: Headlines, summaries, experience sections, skills
- **Content Strategy**: Thought leadership, viral content formulas, engagement tactics  
- **Personal Branding**: Professional positioning, industry authority building
- **Networking**: Connection strategies, relationship building, outreach templates
- **Career Growth**: Job search optimization, recruiter attraction, salary negotiation
- **Lead Generation**: Using LinkedIn for business development

## 🛠️ Tech Stack

- **Frontend**: Gradio web interface with custom styling
- **Backend**: Python with Google Gemini 2.5 Flash AI model
- **Infrastructure**: Docker containerization
- **AI Model**: Google Gemini 2.5 Flash for advanced reasoning and conversation

## 🚀 Quick Start

### Prerequisites
- Docker installed and running
- Google API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd linkedin-ai-consultant
```

### 2. Get Google API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Copy the key for the next step

### 3. Build & Run (One Command!)
```bash
./run YOUR_GOOGLE_API_KEY
```

### 4. Access the Application
- Open your browser to: **http://localhost:7860**
- Start consulting with Hayek! 💼

## 📋 Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Build Docker image
docker build -t linkedin-ai-consultant .

# Run container
docker run -d \
  --name linkedin-consultant \
  -p 7860:7860 \
  -e GOOGLE_API_KEY="YOUR_API_KEY" \
  linkedin-ai-consultant
```

## 🎯 Example Conversations

Try these consulting topics:

- "How can I optimize my LinkedIn headline to attract more recruiters?"
- "What's the best content strategy to establish thought leadership in tech?"
- "I need help writing a compelling LinkedIn summary for my profile"
- "How do I network effectively on LinkedIn without being pushy?"
- "What are the best practices for LinkedIn posts that go viral?"
- "I'm job hunting - how can I make my profile stand out?"

## 🐳 Docker Commands

```bash
# Check container status
docker ps

# View logs
docker logs linkedin-consultant

# Stop container
docker stop linkedin-consultant

# Remove container
docker rm linkedin-consultant
```

## 📁 Project Structure

```
linkedin-ai-consultant/
├── linkedin_consultant.py    # Main Gradio application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
├── run                      # Automated build & deploy script
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key (required)

### Model Configuration
- **Default Model**: `gemini-2.5-flash`
- **Features**: Advanced reasoning, multimodal capabilities
- **Context Window**: 1M tokens for long conversations

## 🌟 Key Features

### AI Consultant "Hayek"
- **Strategic Focus**: Long-term professional goals and brand building
- **Data-Driven**: Uses LinkedIn analytics and industry benchmarks  
- **Actionable**: Provides specific, implementable strategies
- **Results-Oriented**: Focus on measurable outcomes
- **Industry-Aware**: Tailored advice for specific industries

### Web Interface
- **Modern Design**: Professional styling with LinkedIn-inspired theme
- **Interactive Chat**: Real-time conversation with markdown support
- **Examples**: Pre-loaded consulting scenarios
- **Responsive**: Works on desktop and mobile
- **Professional**: Executive-level communication

## 🚨 Troubleshooting

### Container Won't Start
```bash
# Check Docker is running
docker info

# Check logs for errors
docker logs linkedin-consultant
```

### API Key Issues
- Ensure your Google API key is valid
- Check billing is enabled on your Google Cloud account
- Verify the key has Gemini API access

### Port Already in Use
```bash
# Stop existing container
docker stop linkedin-consultant

# Or use different port
docker run -p 8080:7860 ...
```

## 📊 Performance & Usage

- **Response Time**: ~2-5 seconds for complex consulting queries
- **Concurrent Users**: Supports multiple simultaneous consultations
- **Model Capacity**: 1M token context for detailed conversations
- **Cost**: Pay-per-use Google Gemini API pricing

## 🔒 Security & Privacy

- **API Key**: Securely passed as environment variable
- **No Data Storage**: Conversations are not persisted
- **Professional Focus**: Designed for business/career consultation
- **HTTPS Ready**: Container supports SSL termination

## 📝 License

This project is available for professional and educational use. Please ensure compliance with Google's API terms of service.

---

**Ready to transform your LinkedIn presence?** 🎯  
Start chatting with Hayek at http://localhost:7860

*Built with ❤️ by **Acile** and **Shawn** for LinkedIn professionals everywhere*