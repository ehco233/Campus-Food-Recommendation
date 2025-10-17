// Vercel Serverless Function for Deepseek API
// This hides the API key from the frontend

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  // Handle OPTIONS request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Get API Key from environment variable
  const API_KEY = process.env.DEEPSEEK_API_KEY;

  if (!API_KEY) {
    return res.status(500).json({ 
      error: 'API key not configured',
      message: 'Please set DEEPSEEK_API_KEY in environment variables'
    });
  }

  try {
    const { messages, temperature, max_tokens } = req.body;

    // Validate request body
    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ 
        error: 'Invalid request',
        message: 'messages array is required'
      });
    }

    console.log('Calling Deepseek API...');

    // Call Deepseek API
    const response = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`
      },
      body: JSON.stringify({
        model: 'deepseek-chat',
        messages: messages,
        temperature: temperature || 0.7,
        max_tokens: max_tokens || 2000
      })
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Deepseek API error:', response.status, errorText);
      throw new Error(`Deepseek API error: ${response.status}`);
    }

    const data = await response.json();
    
    console.log('Deepseek API success');

    // Return the result
    return res.status(200).json(data);

  } catch (error) {
    console.error('Error in deepseek function:', error);
    return res.status(500).json({ 
      error: 'Failed to generate report',
      message: error.message 
    });
  }
}

