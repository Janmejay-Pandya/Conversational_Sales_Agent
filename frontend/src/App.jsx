import { useEffect, useState, useRef } from "react";
import { startSession, sendMessage } from "./api";
import Message from "./components/Message";
import ProductCard from "./components/ProductCard";

function App() {
  const [sessionId, setSessionId] = useState("");
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [products, setProducts] = useState([]);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    // start a demo session as guest (you could pass customer id)
    async function init() {
      try {
        const res = await startSession("cust_001"); // use a seeded customer id
        setSessionId(res.session_id || res.sessionId || "demo-session");

        // initial system/greeting from backend can be appended
        setMessages([
          { from: "bot", text: "Hi! I’m your Sales Agent. How can I help today?" },
        ]);
      } catch (err) {
        console.error("Error starting session:", err);
      }
    }
    init();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, products]);

  async function handleSend(e) {
    e?.preventDefault();
    if (!input.trim()) return;

    const text = input.trim();

    // add user message
    setMessages((msgs) => [...msgs, { from: "user", text }]);
    setInput("");

    try {
      const res = await sendMessage(sessionId, text);
      // expected response: { reply: "text", products: [ ... ] }

      if (res.reply) {
        setMessages((msgs) => [...msgs, { from: "bot", text: res.reply }]);
      }

      // always set products; if none, clear the old ones
      setProducts(res.products || []);
    } catch (err) {
      console.error("Error sending message:", err);
      setMessages((msgs) => [
        ...msgs,
        { from: "bot", text: "Sorry — something went wrong talking to the backend." },
      ]);
    }
  }

  function handleProductAction(action, product) {
    // quick client-side demo: send a special message to backend to reserve
    setMessages((m) => [
      ...m,
      { from: "user", text: `Please ${action} ${product.sku}` },
    ]);

    // For now simulate reservation response
    setTimeout(() => {
      setMessages((m) => [
        ...m,
        {
          from: "bot",
          text: `Okay — reserved ${product.name} for you at your preferred store.`,
        },
      ]);
    }, 600);
  }

  return (
    <div className="min-h-screen bg-slate-50 p-6">
      <div className="max-w-4xl mx-auto bg-white rounded-2xl shadow p-6">
        <div className="flex items-center justify-between mb-4">
          <h1 className="text-xl font-bold">OmniSales — Chat Demo</h1>
          <div className="text-sm text-gray-500">Session: {sessionId}</div>
        </div>

        <div className="border rounded-lg p-4 h-[60vh] overflow-auto bg-gray-50">
          {messages.map((m, idx) => (
            <Message key={idx} from={m.from} text={m.text} meta={m.meta} />
          ))}
          <div ref={messagesEndRef} />
        </div>

        {products.length > 0 && (
          <div className="mt-4">
            <h2 className="font-semibold mb-2">Recommendations</h2>
            <div className="flex gap-3 overflow-x-auto pb-3">
              {products.map((p) => (
                <ProductCard
                  key={p.sku}
                  product={p}
                  onAction={handleProductAction}
                />
              ))}
            </div>
          </div>
        )}

        <form onSubmit={handleSend} className="mt-4 flex gap-2">
          <input
            className="flex-1 border rounded px-4 py-2"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type message (e.g., 'I need running shoes')"
          />
          <button
            className="px-4 py-2 bg-indigo-600 text-white rounded"
            type="submit"
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
