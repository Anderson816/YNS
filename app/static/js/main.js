// File: app/static/js/main.js

document.addEventListener("DOMContentLoaded", () => { const pan = document.getElementById('pan'); const aadhaar = document.getElementById('aadhaar'); const form = document.querySelector("form"); if (pan && aadhaar && form) { form.addEventListener("submit", (e) => { if (!pan.value.trim() || !aadhaar.value.trim()) { e.preventDefault(); alert("Please fill both PAN and Aadhaar details to proceed."); } }); } });

