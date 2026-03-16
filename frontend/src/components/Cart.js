import React from "react";

function Cart({ cart }) {
  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Cart</h2>
      {cart.length === 0 ? <p>Cart is empty</p> : (
        <ul>
          {cart.map((item, idx) => (
            <li key={idx}>{item.name} x {item.quantity} = ${item.price * item.quantity}</li>
          ))}
        </ul>
      )}
      <h3>Total: ${total}</h3>
    </div>
  );
}

export default Cart;