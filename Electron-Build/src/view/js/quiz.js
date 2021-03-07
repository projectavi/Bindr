(function(){

    const fs = require("fs")
    const path = require('path');

    window.$ = window.jQuery = require('jquery');

    function run_python() {
      
    let {PythonShell} = require('python-shell')

    PythonShell.run("./src/model/engine/question_gen.py", null, function(err, results) {
        if (err) throw err;
        //console.log("main.py executed.")
        console.log("results: ", results)
    })
      

     //var spawn = require('child_process').spawn;
     //var process = spawn('python', ['./src/model/engine/question_gen.py'])
    }

    function read_json(json_filepath){
      const fs = require("fs")
      return (JSON.parse(fs.readFileSync(json_filepath)))
    }

    function write_json(data, json_filepath){
      const fs = require("fs")
      fs.writeFileSync(json_filepath, JSON.stringify(data))
    }

    function buildQuiz(){
      // variable to store the HTML output
      const output = [];
  
      // for each question...
      myQuestions.forEach(
        (currentQuestion, questionNumber) => {
  
          // variable to store the list of possible answers
          const answers = [];
          if (currentQuestion.type == "mcq"){
          // and for each available answer...
            for(letter in currentQuestion.answers){
    
              // ...add an HTML radio button
              answers.push(
                `<label>
                  <input type="radio" id="q${questionNumber}" name="question${questionNumber}" value="${letter}">
                  ${letter} :
                  ${currentQuestion.answers[letter]}
                </label>`
              );
            }
          }
          else if (currentQuestion.type == "short"){
            // and for each available answer...
              answers.push(
                `<label>
                  <input type="text" class="short" id="q${questionNumber}" name="question${questionNumber}" placeholder="Answer here...">
                 </label>`
                
              );
          }
          else if (currentQuestion.type == "long"){
            // and for each available answer...
              answers.push(
                `<label class="longlable" href="#q${questionNumber}">
                  <textarea rows="4" cols="50" class="long" id="q${questionNumber}" name="question${questionNumber}" placeholder="Answer here..."></textarea>
                 </label>`
                
              );
          }
  
          // add this question and its answers to the output
          output.push(
            `<div class="question"> <b> ${currentQuestion.question} </b> </div> <br>
            <div class="answers"> ${answers.join('')} </div> `
          );
        }
      );
  
      // finally combine our output list into one string of HTML and put it on the page
      quizContainer.innerHTML = output.join('');
    }
  
    function showResults(){
  
      // gather answer containers from our quiz
      const answerContainers = quizContainer.querySelectorAll('.answers');
  
      // keep track of user's answers
      let numCorrect = 0;
  
      // for each question...
      myQuestions.forEach( (currentQuestion, questionNumber) => {
  
        // find selected answer
        const answerContainer = answerContainers[questionNumber];        
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
  
        // if answer is correct
        if(userAnswer === currentQuestion.correctAnswer){
          // add to the number of correct answers
          numCorrect++;
  
          // color the answers green
          answerContainers[questionNumber].style.color = 'mediumseagreen';
        }
        else if (currentQuestion.type == "short"){
          const selector = `input[name=question${questionNumber}]`;
          const userAnswer = (answerContainer.querySelector(selector)).value;
          if (userAnswer == currentQuestion.correctAnswer){
            numCorrect++;
            //document.getElementById("q".concat(questionNumber)).style.backgroundColor = "lightgreen";
            document.getElementById("q".concat(questionNumber)).style.border = "2px solid mediumseagreen";
          }
          else{
            //document.getElementById("q".concat(questionNumber)).style.backgroundColor = "red";
            document.getElementById("q".concat(questionNumber)).style.border = "2px solid red";
          }
        }
        else if (currentQuestion.type == "long"){
          const selector = `textarea[name=question${questionNumber}]`;
          const userAnswer = (answerContainer.querySelector(selector)).value;
          if (userAnswer == currentQuestion.correctAnswer){
            numCorrect++;
            //document.getElementById("q".concat(questionNumber)).style.backgroundColor = "lightgreen";
            document.getElementById("q".concat(questionNumber)).style.border = "2px solid mediumseagreen";
          }
          else{
            //document.getElementById("q".concat(questionNumber)).style.backgroundColor = "red";
            document.getElementById("q".concat(questionNumber)).style.border = "2px solid red";
          }
        }
        // if answer is wrong or blank
        else{
          // color the answers red
          answerContainers[questionNumber].style.color = 'red';
        }
      });
  
      // show number of correct answers out of total
      resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
    }  
    const quizContainer = document.getElementById('quiz');
    const resultsContainer = document.getElementById('results');
    const submitButton = document.getElementById('submit');

    let myQuestions = []

    function checkExistsWithTimeout(filePath, timeout) {
      return new Promise(function (resolve, reject) {
  
          var timer = setTimeout(function () {
              watcher.close();
              reject(new Error('File did not exists and was not created during the timeout.'));
          }, timeout);
  
          fs.access(filePath, fs.constants.R_OK, function (err) {
              if (!err) {
                  clearTimeout(timer);
                  watcher.close();
                  myQuestions = read_json(filePath)
                  buildQuiz();
                  resolve();
              }
          });
  
          var dir = path.dirname(filePath);
          var basename = path.basename(filePath);
          var watcher = fs.watch(dir, function (eventType, filename) {
              if (eventType === 'rename' && filename === basename) {
                  clearTimeout(timer);
                  watcher.close();
                  myQuestions = read_json(filePath)
                  buildQuiz();
                  resolve();
              }
          });
      });
    }

    fs.unlinkSync("./src/view/js/json/questions.json")

    run_python()

    //const myQuestions = read_json("./src/view/js/json/questions.json")
    
    checkExistsWithTimeout("./src/view/js/json/questions.json", 2000) //The operation of Creating an Array and Saving it to JSON takes 150ms, 1400 for 5 mcqs, 1650 for 5 mcq 5 short
  
    // Event listeners
    submitButton.addEventListener('click', showResults);

    // Basic Styling Stuff
    //$('textarea').autoResize(); // not working for some reason
  })();