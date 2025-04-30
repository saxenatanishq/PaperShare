let question_count = 0;

function add_question(){
    question_count++;
    const questionDiv = document.createElement('div');
    questionDiv.className = "question";
    questionDiv.innerHTML = `
        <strong>Question ${question_count}</strong>
        <div class="subpart-controls">
            <input type="number" class="subpartNumber" placeholder="No. of subparts">
            <button onclick="addSubpart(this)">Add subparts</button>
        </div>
        <input type="number" placeholder="Marks" class="marks">
        <div class="subpartsContainer"></div>
      `;
    document.getElementById('questions_container').appendChild(questionDiv);
}

function addSubpart(button){
    console.log(`Function called and the button is ${button}`)
    const subpartsContainer = button.parentElement.nextElementSibling.nextElementSibling;
    const marksInput = button.parentElement.nextElementSibling;
    const number = button.previousElementSibling.value;
    button.previousElementSibling.value = null;
    if (number <= 1){
        alert("Please enter more than 1 subparts")
    }else{
        marksInput.style.display = "none";
        marksInput.value = null;
        subpartsContainer.innerHTML = "";
        for (let i = 0; i < number; i++) {
            const subpartDiv = document.createElement('div');
            subpartDiv.className = 'subpart';
            subpartDiv.innerHTML = `
                Subpart ${i + 1}
                <div class="subpart-controls">
                    <input type="number" class="subpartNumber" placeholder="No. of subparts">
                    <button onclick="addSubpart(this)">Add subparts</button>
                </div>
                <input type="number" placeholder="Marks" class="marks">
                <div class="subpartsContainer"></div>
            `;
            subpartsContainer.appendChild(subpartDiv);
        }
    }
}

function makeStructure(container){
    const elements = container.children;
    let structure = [];
    for (let element of elements){
        let marksValue = element.querySelector(".marks").value;
        let subElements = element.querySelector(".subpartsContainer").children
        if (marksValue.trim() !== ""){
            structure.push(Number(marksValue));
        }else if (subElements.length !== 0){
            structure.push(makeStructure(element.querySelector(".subpartsContainer")));
        }else{
            alert("Please enter the marks of all subparts");
            return [];
        }
    }
    return structure
}

function submitStructure(){
    const container = document.querySelector('#questions_container');
    structure = makeStructure(container);
    return structure
}

function handleForm() {
    let structure = submitStructure();
    console.log(structure)
    if (structure.length === 0) {
        alert("Please complete the question structure before submitting.");
        return false;
    }
    const fileInput = document.getElementById('id_pdf_file');
    if (!fileInput.value) {
        alert("Please select a file to upload.");
        return false;
    }
    document.getElementById('id_questions').value = JSON.stringify(structure);
    question_count = 0
    return true;
}

