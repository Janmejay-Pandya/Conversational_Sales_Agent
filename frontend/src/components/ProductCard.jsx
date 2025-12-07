export default function ProductCard({ product, onAction }) {
    return (
        <div className="border rounded-lg p-3 w-64 shadow-sm bg-white">
            <div className="h-36 bg-gray-100 rounded mb-2 flex items-center justify-center text-sm text-gray-500">Image</div>
            <h3 className="font-semibold">{product.name}</h3>
            <p className="text-sm text-gray-600">{product.brand} · {product.category}</p>
            <div className="mt-2 flex items-center justify-between">
                <span className="font-bold">₹{product.price}</span>
                <button onClick={() => onAction("reserve", product)} className="px-3 py-1 bg-indigo-600 text-white rounded">Reserve</button>
            </div>
        </div>
    );
}
