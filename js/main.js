var pastIndex = 1;
showPast(pastIndex);

var aboutIndex = 1;

function movement(x) {
    showPast(pastIndex += x);
    showAbout(aboutIndex = x);
}

function showPast(x) {
    var y;
    var content = document.getElementsByClassName('pastEventDiv');
    // resets index to 1 if it goes past the content length (15)
    if (x > content.length) {
    	pastIndex = 1
    }
    // sets index to content length (15) if it goes under value of 1
    if (x < 1) {
    	pastIndex = content.length
    }
    // hides previous div content
    for (y = 0; y < content.length; y++) {
    	content[y].style.display = "none";
    }
    // shows current index div
    content[pastIndex-1].style.display = "block";
}

function reset() {
    click = document.getElementById('clickA');
    click.style.display = "none";
    box = document.getElementById('conOneSub');
    box.style.display = "none";
}

function showAbout(x) {
    reset();
    var y;
    var content = document.getElementsByClassName('aboutButtonContent');
    for (y = 0; y < content.length; y++) {
    	content[y].style.display = "none";
    }
    content[aboutIndex].style.display = "block";
}



