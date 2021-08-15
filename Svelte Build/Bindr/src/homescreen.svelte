<script>
    //export username

    import { Router, Route, Link } from "svelte-navigator";

    let username = "Test"
</script>

<style>
    /*
    .wrapper1 {
        display:flex;       
    }

    .banner {
        height:15%;
    }
 
    .option-area {
        width: 1fr/3;
        transform: rotate(90deg);
    }

    #quiz {
        background-color:cyan;
    }

    #notes {
        background-color:lawngreen;
    }
    
    #content {
        background-color:indianred;
    }
    */
    /*
    @font-face {
        font-family:'font-space';
        src: url('resources/other/Font/woff2/SpaceGrotesk[wght].woff2') format ("wofff2")
            url('./resources/other/Font/ttf/static/SpaceGrotesk-Regular.ttf');
    }
    */
    @font-face {
        font-family:'font-space';
        font-style: normal;
        font-weight: 400;
        src: url('./resources/other/Font/ttf/static/SpaceGrotesk-Regular.ttf') format('ttf');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    /*Defaulword
    ts for the entire page, change these, and you can change almost all the colors*/

    :root {
        --bg-p: #2A2A2A;
        /*Background primary variable*/
        --bg-s: #4F4F4F;
        /*Background primary variable*/
        --text-p: #FFFFFF;
        /*Text primary variable*/
        --text-s: #7F7F7F;
        /*Text secondary variable*/
        --theme-p: #222277;
        /*Theme primary variable*/
        --theme-s: #227722;
        /*Theme Seconary variable*/
        --theme-t: #772222;
        /*Theme Tertiary variable*/
        
        font-size: 16px;
        font-family:'font-space';
    }

    body {
        margin: 0;
        height: 100%;
        font-family: "font-space";
    }

    .selection-grid {
        font-size:30px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-column-gap: 5px;
        width: 100%;
        height: 90%;
    }

    #notes {
        width: 100%;
        height: 100%;
        background-color: rgb(106, 194, 18);
    }

    #quizzes {
        width: 100%;
        height: 100%;
        background-color: rgb(0, 174, 255);
    }

    #resources {
        width: 100%;
        height: 100%;
        background-color: indianred;
    }

    .element {
        justify-content: center;
        text-align: center;
        grid-column: auto;
        filter: grayscale(100%);
    }

    .element span h1{
        text-align: left;
        transform:rotate(90deg) translate(200px, 200px);
    }

    .element:hover {
        filter: grayscale(0%);
        transition: 600ms;
        color:var(--text-p);
    }

    .screen {
		height:100%;
		width:100%;

	}
</style>
<!--
<section>
    <div id="wrapper1">
        <div id="banner">
            Welcome to Bindr {username}
        </div>
        <div id="wrapper2">
            <div id="quiz" class="option-area">
                Quiz
            </div>

            <div id="notes" class="option-area">
                Notes
            </div>

            <div id="content" class="option-area">
                Content
            </div>
        </div>
    </div>
</section>
-->
<body class='screen'>
    <header style="height:10%;">
        <h2>Welcome to Bindr</h2>
    </header>
    <div class='selection-grid'>
        <Link to="/notes">
            <div id="notes" class="element">
                <span><h1>Notes</h1></span>
            </div>
        </Link>
        <Link to="/quiz">
            <div id="quizzes" class="element">
                <span><h1>Quizzes</h1></span>
            </div>
        </Link>
        <Link to="/resources">
        <div id="resources" class="element">
            <span><h1>Resources</h1></span>
        </div>
        </Link>
    </div>
</body>
