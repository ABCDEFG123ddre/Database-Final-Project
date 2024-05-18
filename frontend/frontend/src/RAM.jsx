import { useState } from 'react'
import 'vite/modulepreload-polyfill'
import Home from "./pages/Home_RAM"
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.scss'

const container = document.getElementById('ram_root');
const root = ReactDOM.createRoot(container);
root.render(<Home></Home>);
