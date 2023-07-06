function calculateDaysBetweenDates(begin, end) {
    var beginDate = new Date(begin);
    var endDate = new Date(end);
    var beginYear = beginDate.getFullYear();
    var endYear = endDate.getFullYear();
    var beginMonth = beginDate.getMonth();
    var endMonth = endDate.getMonth();
    var beginDay = beginDate.getDate();
    var endDay = endDate.getDate();
    var days = 0;
    if (beginYear == endYear) {
        if (beginMonth == endMonth) {
        days = endDay - beginDay;
        } else {
        days = daysInMonth(beginYear, beginMonth) - beginDay;
        for (var i = beginMonth + 1; i < endMonth; i++) {
            days += daysInMonth(beginYear, i);
        }
        days += endDay;
        }
    } else {
        days = daysInMonth(beginYear, beginMonth) - beginDay;
        for (var i = beginMonth + 1; i < 12; i++) {
        days += daysInMonth(beginYear, i);
        }
        for (var i = beginYear + 1; i < endYear; i++) {
        days += daysInYear(i);
        }
        for (var i = 0; i < endMonth; i++) {
        days += daysInMonth(endYear, i);
        }
        days += endDay;
    }
    return days;
}



// Express server on port 3000
app.listen(3000, () => {
    console.log("Server running on port 3000");
}
);

// Return the current time  
function getCurrentTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var time = hours + ":" + minutes + ":" + seconds;
    return time;
}