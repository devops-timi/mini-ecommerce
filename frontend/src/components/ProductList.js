import React, { useEffect, useState } from "react";
import axios from "axios";

function ProductList({ cart, setCart }) {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/products")
      .then(res => setProducts(res.data))
      .catch(err => console.error(err));
  }, []);

  const addToCart = (product) => {
    const quantity = 1;
    axios.post("http://localhost:5000/cart", {
      user_id: 1,
      product_id: product.id,
      quantity
    }).then(res => {
      alert(`Added ${product.name} to cart`);
      setCart([...cart, { ...product, quantity }]);
    }).catch(err => alert(err.response.data.error));
  };

  return (
    <div>
      <h2>Products</h2>
      {products.map(p => (
        <div key={p.id} style={{ border: "1px solid #ccc", margin: "5px", padding: "5px" }}>
          <h3>{p.name}</h3>
          <p>{p.description}</p>
          <p>Price: ${p.price}</p>
          <p>Stock: {p.stock}</p>
          <button onClick={() => addToCart(p)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

export default ProductList;