<script>
	import AutoComplete from "simple-svelte-autocomplete";
	
	const subjects = ["Computer Science", "Mathematics Analysis & Approaches", "Physics"];
    const shortform = ["CSC", "MAA", "PHY"]
	
	let subject = "";

    console.log(subject)

    function generateQuestions() {
        let generate_sub = shortform[subjects.indexOf(subject)]
        console.log(generate_sub)
    }
</script>

<h2>Subject</h2>
<AutoComplete items={subjects} class="dropdown" placeholder="Enter Subject" bind:selectedItem={subject} style="width: 40%;"/>
<button on:click={generateQuestions}>Generate Quiz</button>