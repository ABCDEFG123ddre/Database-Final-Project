import { useState } from 'react'
import 'vite/modulepreload-polyfill'
import Home from "./pages/Home_HDD"
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.scss'

const container = document.getElementById('hdd_root');
const root = ReactDOM.createRoot(container);
root.render(<Home></Home>);
