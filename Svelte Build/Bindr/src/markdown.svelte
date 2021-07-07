<!--Markdown Parser-->
<!--Lots of code taken from https://www.chrsjxn.io/svelte/adding-markdown-->
<script>
    import MarkdownIt from 'markdown-it';
    export let markdown = '';

    // https://www.chrsjxn.io/svelte/adding-markdown
    const md = new MarkdownIt();
    
    const rendered_md = md.render(markdown);
</script>

<div>
    {@html rendered_md}
</div>