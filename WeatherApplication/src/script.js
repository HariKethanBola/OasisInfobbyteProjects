const API_KEY = "db0356c83fbf11ce473bf4ff509b5316";
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

async function getWeather(city, units="metric") {
  const url = `${BASE_URL}?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=${units}`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status} — ${res.statusText}`);
  }
  return res.json();
}

function formatReport(data) {
  const name = data.name ?? "?";
  const main = data.main ?? {};
  const desc = (data.weather && data.weather[0]?.description) ? data.weather[0].description : "N/A";
  return [
    `City: ${name}`,
    `Temp: ${main.temp}°`,
    `Humidity: ${main.humidity}%`,
    `Conditions: ${desc.charAt(0).toUpperCase() + desc.slice(1)}`
  ].join("\n");
}

async function showWeather(city, units) {
  const result = document.getElementById("result");
  result.textContent = "Loading...";
  try {
    const data = await getWeather(city, units);
    result.textContent = formatReport(data);
  } catch (err) {
    result.textContent = "Error: " + err.message;
  }
}

document.getElementById("weatherForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const city = document.getElementById("city").value.trim();
  const units = document.getElementById("units").value;
  showWeather(city, units);
});

// Default city on load

