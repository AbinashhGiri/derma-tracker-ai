import React, { useState } from 'react';
import { Camera, MessageCircle, TrendingUp, Sparkles, Send, Home, Info } from 'lucide-react';

const DermaTracker = () => {
  const [activeTab, setActiveTab] = useState('home');
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', content: 'Hi there! 👋 I\'m your skincare companion. Ask me anything about acne, dryness, routines, or product recommendations!' }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [skinAnalysis, setSkinAnalysis] = useState(null);
  const [progressData, setProgressData] = useState([
    { date: 'Oct 1', hydration: 65, clarity: 70 },
    { date: 'Oct 8', hydration: 70, clarity: 75 },
    { date: 'Oct 15', hydration: 75, clarity: 80 },
    { date: 'Oct 22', hydration: 80, clarity: 85 },
  ]);

  const skinCareResponses = {
    acne: "For acne-prone skin, I recommend a gentle cleanser with salicylic acid, a lightweight moisturizer, and spot treatment with benzoyl peroxide. Don't forget sunscreen! Start slowly and be patient - skin takes time to adjust. 🌿",
    dry: "Dry skin needs extra love! Use a creamy cleanser, hyaluronic acid serum for hydration, and a rich moisturizer. Consider adding a facial oil at night. Avoid hot water and harsh soaps. 💧",
    oily: "Oily skin benefits from gel-based cleansers, niacinamide serum to balance oil production, and lightweight, oil-free moisturizers. Don't skip moisturizer - dehydrated skin produces MORE oil! ✨",
    routine: "A basic routine: Morning - cleanser, vitamin C serum, moisturizer, SPF. Evening - cleanser, treatment (retinol/acids), moisturizer. Start simple and add products gradually! 🌙",
    dark: "Dark spots respond well to vitamin C, niacinamide, and alpha arbutin. Always use SPF to prevent darkening. Patience is key - results take 6-8 weeks. Consider gentle exfoliation 2x weekly. 🌟"
  };

  const handleSendMessage = () => {
    if (!inputMessage.trim()) return;

    const userMessage = { role: 'user', content: inputMessage };
    setChatMessages(prev => [...prev, userMessage]);

    setTimeout(() => {
      let response = "I'm here to help! For specific concerns, you can ask me about acne, dry skin, oily skin, skincare routines, or dark spots. What would you like to know? 😊";
      
      const lowerInput = inputMessage.toLowerCase();
      if (lowerInput.includes('acne') || lowerInput.includes('pimple') || lowerInput.includes('breakout')) {
        response = skinCareResponses.acne;
      } else if (lowerInput.includes('dry') || lowerInput.includes('flaky')) {
        response = skinCareResponses.dry;
      } else if (lowerInput.includes('oily') || lowerInput.includes('greasy')) {
        response = skinCareResponses.oily;
      } else if (lowerInput.includes('routine') || lowerInput.includes('regimen')) {
        response = skinCareResponses.routine;
      } else if (lowerInput.includes('dark') || lowerInput.includes('spot') || lowerInput.includes('pigment')) {
        response = skinCareResponses.dark;
      }

      setChatMessages(prev => [...prev, { role: 'assistant', content: response }]);
    }, 800);

    setInputMessage('');
  };

  const analyzeSkin = () => {
    const skinTypes = ['Oily', 'Dry', 'Combination', 'Normal', 'Sensitive'];
    const randomType = skinTypes[Math.floor(Math.random() * skinTypes.length)];
    
    const analysis = {
      type: randomType,
      hydration: Math.floor(Math.random() * 30) + 60,
      clarity: Math.floor(Math.random() * 30) + 65,
      texture: Math.floor(Math.random() * 25) + 70,
      concerns: []
    };

    if (randomType === 'Oily') {
      analysis.concerns = ['Enlarged pores', 'Occasional breakouts', 'Excess shine'];
      analysis.recommendation = 'Use oil-free products, gentle exfoliation, and lightweight hydration.';
    } else if (randomType === 'Dry') {
      analysis.concerns = ['Tightness', 'Flaky patches', 'Fine lines'];
      analysis.recommendation = 'Focus on rich moisturizers, hydrating serums, and gentle cleansing.';
    } else if (randomType === 'Combination') {
      analysis.concerns = ['Oily T-zone', 'Dry cheeks', 'Occasional breakouts'];
      analysis.recommendation = 'Balance with targeted treatments - lightweight on oily areas, richer on dry zones.';
    } else if (randomType === 'Sensitive') {
      analysis.concerns = ['Redness', 'Irritation', 'Reactive skin'];
      analysis.recommendation = 'Stick to fragrance-free, gentle products. Patch test everything new.';
    } else {
      analysis.concerns = ['Minimal concerns', 'Well-balanced'];
      analysis.recommendation = 'Maintain your routine! Focus on prevention with SPF and antioxidants.';
    }

    setSkinAnalysis(analysis);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 via-purple-50 to-blue-50">
      {/* Header */}
      <div className="bg-white shadow-sm">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Sparkles className="w-8 h-8 text-purple-500" />
              <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                Derma Tracker
              </h1>
            </div>
            <p className="text-sm text-gray-600 hidden sm:block">Your AI Skincare Companion</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="max-w-6xl mx-auto px-4 py-4">
        <div className="flex gap-2 overflow-x-auto pb-2">
          {[
            { id: 'home', icon: Home, label: 'Home' },
            { id: 'chat', icon: MessageCircle, label: 'Chatbot' },
            { id: 'scan', icon: Camera, label: 'Scan Skin' },
            { id: 'progress', icon: TrendingUp, label: 'Progress' },
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-2 px-4 py-2 rounded-full transition-all whitespace-nowrap ${
                activeTab === tab.id
                  ? 'bg-purple-500 text-white shadow-lg'
                  : 'bg-white text-gray-600 hover:bg-purple-50'
              }`}
            >
              <tab.icon className="w-4 h-4" />
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-6xl mx-auto px-4 pb-8">
        {/* Home Tab */}
        {activeTab === 'home' && (
          <div className="space-y-6 animate-fadeIn">
            <div className="bg-white rounded-3xl shadow-lg p-8 text-center">
              <Sparkles className="w-16 h-16 mx-auto text-purple-500 mb-4" />
              <h2 className="text-3xl font-bold text-gray-800 mb-3">
                Welcome to Your Skincare Journey
              </h2>
              <p className="text-gray-600 max-w-2xl mx-auto mb-6">
                Track your skin health, get personalized advice, and watch your confidence bloom. 
                Your skin is unique, and so is your journey. 🌸
              </p>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
                <div className="bg-gradient-to-br from-pink-100 to-pink-50 rounded-2xl p-6">
                  <MessageCircle className="w-10 h-10 text-pink-600 mb-3" />
                  <h3 className="font-semibold text-gray-800 mb-2">AI Chat Assistant</h3>
                  <p className="text-sm text-gray-600">Get instant answers to your skincare questions</p>
                </div>
                <div className="bg-gradient-to-br from-purple-100 to-purple-50 rounded-2xl p-6">
                  <Camera className="w-10 h-10 text-purple-600 mb-3" />
                  <h3 className="font-semibold text-gray-800 mb-2">Skin Analysis</h3>
                  <p className="text-sm text-gray-600">Upload a photo for instant skin type detection</p>
                </div>
                <div className="bg-gradient-to-br from-blue-100 to-blue-50 rounded-2xl p-6">
                  <TrendingUp className="w-10 h-10 text-blue-600 mb-3" />
                  <h3 className="font-semibold text-gray-800 mb-2">Track Progress</h3>
                  <p className="text-sm text-gray-600">Monitor improvements over time</p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Chatbot Tab */}
        {activeTab === 'chat' && (
          <div className="bg-white rounded-3xl shadow-lg p-6 animate-fadeIn">
            <div className="flex items-center gap-3 mb-6 pb-4 border-b">
              <MessageCircle className="w-6 h-6 text-purple-500" />
              <h2 className="text-2xl font-bold text-gray-800">Chat with Your Skincare Expert</h2>
            </div>
            
            <div className="h-96 overflow-y-auto mb-4 space-y-4 px-2">
              {chatMessages.map((msg, idx) => (
                <div
                  key={idx}
                  className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  <div
                    className={`max-w-xs md:max-w-md rounded-2xl px-4 py-3 ${
                      msg.role === 'user'
                        ? 'bg-purple-500 text-white'
                        : 'bg-gray-100 text-gray-800'
                    }`}
                  >
                    {msg.content}
                  </div>
                </div>
              ))}
            </div>

            <div className="flex gap-2">
              <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                placeholder="Ask about acne, dryness, routines..."
                className="flex-1 px-4 py-3 rounded-full border-2 border-purple-200 focus:border-purple-500 focus:outline-none"
              />
              <button
                onClick={handleSendMessage}
                className="bg-purple-500 text-white p-3 rounded-full hover:bg-purple-600 transition-colors"
              >
                <Send className="w-5 h-5" />
              </button>
            </div>
          </div>
        )}

        {/* Scan Tab */}
        {activeTab === 'scan' && (
          <div className="bg-white rounded-3xl shadow-lg p-6 animate-fadeIn">
            <div className="flex items-center gap-3 mb-6 pb-4 border-b">
              <Camera className="w-6 h-6 text-purple-500" />
              <h2 className="text-2xl font-bold text-gray-800">Analyze Your Skin</h2>
            </div>

            {!skinAnalysis ? (
              <div className="text-center py-12">
                <div className="w-48 h-48 mx-auto bg-gradient-to-br from-purple-100 to-pink-100 rounded-full flex items-center justify-center mb-6">
                  <Camera className="w-20 h-20 text-purple-500" />
                </div>
                <h3 className="text-xl font-semibold text-gray-800 mb-3">Ready to scan your skin?</h3>
                <p className="text-gray-600 mb-6 max-w-md mx-auto">
                  Our AI will analyze your skin type and provide personalized recommendations
                </p>
                <button
                  onClick={analyzeSkin}
                  className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-8 py-3 rounded-full hover:shadow-lg transition-all"
                >
                  Start Analysis
                </button>
              </div>
            ) : (
              <div className="space-y-6">
                <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-2xl p-6">
                  <h3 className="text-2xl font-bold text-gray-800 mb-2">
                    Your Skin Type: {skinAnalysis.type}
                  </h3>
                  <p className="text-gray-600 mb-4">{skinAnalysis.recommendation}</p>
                  
                  <div className="grid grid-cols-3 gap-4 mb-4">
                    <div className="text-center">
                      <div className="text-3xl font-bold text-purple-600">{skinAnalysis.hydration}%</div>
                      <div className="text-sm text-gray-600">Hydration</div>
                    </div>
                    <div className="text-center">
                      <div className="text-3xl font-bold text-pink-600">{skinAnalysis.clarity}%</div>
                      <div className="text-sm text-gray-600">Clarity</div>
                    </div>
                    <div className="text-center">
                      <div className="text-3xl font-bold text-blue-600">{skinAnalysis.texture}%</div>
                      <div className="text-sm text-gray-600">Texture</div>
                    </div>
                  </div>

                  <div className="bg-white rounded-xl p-4">
                    <h4 className="font-semibold text-gray-800 mb-2">Key Concerns:</h4>
                    <ul className="space-y-1">
                      {skinAnalysis.concerns.map((concern, idx) => (
                        <li key={idx} className="text-gray-600 flex items-center gap-2">
                          <span className="w-2 h-2 bg-purple-400 rounded-full"></span>
                          {concern}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <button
                  onClick={() => setSkinAnalysis(null)}
                  className="w-full bg-gray-200 text-gray-700 py-3 rounded-full hover:bg-gray-300 transition-colors"
                >
                  Analyze Again
                </button>
              </div>
            )}
          </div>
        )}

        {/* Progress Tab */}
        {activeTab === 'progress' && (
          <div className="bg-white rounded-3xl shadow-lg p-6 animate-fadeIn">
            <div className="flex items-center gap-3 mb-6 pb-4 border-b">
              <TrendingUp className="w-6 h-6 text-purple-500" />
              <h2 className="text-2xl font-bold text-gray-800">Your Progress Journey</h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-6">
                <h3 className="font-semibold text-gray-800 mb-2">Current Hydration</h3>
                <div className="text-4xl font-bold text-blue-600">80%</div>
                <div className="text-sm text-gray-600 mt-2">↑ 15% from last month</div>
              </div>
              <div className="bg-gradient-to-br from-pink-50 to-pink-100 rounded-2xl p-6">
                <h3 className="font-semibold text-gray-800 mb-2">Skin Clarity</h3>
                <div className="text-4xl font-bold text-pink-600">85%</div>
                <div className="text-sm text-gray-600 mt-2">↑ 15% from last month</div>
              </div>
            </div>

            <div className="bg-gray-50 rounded-2xl p-6">
              <h3 className="font-semibold text-gray-800 mb-4">Progress Over Time</h3>
              <div className="space-y-3">
                {progressData.map((data, idx) => (
                  <div key={idx} className="flex items-center gap-4">
                    <div className="w-16 text-sm text-gray-600">{data.date}</div>
                    <div className="flex-1 flex gap-2">
                      <div className="flex-1">
                        <div className="bg-blue-200 rounded-full h-6 overflow-hidden">
                          <div 
                            className="bg-blue-500 h-full rounded-full transition-all"
                            style={{ width: `${data.hydration}%` }}
                          ></div>
                        </div>
                      </div>
                      <div className="flex-1">
                        <div className="bg-pink-200 rounded-full h-6 overflow-hidden">
                          <div 
                            className="bg-pink-500 h-full rounded-full transition-all"
                            style={{ width: `${data.clarity}%` }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              <div className="flex gap-4 mt-4 text-sm">
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 bg-blue-500 rounded"></div>
                  <span className="text-gray-600">Hydration</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 bg-pink-500 rounded"></div>
                  <span className="text-gray-600">Clarity</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default DermaTracker;




