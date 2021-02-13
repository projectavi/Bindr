function read_json(json_filepath){
    const fs = require("fs")
    return (JSON.parse(fs.readFileSync(json_filepath)))
}

function write_json(data, json_filepath){
    const fs = require("fs")
    fs.writeFileSync(json_filepath, JSON.stringify(data))
}