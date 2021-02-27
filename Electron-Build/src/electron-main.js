
const electron = require("electron")

//const fs = require("fs"); 

const app = electron.app;
const BrowserWindow = electron.BrowserWindow

let mainWindow 

app.on("ready", _ => {
    mainWindow = new BrowserWindow({
        height: 720,
        width: 1280,
    })

    //console.log("Hello")
    mainWindow.loadURL('file://' + __dirname + './view/index.html')

    // var python = require("child_process").spawn("python", ["./main.py"]);
    // python.stdout.on("data", function(data) {console.log(data.toString("utf8"))});
    
    mainWindow.on("closed", _ => {
        //console.log("closed!")
        mainWindow = null
    })
})