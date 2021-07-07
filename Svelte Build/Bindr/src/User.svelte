<script>
    import { db } from './firebase';
    import { collectionData } from 'rxfire/firestore';
    import { startWith } from 'rxjs/operators';
    import { createEventDispatcher } from 'svelte';
    import { onMount } from 'svelte';

    const dispatch = createEventDispatcher();

    console.log("mounted")

    function update() {
        console.log("1", data)

		dispatch('update', { id, new_data: data });
	};

    export let id; // document ID
    export let data;

    onMount(async () => {
        console.log("Dispatching")
		dispatch("u_data", { id, new_data: data });
        console.log("Dispatched.")
	});
</script>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>

<div class="row gutters">
    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
        <div class="text-right">
            <button type="button" id="submit" name="submit" class="btn btn-secondary">Cancel</button>
            <button type="button" id="submit" name="submit" class="btn btn-primary" on:click={update}>Update</button>
        </div>
    </div>
</div>

<style>
    body{
        margin-top:20px;
        color: #bcd0f7;
        background: #1A233A;
    }
    .account-settings .user-profile {
        margin: 0 0 1rem 0;
        padding-bottom: 1rem;
        text-align: center;
    }
    .account-settings .user-profile .user-avatar {
        margin: 0 0 1rem 0;
    }
    .account-settings .user-profile .user-avatar img {
        width: 90px;
        height: 90px;
        -webkit-border-radius: 100px;
        -moz-border-radius: 100px;
        border-radius: 100px;
    }
    .account-settings .user-profile h5.user-name {
        margin: 0 0 0.5rem 0;
    }
    .account-settings .user-profile h6.user-email {
        margin: 0;
        font-size: 0.8rem;
        font-weight: 400;
    }
    .account-settings .about {
        margin: 1rem 0 0 0;
        font-size: 0.8rem;
        text-align: center;
    }
    .card {
        background: #272E48;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        border: 0;
        margin-bottom: 1rem;
    }
    .form-control {
        border: 1px solid #596280;
        -webkit-border-radius: 2px;
        -moz-border-radius: 2px;
        border-radius: 2px;
        font-size: .825rem;
        background: #1A233A;
        color: #bcd0f7;
    }
</style>