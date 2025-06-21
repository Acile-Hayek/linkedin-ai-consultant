import gradio as gr
import os
from google import genai
import markdown

def generate_response(message, history):
    """
    Send a request to Google's Gemini API and get the response with markdown formatting
    """
    if not message.strip():
        return "Please enter a message."

    # Check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "❌ **Error**: Please set your GOOGLE_API_KEY environment variable."

    try:
        # Initialize Gemini client
        client = genai.Client(api_key=api_key)

        # Prepare the context from history
        context = ""
        for human, assistant in history:
            context += f"**Client**: {human}\n\n**Hayek**: {assistant}\n\n"

        # Prepare the prompt with history context
        prompt = f"{context}**Client**: {message}\n\n**Hayek**:"

        # Send request to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""You are Hayek, a Professional LinkedIn Promoter & Career Growth Consultant.

**Primary Objective**: Help professionals maximize their LinkedIn presence, build powerful personal brands, and accelerate career growth through strategic networking and content marketing.

**Core Areas of Expertise**:
- **LinkedIn Profile Optimization**: Headlines, summaries, experience sections, skills, recommendations
- **Content Strategy & Creation**: Thought leadership, industry insights, engagement tactics, viral content formulas
- **Personal Branding**: Professional positioning, unique value proposition, industry authority building
- **Networking & Relationship Building**: Connection strategies, outreach templates, relationship nurturing
- **Career Advancement**: Job search optimization, recruiter attraction, salary negotiation, career pivoting
- **Industry Positioning**: Establishing expertise, building credibility, becoming a recognized thought leader

**Advanced Consulting Services**:
- **Profile Audit & Optimization**: Comprehensive LinkedIn profile analysis and enhancement
- **Content Calendar Planning**: Strategic posting schedules and content themes
- **Engagement Strategy**: Comment tactics, post timing, algorithm optimization
- **Network Expansion**: Targeted connection strategies and relationship building
- **Thought Leadership Development**: Establishing expertise and industry recognition
- **Personal Brand Architecture**: Crafting compelling professional narratives
- **Lead Generation**: Using LinkedIn for business development and client acquisition
- **Crisis Management**: Handling professional reputation issues

**Consultation Style**:
- **Data-Driven**: Use LinkedIn analytics, engagement metrics, and industry benchmarks
- **Actionable**: Provide specific, implementable strategies with clear next steps
- **Results-Oriented**: Focus on measurable outcomes like profile views, connection growth, job opportunities
- **Industry-Aware**: Tailor advice to specific industries and professional levels
- **Trend-Current**: Stay updated on LinkedIn algorithm changes and platform features

**Response Guidelines**:
- **Strategic Focus**: Always think about long-term professional goals and brand building
- **Markdown Formatting**: Use headers, bullet points, and emphasis for professional presentation
- **Practical Examples**: Provide real templates, scripts, and actionable content
- **Metrics-Minded**: Suggest ways to measure success and track progress
- **Platform Expertise**: Demonstrate deep understanding of LinkedIn's features and algorithm
- **Professional Tone**: Maintain executive-level communication while being approachable
- **Competitive Edge**: Help clients stand out in crowded professional markets

**Value Propositions**:
- Transform LinkedIn profiles into lead generation machines
- Build thought leadership that attracts opportunities
- Create content strategies that generate consistent engagement
- Develop networking approaches that build valuable professional relationships
- Position clients as industry experts and go-to professionals

**Communication Approach**:
- Ask strategic questions to understand career goals and current challenges
- Provide specific, actionable recommendations with clear implementation steps
- Share industry insights and best practices
- Offer templates, examples, and proven frameworks
- Focus on ROI and measurable professional outcomes

Remember: Every interaction should move the client closer to their professional goals and enhance their LinkedIn presence for maximum career impact.

{prompt}"""
        )

        # Convert response to markdown if it isn't already
        response_text = response.text
        
        # Add some basic formatting improvements if needed
        if not any(marker in response_text for marker in ['**', '*', '#', '-', '1.']):
            # If no markdown formatting detected, add some basic structure
            lines = response_text.split('\n')
            formatted_lines = []
            for line in lines:
                line = line.strip()
                if line:
                    if line.endswith(':') and len(line) < 50:
                        formatted_lines.append(f"**{line}**")
                    else:
                        formatted_lines.append(line)
                else:
                    formatted_lines.append('')
            response_text = '\n'.join(formatted_lines)

        return response_text

    except Exception as e:
        return f"❌ **Error**: Could not connect to Gemini API. Please check your API key and internet connection.\n\n**Details**: {str(e)}"

def submit_message(message, history):
    """
    Handle message submission
    """
    if message is None or len(message.strip()) == 0:
        return "", history

    response = generate_response(message, history)
    history = history + [(message, response)]
    return "", history

# JavaScript code for welcome message animation
js_welcome_animation = """
function createWelcomeAnimation() {
    var container = document.createElement('div');
    container.id = 'welcome-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';
    container.style.background = 'linear-gradient(45deg, #0077B5 0%, #00A0DC 50%, #40E0D0 100%)';
    container.style.backgroundClip = 'text';
    container.style.webkitBackgroundClip = 'text';
    container.style.webkitTextFillColor = 'transparent';

    var text = 'Transform Your LinkedIn Presence with Hayek!';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 80);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    if (gradioContainer) {
        gradioContainer.insertBefore(container, gradioContainer.firstChild);
    }

    setTimeout(function() {
        var welcomeAnim = document.getElementById('welcome-animation');
        if (welcomeAnim) {
            welcomeAnim.style.opacity = '0';
            setTimeout(function() { 
                if (welcomeAnim.parentNode) {
                    welcomeAnim.remove(); 
                }
            }, 1000);
        }
    }, 12000); // Remove animation after 12 seconds

    return 'Animation created';
}
"""

def create_chat_interface():
    """
    Create the chat interface with custom components
    """
    with gr.Blocks(
        theme="citrus", 
        js=js_welcome_animation,
        title="Hayek - LinkedIn Growth Consultant",
        css="""
        .gradio-container {
            max-width: 1000px !important;
            margin: auto !important;
        }
        .message {
            border-radius: 15px !important;
        }
        #header {
            background: linear-gradient(135deg, #0077B5 0%, #00A0DC 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        """
    ) as chat_app:
        
        gr.HTML("<script>createWelcomeAnimation();</script>")

        gr.Markdown(
            """
            # 🚀 Hayek - LinkedIn Growth Consultant
            ### *Your Strategic Partner for Professional Success & Personal Branding*
            
            **Expertise**: Profile Optimization • Content Strategy • Networking • Thought Leadership • Career Growth • Lead Generation
            """,
            elem_id="header"
        )

        # API Key status check
        api_key_status = gr.Markdown(
            "🔑 **API Status**: " + ("✅ Connected" if os.getenv("GOOGLE_API_KEY") else "❌ Please set GOOGLE_API_KEY environment variable")
        )

        chatbot = gr.Chatbot(
            height=650,
            show_label=False,
            container=True,
            bubble_full_width=False,
            render_markdown=True,
            avatar_images=("https://api.dicebear.com/7.x/professional/svg?seed=client&backgroundColor=f0f8ff", 
                          "https://api.dicebear.com/7.x/professional/svg?seed=hayek&backgroundColor=0077B5&clothingColor=ffffff")
        )

        with gr.Row():
            message = gr.Textbox(
                label="💼 What's your LinkedIn growth challenge?",
                placeholder="Ask about profile optimization, content strategy, networking, or any LinkedIn growth topic...",
                lines=3,
                scale=8,
                max_lines=5
            )
            submit_btn = gr.Button(
                "Get Strategy 📈",
                variant="primary",
                scale=1,
                size="lg"
            )

        with gr.Row():
            clear_btn = gr.Button("🗑️ Clear Session", variant="secondary")
            undo_btn = gr.Button("↩️ Undo Last", variant="secondary")

        # Example prompts with LinkedIn consulting focus
        gr.Examples(
            examples=[
                "How can I optimize my LinkedIn headline to attract more recruiters?",
                "What's the best content strategy to establish thought leadership in tech?",
                "I need help writing a compelling LinkedIn summary for my profile",
                "How do I network effectively on LinkedIn without being pushy?",
                "What are the best practices for LinkedIn posts that go viral?",
                "I'm job hunting - how can I make my profile stand out to hiring managers?",
                "How do I transition my LinkedIn from one industry to another?",
                "What's the best way to ask for LinkedIn recommendations?",
                "How can I use LinkedIn to generate leads for my business?",
                "I want to build a personal brand - where should I start on LinkedIn?"
            ],
            inputs=message,
            label="💡 Popular Consulting Topics - Click to explore:"
        )

        # Professional information footer
        gr.Markdown(
            """
            ---
            ## 📊 **Your LinkedIn Growth Metrics Dashboard**
            
            **Track Your Progress:**
            - Profile views and search appearances
            - Connection growth rate
            - Post engagement rates
            - Industry ranking improvements
            
            **Professional Resources:**
            - **LinkedIn Learning**: [LinkedIn Marketing Solutions](https://business.linkedin.com/)
            - **LinkedIn Creator Hub**: [Create compelling content](https://www.linkedin.com/creators/)
            - **LinkedIn Sales Navigator**: [Advanced networking tools](https://business.linkedin.com/sales-solutions)
            
            **Ready to Transform Your Career?** 
            Book a comprehensive LinkedIn audit and strategy session with Hayek!
            
            ---
            *🔒 Confidential consultations • 📈 Data-driven strategies • 🎯 Results-focused approach*
            """,
            elem_id="footer"
        )

        # Set up event handlers
        submit_btn.click(
            fn=submit_message,
            inputs=[message, chatbot],
            outputs=[message, chatbot],
            queue=True
        )

        # Also allow submission with Enter key
        message.submit(
            fn=submit_message,
            inputs=[message, chatbot],
            outputs=[message, chatbot],
            queue=True
        )

        clear_btn.click(
            lambda: (None, "🚀 New consultation session started! What LinkedIn challenge can I help you solve today?"), 
            None, 
            [chatbot, message], 
            queue=False
        )
        
        undo_btn.click(
            lambda x: (x[:-1] if len(x) > 0 else x), 
            chatbot, 
            chatbot, 
            queue=False
        )

    return chat_app

# Run the app
if __name__ == "__main__":
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not set!")
        print("📝 Please set it using: -e GOOGLE_API_KEY='your-api-key-here' when running docker")
        print("🔗 Get your API key from: https://aistudio.google.com/app/apikey")
        print("💼 Ready to transform LinkedIn strategies with AI-powered consulting!")
    
    chat_app = create_chat_interface()
    chat_app.launch(
        server_name="0.0.0.0", 
        server_port=7860,
        show_error=True,
        share=False
    )