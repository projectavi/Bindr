<script>
    import {db} from './firebase';
    import {collectionData} from 'rxfire/firestore';
    import {startWith} from 'rxjs/operators';
    import Youtube from "./youtube.svelte";

    //export let subject_code;
    //export let topic_code;
    let subject_code = 'CSC';
    let topic_code = 'Topic_1';
    let topic_sub_code = 'Topic_1.0';

    db.collection('Resources').doc(subject_code).collection(topic_code).get().then((content_data) => {
        content_data.docs.forEach(doc => {
            console.log(doc.id);
            console.log(doc.data().para);
            add_component(doc);
        });
    });

    

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

<section class='wrapper'>
        <div id="content-page" class='content'></div>
</section>