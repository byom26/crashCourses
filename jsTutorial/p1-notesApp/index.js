showNotes();
// If user adds a note, add it to the local storage
let addBtn = document.getElementById('addBtn');
addBtn.addEventListener("click", function (e) {
    let addTxt = document.getElementById("addTxt");
    let addTitle = document.getElementById("addTitle");
    let notes = localStorage.getItem("notes");
    let titles = localStorage.getItem("titles");

    if (addTxt.value != "" && addTitle.value != "") {
        //console.log(addTxt.value)
        if (notes == null) {
            notesObj = [];
            titlesObj = [];
        }
        else {
            notesObj = JSON.parse(notes);
            titlesObj = JSON.parse(titles);
        }

        notesObj.push(addTxt.value);
        titlesObj.push(addTitle.value);
        localStorage.setItem("notes", JSON.stringify(notesObj));
        localStorage.setItem("titles", JSON.stringify(titlesObj));
        addTxt.value = "";
        addTitle.value = "";
        //console.log(notesObj);

        showNotes();
    }
    else {
        let bodyElem = document.getElementById("nav");
        let alertHtml = `
            <div class="alert alert-info alert-dismissible fade show" role="alert">
                <strong>Empty Note Title / Description!</strong> Please insert some text to save the note.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>`;
        bodyElem.insertAdjacentHTML('afterend', alertHtml)
    }
})

// Function to show elements from the loal storage
function showNotes() {
    let notes = localStorage.getItem("notes")
    let titles = localStorage.getItem("titles")
    if (notes == null) {
        notesObj = [];
        titlesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
        titlesObj = JSON.parse(titles);
    }

    let html = "";
    notesObj.forEach(function (element, index) {
        const titleVal = titlesObj[index];
        html += `
            <div class="noteCard mx-2 my-2" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">${titleVal}</h5>
                    <p class="card-text">${element}</p>
                    <button id="${index}"  onclick="deleteNote(this.id)" class="btn btn-primary">Delete Note</button>
                </div>
            </div>`;
    });
    let notesElem = document.getElementById("noteDiv");
    if (notesObj.length != 0) {
        notesElem.innerHTML = html;
    }
    else {
        notesElem.innerHTML = `Nothing to show!`;
    }
}

// Function to delete a note
function deleteNote(index) {
    //console.log("I am deleting", index);
    let notes = localStorage.getItem("notes")
    let titles = localStorage.getItem("titles")
    if (notes == null) {
        notesObj = [];
        itemsObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
        itemsObj = JSON.parse(titles);
    }
    notesObj.splice(index, 1);
    itemsObj.splice(index, 1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    localStorage.setItem("items", JSON.stringify(itemsObj));
    showNotes();
}

let search = document.getElementById("searchTxt");
search.addEventListener("input", function () {
    let inputVal = search.value.toLowerCase();
    //console.log("Input event fired!", inputVal);
    let noteCards = document.getElementsByClassName("noteCard");
    Array.from(noteCards).forEach(function (element) {
        let cardText = element.getElementsByTagName("p")[0].innerText.toLowerCase();
        if (cardText.includes(inputVal)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    });
});