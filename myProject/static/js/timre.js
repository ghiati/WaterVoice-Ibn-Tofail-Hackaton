// Function to calculate the next Sunday at 12:00 PM (noon)
function getNextSundayAtNoon() {
    const now = new Date();
    const nextSunday = new Date(now);
    
    // Set next Sunday to 12:00 PM
    nextSunday.setDate(now.getDate() + (7 - now.getDay())); // next Sunday
    nextSunday.setHours(12, 0, 0, 0); // Set time to 12:00 PM
    
    // If today is Sunday and it's already past 12:00 PM, move to the next Sunday
    if (now.getDay() === 0 && now.getHours() >= 12) {
        nextSunday.setDate(nextSunday.getDate() + 7);
    }
    
    return nextSunday;
}

// Function to format the remaining time in HH:MM:SS format
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
    return `${pad(hours)}:${pad(minutes)}:${pad(remainingSeconds)}`;
}

// Function to add a leading zero for single-digit numbers
function pad(number) {
    return number < 10 ? `0${number}` : number;
}

// Function to update the countdown timer
function updateTimer() {
    const now = new Date();
    const nextSunday = getNextSundayAtNoon();
    const remainingTime = nextSunday - now; // Time difference in milliseconds

    // If time remaining is greater than 0, update the countdown
    if (remainingTime > 0) {
        const remainingSeconds = Math.floor(remainingTime / 1000); // Convert to seconds
        document.getElementById('timer').innerText = formatTime(remainingSeconds);
    } else {
        document.getElementById('timer').innerText = "00:00:00"; // Countdown complete
    }
}

// Initial call to update the timer immediately
updateTimer();

// Update the timer every second
setInterval(updateTimer, 1000);
