// Function to initialize the dropdowns with provided values
function initializeDropdowns() {
    const cutValues = ["FAIR", "GOOD", "IDEAL", "PREMIUM", "VERY GOOD"];
    const colorValues = ["J", "I", "H", "G", "F", "E", "D"];
    const clarityValues = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"];

    initializeDropdown('cut', cutValues);
    initializeDropdown('color', colorValues);
    initializeDropdown('clarity', clarityValues);
}

// Function to populate a dropdown with options
function initializeDropdown(dropdownId, values) {
    const dropdown = document.getElementById(dropdownId);

    values.forEach(value => {
        const option = document.createElement('option');
        option.value = value;
        option.text = value;
        dropdown.appendChild(option);
    });
}

// Call the initialization function when the page loads
document.addEventListener('DOMContentLoaded', function () {
    initializeDropdowns();
});

// Function to make the prediction request
async function predictPrice() {
    const form = document.getElementById('predictionForm');
    const formData = new FormData(form);

    try {
        const response = await fetch('http://127.0.0.1:8000/predict_price', {
            //const response = await fetch('/api/predict_price', { //using nginx
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            displayResult(result.predicted_price);
        } else {
            console.error('Error from server:', result.error);
            displayResult('Error during prediction');
        }
    } catch (error) {
        console.error('Network error:', error);
        displayResult('Error during prediction');
    }
}

// Open the Diamond Features modal

function showDiamondFeatures() {
    // Set the source of the diamond image with an absolute path
    //document.getElementById("diamondImage").src = "Diamond.jpeg";
    
    // Display the Diamond Features modal
    document.getElementById("diamondFeaturesModal").style.display = "block";
}

// Close the Diamond Features modal
function closeDiamondFeaturesModal() {
    document.getElementById("diamondFeaturesModal").style.display = "none";
}

// Close the Diamond Features modal if the user clicks outside the modal
window.onclick = function(event) {
    if (event.target == document.getElementById("diamondFeaturesModal")) {
        closeDiamondFeaturesModal();
    }
};

// Function to display the prediction result
function displayResult(result) {
    const resultDiv = document.getElementById('result');
    const resultContainer = document.getElementById('result-container');

    // Update the content and show the result container
    resultDiv.innerText = `Predicted Price: ${result}`;
    resultContainer.style.display = 'block';
}
