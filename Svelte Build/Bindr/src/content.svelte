<script>
    import {db, storage} from './firebase';
    import {collectionData} from 'rxfire/firestore';
    import {startWith} from 'rxjs/operators';
    import Youtube from "./youtube.svelte";
    import Markdown from "./markdown.svelte";
    import markdownText from "./test.md";

    let markdown_text_2 = "The *FitnessGram*^TM **PACER** Test is a multistage ## aerobic capacity test that *progressively* gets more difficult as it continues. The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound.";
    //export let subject_code;
    //export let topic_code;
    let subject_code = 'CSC';
    let topic_code = 'Topic_1';
    let topic_sub_code = 'Topic_1.0';
    let markdown_file;

    var pathReference = storage.ref("Content/");

    storageRef.child(subject_code + "/" + topic_code + ".md").getDownloadURL()
    .then((url) => {
    // `url` is the download URL for 'images/stars.jpg'
    markdown_file = url;
    // Or inserted into an <img> element
  })
  .catch((error) => {
    // Handle any errors
  });
    
    /*
    db.collection('Resources').doc(subject_code).collection(topic_code).get().then((content_data) => {
        content_data.docs.forEach(doc => {
            console.log(doc.id);
            console.log(doc.data().para);
            add_component(doc);
        });
    });
    */

    /* Firestore Auth User code which I will probably forget
        service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}
    */
    function add_component (doc) {
        console.log(doc.data().para)
        let paras = doc.data().para;

        var html="";
        console.log(paras.length)
        for (let i=0;i<paras.length; i++) {
            console.log(paras[i]);
            html +=paras[i];
        }
        console.log("Boop"+html)
        document.getElementById("content-page").innerHTML+= "<h1>"+doc.id+"</h1>" + html;

        //components include headings [head], paragraphs [para], tips [tip], hints [hint], questions [quest], videos [vid]
    }


</script>

<style>

    :root {
        --theme-color: ;
        --font-primary: ;
        --font-seocndary: ;
    }

    h1 {
        font-size: 3em;
    }
    .content {
        text-align:justify;
        background-color: azure;
        margin:auto;
        padding:4rem;
        border-radius: 10px;
    }


    .wrapper {
        background-color: antiquewhite;
        padding:15%
    }
</style>
<!--
<section class='wrapper'>
        <div id="content-page" class='content'></div>
</section>
-->
<!-- Markdown from string  -->
<Markdown markdown="## *Bindr more like* 
# Bndr"/>

<Markdown markdown={markdown_text_2}/>

<Markdown markdown={markdown_file}/>

<!-- Markdown from file -->
<Markdown markdown={markdownText}/> 