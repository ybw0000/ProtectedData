"use strict";

// Add onclick for revert value button in 9 BLOCK - CHOOSE
const getDataInParagraph = document.querySelector("#container");

function pressIndividualButton() {
    getDataInParagraph.innerHTML = "An individual plan costs $ 0.00. Productive use.";
}

function pressCompanyButton() {
    getDataInParagraph.innerHTML = "The plan for private companies costs $ 5.00. Productive use.";
}