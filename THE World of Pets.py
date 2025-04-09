// The World of Pets - Full eCommerce App with Admin Panel, Product Categories, Online & COD Options

import React, { useState } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Input } from "@/components/ui/input"; import { Select, SelectItem } from "@/components/ui/select"; import { motion } from "framer-motion";

const initialProducts = [ { id: 1, name: "Dog Food (5kg)", price: 799, category: "Dog", image: "https://via.placeholder.com/150" }, { id: 2, name: "Cat Toy Set", price: 299, category: "Cat", image: "https://via.placeholder.com/150" }, ];

export default function WorldOfPetsStore() { const [products, setProducts] = useState(initialProducts); const [cart, setCart] = useState([]); const [adminMode, setAdminMode] = useState(false); const [newProduct, setNewProduct] = useState({ name: "", price: "", category: "Dog", image: "" }); const [paymentMethod, setPaymentMethod] = useState("COD");

const addToCart = (product) => { setCart([...cart, product]); };

const addProduct = () => { const id = products.length + 1; setProducts([...products, { ...newProduct, id, price: parseFloat(newProduct.price) }]); setNewProduct({ name: "", price: "", category: "Dog", image: "" }); };

const subtotal = cart.reduce((sum, item) => sum + item.price, 0);

return ( <div className="p-4 grid grid-cols-1 md:grid-cols-2 gap-4"> <div className="col-span-full flex justify-between items-center"> <h1 className="text-2xl font-bold">The World of Pets</h1> <Button onClick={() => setAdminMode(!adminMode)}> {adminMode ? "Switch to Shop View" : "Admin Panel"} </Button> </div>

{adminMode ? (
    <Card className="col-span-full">
      <CardContent className="p-4 space-y-2">
        <h2 className="text-xl font-bold mb-2">Add New Product</h2>
        <Input placeholder="Product Name" value={newProduct.name} onChange={(e) => setNewProduct({ ...newProduct, name: e.target.value })} />
        <Input placeholder="Price" type="number" value={newProduct.price} onChange={(e) => setNewProduct({ ...newProduct, price: e.target.value })} />
        <Select value={newProduct.category} onValueChange={(value) => setNewProduct({ ...newProduct, category: value })}>
          <SelectItem value="Dog">Dog</SelectItem>
          <SelectItem value="Cat">Cat</SelectItem>
        </Select>
        <Input placeholder="Image URL" value={newProduct.image} onChange={(e) => setNewProduct({ ...newProduct, image: e.target.value })} />
        <Button onClick={addProduct}>Add Product</Button>
      </CardContent>
    </Card>
  ) : (
    products.map((product) => (
      <motion.div key={product.id} whileHover={{ scale: 1.05 }}>
        <Card>
          <CardContent className="p-4">
            <img src={product.image} alt={product.name} className="mb-2 rounded-xl" />
            <h3 className="text-lg font-semibold">{product.name}</h3>
            <p className="text-sm text-gray-600">Category: {product.category}</p>
            <p className="text-sm text-gray-600 mb-2">₹{product.price}</p>
            <Button onClick={() => addToCart(product)}>Add to Cart</Button>
          </CardContent>
        </Card>
      </motion.div>
    ))
  )}

  {!adminMode && (
    <Card className="col-span-full">
      <CardContent className="p-4">
        <h2 className="text-xl font-bold mb-2">Your Cart</h2>
        {cart.map((item, index) => (
          <p key={index} className="text-sm">{item.name} - ₹{item.price}</p>
        ))}
        <p className="mt-2 font-semibold">Total: ₹{subtotal}</p>

        <Select value={paymentMethod} onValueChange={setPaymentMethod} className="my-2">
          <SelectItem value="COD">Cash on Delivery</SelectItem>
          <SelectItem value="Online">Online Payment</SelectItem>
        </Select>

        {paymentMethod === "COD" ? (
          <a
            href={`https://wa.me/919653193811?text=I%20want%20to%20order:%20${cart
              .map((item) => item.name)
              .join(",%20")}%20Total:%20₹${subtotal}%20Payment:%20Cash%20on%20Delivery`}
            target="_blank"
            rel="noopener noreferrer"
          >
            <Button className="mt-2">Order on WhatsApp (COD)</Button>
          </a>
        ) : (
          <Button className="mt-2" onClick={() => alert("Redirecting to payment gateway...")}>Pay Online</Button>
        )}
      </CardContent>
    </Card>
  )}
</div>

); }
