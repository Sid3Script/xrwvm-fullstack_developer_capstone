import React from 'react';
import { Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header";
import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer";
import PostReview from "./components/Dealers/PostReview";

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/dealers" element={<Dealers />} />
        <Route path="/dealer/:id" element={<Dealer />} />
        <Route path="/postreview/:id" element={<PostReview />} />
      </Routes>
    </div>
  );
}

export default App;