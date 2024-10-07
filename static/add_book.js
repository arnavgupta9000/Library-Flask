let page_btn = document.getElementById("page-by-page-button");
let once_btn =  document.getElementById("all-at-once-button");
let page = document.getElementById("page-by-page");
let once = document.getElementById("all-at-once");

page_btn.addEventListener("click", () => {
    page.style.display = 'block';
    once_btn.style.display = "block"
    page_btn.style.display = 'none';
    once.style.display = 'none';

})


document.getElementById("next_button1").addEventListener("click", () => {
    document.getElementById('form1').style.display = 'none'; // hide the first form
    document.getElementById('form2').style.display = 'block'; // show the second form
    document.getElementById("form-display").style.display = 'block';
})


let currentPage = 0;
let pageInputsContainer = document.getElementById('pageInputs');
let setPagesButton = document.getElementById('setPagesButton');
let nextPageButton = document.getElementById('nextPageButton');


setPagesButton.addEventListener("click", () => {
    let numPages = parseInt(document.getElementById("numPages").value); // recieves value from the input, and converts it to an int (its orginally a string), careful of bad inputs
    //clear previous inputs
    pageInputsContainer.innerHTML = '';
    currentPage = 0;
    
    // Create a field for each type
    for (let i = 0; i < numPages; i ++) {
        let input = document.createElement('input'); // creates a new input field (in html)
        input.type = 'text';
        input.placeholder = `Page ${i+1}`; // notice the `` are used for us to input values directly in the string. its bascially the f"" from python
        input.style.display= "none"; // hide the input orginally 
        pageInputsContainer.appendChild(input); // part of DOM. -> basically allows u to create dynamically made websites. appending is how we control it
        // u can manipulate all children as a group or individually 
    }

    // show the first page input
    console.log(pageInputsContainer.children)

    if (pageInputsContainer.children.length > 0 ) { // we have at least 1 child 
        pageInputsContainer.children[currentPage].style.display='block'; // make the first input visible
        nextPageButton.style.display = 'block'; // show the next page button
    }

})

nextPageButton.addEventListener("click", () => {
    if (currentPage < pageInputsContainer.children.length) { // still have more things to load, each input = 1 page
        pageInputsContainer.children[currentPage].style.display = 'none'; // hide the current input field so the next one can take its place, finding the children at a specific pos hence the children[currentPage]
        currentPage++; 
    }

    // show the next page if it is available (notice its after the increment so no need to -1 anywhere)
    if (currentPage < pageInputsContainer.children.length) {
        pageInputsContainer.children[currentPage].style.display = 'block'; // show the new block

    } else {
        nextPageButton.style.display = 'none'; // hide the button we're done
    }
})

once_btn.addEventListener("click", () => {
    once.style.display = "block";
    page_btn.style.display = "block"
    once_btn.style.display = 'none';
    page.style.display = 'none';

})