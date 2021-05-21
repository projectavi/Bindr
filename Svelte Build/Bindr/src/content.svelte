<script>
    import Youtube from "./youtube.svelte";

    function add_component (comp_type, data) {
        //comp_type is the type of component to be added - for example, a paragraph
        //components include headings [head], paragraphs [para], tips [tip], hints [hint], questions [quest], videos [vid]
        if (comp_type = "para") {
            document.getElementById("content-page").innerHTML = document.getElementById("content-page").innerHTML + "<p>" + data + "</p>";
        }

    }
</script>

<style>
</style>

<div id="content-page">

</div>