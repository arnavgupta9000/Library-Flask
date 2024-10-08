let page_btn = document.getElementById("page-by-page-button");
let once_btn =  document.getElementById("all-at-once-button");
let page = document.getElementById("page-by-page");
let once = document.getElementById("all-at-once");

page_btn.addEventListener("click", () => {
    page.style.display = 'block';
    once_btn.style.display = "block"
    page_btn.style.display = 'none';
    once.style.display = 'none';

});


document.getElementById("next_button1").addEventListener("click", () => {
    document.getElementById('form1').style.display = 'none'; // hide the first form
    document.getElementById('form2').style.display = 'block'; // show the second form
    document.getElementById("form-display").style.display = 'block';
});


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

});

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
});

once_btn.addEventListener("click", () => {
    once.style.display = "block";
    page_btn.style.display = "block"
    once_btn.style.display = 'none';
    page.style.display = 'none';

});

document.getElementById("next_button2").addEventListener("click", () => {
    // check if all fields are filled
    let required_fields = document.querySelectorAll('#all-at-once-first-form [required]') // query selector get ALL  elements with matching query. returns a NODELIST
    // '#all-at-once-first-form ->This part of the selector targets the element with the ID all-at-once-first-form
    //[required]: This part is an attribute selector. It selects any element that has the required attribute. 
    //Definition: Attributes are additional information provided within an HTML element that describe the element's properties or behavior.


    // The space between #all-at-once-first-form and [required] indicates a descendant selector. This means it will select all elements that have the required attribute that are descendants of the element with the ID all-at-once-first-form. ie The selector A B selects all elements of type B that are descendants (children, grandchildren, etc.) of any A element.

    // In the selector #all-at-once-first-form [required], you are combining an ID selector with an attribute selector.
    // #all-at-once-first-form selects the element with that ID. It could be a <div>, <form>, or any other element.
    // The space after it indicates that you want to find elements inside (descendants of) this element that match the [required] attribute condition.



    let all_filled = true;
    required_fields.forEach(function(field) { // for each is just for each element, function(field) { ... } is an anonymous function (a function without a name) that is called for each element in the required_fields NodeList
        //Each element from the required_fields NodeList is passed to this function as the field parameter, which represents the current element being processed in the loop.

        // the 2 lines below also work instead of using the function but the function is cleaner and more convenient 
        // for (let i = 0; i < required_fields.length; i++) {
        //let field = required_fields[i]; // Accessing the element by index

        if (!field.value) {
            all_filled = false;
            field.classList.add('error');
        } else {
            field.classList.remove('error');
        } 
        
    });

    if (all_filled) {
        document.getElementById("all-at-once-first-form").style.display="none";
        document.getElementById("all-at-once-content").style.display='block';
    }

});