(function(){
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
                  <textarea rows="4" cols="50" class="long" id="q${questionNumber}" name="question${questionNumber}"></textarea>
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
    const myQuestions = [
      {
        type: "mcq",
        question: "Question 1",
        answers: {
          a: "Answer 1",
          b: "Answer 2",
          c: "Answer 3"
        },
        correctAnswer: "c"
      },
      {
        type: "mcq",
        question: "Question 2",
        answers: {
            a: "Answer 1",
            b: "Answer 2",
            c: "Answer 3"
        },
        correctAnswer: "c"
      },
      {
        type: "mcq",
        question: "Question 3",
        answers: {
            a: "Answer 1",
            b: "Answer 2",
            c: "Answer 3"
        },
        correctAnswer: "a"
      },
      {
        type: "short",
        question: "Question 4",
        correctAnswer: "TestAnswer"
      },
      {
        type: "short",
        question: "Question 5",
        correctAnswer: "TestAnswers"
      },
      {
        type: "long",
        question: "Question 6",
        correctAnswer: "Test",
      }
    ];

    // Kick things off
    buildQuiz();
  
    // Event listeners
    submitButton.addEventListener('click', showResults);

    // Basic Styling Stuff
    $('textarea').autoResize();
  })();