import React, { useState } from "react";
import ProductList from "./components/ProductList";
import Cart from "./components/Cart";

function App() {
  const [cart, setCart] = useState([]);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Mini E-commerce Catalog</h1>
      <ProductList cart={cart} setCart={setCart} />
      <Cart cart={cart} />
    </div>
  );
}

export default App;