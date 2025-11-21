const varSunrise   = document.getElementById('sunrise-val');
const varSunset    = document.getElementById('sunset-val');
const varWind      = document.getElementById('wind-val');
const varHumidity  = document.getElementById('humidity-val');
const varPressure  = document.getElementById('pressure-val');
const varUV        = document.getElementById('uv-val');
const varVisibility= document.getElementById('visibility-val');
const varAir       = document.getElementById('air-val');
const varTodayTemp = document.getElementById('today-temp-val');
const varTodayIcon = document.getElementById('today-icon');
const varTodayDate = document.getElementById('today-date-val');
varTodayDate.textContent  = formatDateLong();

var xhr = new XMLHttpRequest();
xhr.open('GET', '/data/weather.json');
xhr.onload = function () {
  if (xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);

    varSunrise.textContent    = data.current.sunrise;
    varSunset.textContent     = data.current.sunset;
    varWind.textContent       = data.current.wind_speed + ' m/s';
    varHumidity.textContent   = data.current.humidity + '%';
    varPressure.textContent   = data.current.pressure + ' hPa';
    const uv                  = data.current.uvi;
    varVisibility.textContent = (data.current.visibility / 1000).toFixed(1) + ' km';
    const aq                  = data.current.air_quality;
    varTodayTemp.innerHTML    = Math.round(data.current.temp_c) + '&deg;C';
    varTodayIcon.src          = "assets/icons/" + data.current.weather[0].icon + ".png";
    if (aq === 1) {
      (varAir.textContent = "Good");
    } else if (aq === 2) {
      (varAir.textContent = "Fair");
    } else if (aq === 3) {
      (varAir.textContent = "Moderate");
    } else if (aq === 4) {
      (varAir.textContent = "Poor");
    } else {
      (varAir.textContent = "Very Poor");
    }
    if (uv < 3) {
      (varUV.textContent = "Low");
    } else if (uv >= 3 && uv < 6) {
      (varUV.textContent = "Moderate");
    } else if (uv >= 6 && uv < 8) {
      (varUV.textContent = "High");
    } else if (uv >=8 && uv < 11) {
      (varUV.textContent = "Very High");
    } else {
      (varUV.textContent = "Extreme");
    }

    const varBoxes = document.querySelectorAll('.forecast-item');
    for (let i = 0; i < 7; i++) {
      let varDayData = data.daily[i];
      let varBox = varBoxes[i];

      varBox.querySelector('.forecast-day').textContent = varDayData.day;
      varBox.querySelector('.forecast-icon').src = "assets/icons/" + varDayData.icon + ".png";
      varBox.querySelector('.forecast-temp').innerHTML = Math.round(varDayData.temp_max) + '&deg;C';
    }
  }
};
xhr.send();

function formatDateLong() {
    const fullDays = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    ];

    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    const today = new Date();

    const dayName = fullDays[today.getDay()];
    const monthName = months[today.getMonth()];
    const dayNum = today.getDate();
    const year = today.getFullYear();

    // Add "st", "nd", "rd", "th"
    function ordinal(n) {
        if (n > 3 && n < 21) return n + "th";
        switch (n % 10) {
            case 1: return n + "st";
            case 2: return n + "nd";
            case 3: return n + "rd";
            default: return n + "th";
        }
    }

    const formatted = `${dayName} ${ordinal(dayNum)} ${monthName} ${year}`;
    return formatted;
}