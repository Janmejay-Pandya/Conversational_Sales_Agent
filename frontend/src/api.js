import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function startSession(customerId) {
  const res = await axios.post(`${API_BASE}/chat/start`, { customer_id: customerId });
  return res.data; // { session_id: ... }
}

export async function sendMessage(sessionId, text) {
  const res = await axios.post(`${API_BASE}/chat/${sessionId}/message`, { text });
  return res.data; // { reply: "...", products: [...] }
}
