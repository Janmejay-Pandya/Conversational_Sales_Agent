import ReactMarkdown from "react-markdown";

export default function Message({ from, text, meta }) {
    const isUser = from === "user";
    return (
        <div className={`flex ${isUser ? "justify-end" : "justify-start"} my-2`}>
            <div className={`${isUser ? "bg-indigo-600 text-white" : "bg-white/90 text-gray-900"} max-w-[70%] p-3 rounded-2xl shadow`}>
                <div className="text-sm whitespace-pre-line">
                    {text}
                </div>
                {meta &&
                    <div className="text-xs text-gray-500 mt-1">
                        <ReactMarkdown>{JSON.stringify(meta)}</ReactMarkdown>
                    </div>}
            </div>
        </div>
    );
}
