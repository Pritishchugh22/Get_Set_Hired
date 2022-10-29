const selected = "#c9d8ff";
const unselected = "#f7f4f4";
var visibleDivId = 'projects0';

$(document).ready(function () {
    var elem = document.getElementById("projects0");
    elem.classList.remove("invisible");
    makeChanges();
});

function toggleVisibility(divId) {
    if (visibleDivId != divId) {
        var toHideElem = document.getElementById(visibleDivId);
        var toHideElemButton = document.getElementById(visibleDivId + "button");
        toHideElemButton.classList.remove('buttonSelected')
        toHideElem.classList.add('invisible');

        var toShowElem = document.getElementById(divId);
        var toShowElemButton = document.getElementById(divId + "button");
        toShowElemButton.classList.add('buttonSelected')
        toShowElem.classList.remove('invisible');

        visibleDivId = divId;
    }
}

function changeSize(className, size2, size1) {
    // size1 750
    // size2 1500

    // m = (size2 - size1)/750
    // c = size2 - m*1500

    // size = m*w + c
    var w, m, c;
    w = window.innerWidth;
    m = (size2 - size1) / 650;
    c = size2 - m * 1500;
    var elem = document.getElementsByClassName(className);
    for (var i = 0; i < elem.length; i++) {
        if (w > 1100)
            elem[i].style.fontSize = String(m * w + c) + "px";
        else
            elem[i].style.fontSize = String(m * 1100 + c) + "px";
    }
}

function changeHeight(className, size2, size1) {
    var w, m, c;
    w = window.innerWidth;
    m = (size2 - size1) / 650;
    c = size2 - m * 1500;
    var elem = document.getElementsByClassName(className);
    for (var i = 0; i < elem.length; i++) {
        if (w > 1100)
            elem[i].style.height = String(m * w + c) + "px";
        else
            elem[i].style.height = String(m * 1100 + c) + "px";
    }
}

function makeChanges() {
    changeSize('projectButtonTitle', 15, 10);
    changeSize('projectsNumbers', 20, 15);
    changeSize('cardDetails', 15, 10);
    changeSize('cardTitle', 20, 15);
    changeSize('project-card-title', 20, 15);
    changeSize('project-card-description', 18, 13);
    changeHeight('project-card-description', 56, 45);
}
window.onresize = makeChanges;

$(':radio').change(function() {
  console.log('New star rating: ' + this.value);
});