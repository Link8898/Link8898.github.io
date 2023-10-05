let blockValue = 0;
let updateRate = 300;
        
function IncreaseValue(event) {
    blockValue += 1;
    SaveData();
}
        
function RenderBlock() {
    document.getElementById("Block").textContent = String(blockValue);
}

function InterpretData(data) { // Interpret the loaded data
    blockValue = parseInt(data["BlockValue"]);
    RenderBlock();
}

function init() {
    window.updateLoop = setInterval(LoadData, updateRate); // Render any changes every 3 seconds
    document.getElementById("Block").addEventListener("click", IncreaseValue);
}
function StopUpdateLoop() {
    clearInterval(updateLoop);
}

async function SaveData() { // Only called when we want to globally update our variables
    await fetch("/api", {
        method:"POST", // Using the post method to send data
        headers:{
            "Content-type": "application/json" // Convert to data so backend can read it
        },
        body:JSON.stringify({"BlockValue":blockValue}) // The body is the data we are sending to the server
    });
}

async function LoadData() { // Called every interval to see if save data has changed
    // Only the 'data.txt' is necessary. The rest lets you know the root of the file
    loadedData = null;
    await fetch("/load",{
        method:"GET",
        headers:{
            "Content-type":"application/json"
        }
        }).then((r)=>r.json()).then((response)=>loadedData = response);
    InterpretData(loadedData);
}

window.addEventListener("keydown", StopUpdateLoop);
window.onload = init;