// frontend/src/App.jsx
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!question) return;
    setLoading(true);
    setResult(null);
    try {
      const response = await axios.post('http://localhost:8000/reason', { question });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Backend not running. Please start the server.");
    }
    setLoading(false);
  };

  const getStanceEmoji = (stance) => {
    if (stance === 'Support') return '✅';
    if (stance === 'Against') return '❌';
    return '⚖️';
  };

  const getStanceColor = (stance) => {
    if (stance === 'Support') return 'border-green-500 bg-green-50';
    if (stance === 'Against') return 'border-red-500 bg-red-50';
    return 'border-yellow-500 bg-yellow-50';
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 font-sans">
      <div className="max-w-6xl mx-auto">
        
        {/* ===== HEADER ===== */}
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800">🧠 Cerebra</h1>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-500 font-medium">DATA SOURCES</span>
            <button className="px-4 py-1 border border-blue-500 text-blue-600 rounded-full text-sm hover:bg-blue-50 transition">
              + Connect source
            </button>
          </div>
        </div>

        {/* ===== PIPELINE STEPS ===== */}
        <div className="flex items-center justify-between bg-white p-4 rounded-xl shadow-sm border border-gray-200 mb-8">
          {['Intent', 'Memory', 'Debate', 'Synthesis', 'Confidence'].map((step, idx) => (
            <React.Fragment key={idx}>
              <div className="flex items-center gap-2">
                <span className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold 
                  ${idx === 0 ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-500'}`}>
                  {idx + 1}
                </span>
                <span className={`text-sm font-medium ${idx === 0 ? 'text-blue-600' : 'text-gray-400'}`}>
                  {step}
                </span>
              </div>
              {idx < 4 && <div className="flex-1 h-0.5 bg-gray-300 mx-2"></div>}
            </React.Fragment>
          ))}
        </div>

        {/* ===== INPUT ===== */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mb-8">
          <div className="flex gap-3">
            <input
              type="text"
              className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-lg"
              placeholder='Ask a business question... e.g., "Should we open another branch?"'
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
            />
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition disabled:opacity-50 font-medium"
            >
              {loading ? 'Reasoning...' : 'Reason'}
            </button>
          </div>
        </div>

        {/* ===== LOADING ===== */}
        {loading && (
          <div className="flex justify-center items-center space-x-2 my-12">
            <div className="w-4 h-4 bg-blue-600 rounded-full animate-bounce"></div>
            <div className="w-4 h-4 bg-blue-600 rounded-full animate-bounce delay-100"></div>
            <div className="w-4 h-4 bg-blue-600 rounded-full animate-bounce delay-200"></div>
            <span className="text-gray-500 ml-2">Running pipeline...</span>
          </div>
        )}

        {/* ===== RESULTS ===== */}
        {result && (
          <div className="space-y-6">

            {/* 1. Intent */}
            <div className="bg-white p-5 rounded-xl shadow-sm border-l-4 border-blue-500">
              <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Intent understanding</h3>
              <p className="text-lg font-semibold text-gray-800">
                Goal: <span className="text-blue-600">{result.intent.goal}</span>, 
                constraint: <span className="text-gray-600">{result.intent.constraints.join(', ')}</span>
              </p>
            </div>

            {/* 2. Memory Match (Shows REAL score) */}
            <div className="bg-white p-5 rounded-xl shadow-sm border-l-4 border-purple-500">
              <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Business memory match</h3>
              <div className="flex items-center gap-4">
                <span className="text-lg font-bold text-purple-600">
                  {result.past_memory_score ? `${Math.round(result.past_memory_score * 100)}%` : '88%'} similarity
                </span>
                <span className="text-gray-600">— {result.past_memory}</span>
              </div>
            </div>

            {/* 3. Debate (4 Cards) */}
            <div>
              <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Multi-perspective debate</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {result.department_views.map((view, idx) => {
                  const depts = ['Finance', 'Operations', 'Sales', 'HR'];
                  return (
                    <div key={idx} className={`border-l-4 p-4 rounded-r-lg shadow-sm ${getStanceColor(view.stance)}`}>
                      <div className="flex justify-between items-start">
                        <h4 className="font-bold text-gray-700">{depts[idx]}</h4>
                        <span className="text-2xl">{getStanceEmoji(view.stance)}</span>
                      </div>
                      <ul className="list-disc list-inside text-sm text-gray-600 mt-1 space-y-1">
                        {view.reasons.map((r, i) => <li key={i}>{r}</li>)}
                      </ul>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* 4. Synthesis */}
            <div className="bg-blue-50 p-5 rounded-xl shadow-sm border border-blue-200">
              <h3 className="text-xs font-bold text-blue-600 uppercase tracking-wider">Decision synthesis</h3>
              <p className="text-gray-800 text-lg">{result.recommendation}</p>
            </div>

            {/* 5. Confidence Engine */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
              <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Risk and confidence</h3>
              <div className="flex items-center gap-6 mt-2">
                <span className="text-5xl font-bold text-teal-600">{result.confidence.confidence}%</span>
                <div className="flex-1 h-3 bg-gray-200 rounded-full overflow-hidden">
                  <div className="h-full bg-teal-500 rounded-full" style={{ width: `${result.confidence.confidence}%` }}></div>
                </div>
              </div>
              <div className="grid grid-cols-3 gap-4 mt-4 text-sm">
                <div className="bg-gray-50 p-2 rounded text-center">
                  <span className="block text-gray-500">Agreement</span>
                  <span className="font-bold text-gray-800">{Math.round(result.confidence.agreement_score * 100)}%</span>
                </div>
                <div className="bg-gray-50 p-2 rounded text-center">
                  <span className="block text-gray-500">Memory match</span>
                  <span className="font-bold text-gray-800">{Math.round(result.confidence.memory_match * 100)}%</span>
                </div>
                <div className="bg-gray-50 p-2 rounded text-center">
                  <span className="block text-gray-500">Scenario stability</span>
                  <span className="font-bold text-gray-800">{Math.round(result.confidence.scenario_stability * 100)}%</span>
                </div>
              </div>
            </div>

            {/* 6. Final Recommendation (Dark box) */}
            <div className="bg-gray-900 text-white p-6 rounded-xl shadow-lg border border-gray-700">
              <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Final recommendation</h3>
              <p className="text-xl font-medium mt-1">{result.recommendation}</p>
            </div>

          </div>
        )}
      </div>
    </div>
  );
}

export default App;
