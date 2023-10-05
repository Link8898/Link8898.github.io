// Packages
const express = require("express");
const fs = require('fs');

// Application creation
const app = express();
const PORT = process.env.PORT || 8080; // Use domain port, otherwise localhost port
app.listen(PORT, '0.0.0.0');
app.use(express.json()); // Allows for json interpretation
app.use(express.static(__dirname)); // Allows external css and js files

// Get allows us to get the page we want (We are displaying the html page from backend)
app.get("/netTest", (req, res) => {
    res.sendFile("index.html", {root: __dirname}); // Specify where this html file is located
});

// Handles the post method from the front end
app.post("/api", (req, res) => {
    const sentData = req.body
    const data = JSON.parse(fs.readFileSync("saveData.json"));
    
    returnedData = Object.assign({}, data, sentData);

    fs.writeFileSync("saveData.json", JSON.stringify(returnedData));
    res.end(); // End request by sending nothing
});

//  Handles the get method from the front end
app.get("/load", (req, res) => {
    res.send(JSON.parse(fs.readFileSync("saveData.json"))); // Send data back
});