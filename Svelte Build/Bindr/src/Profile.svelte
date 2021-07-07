<script>

    import { db } from './firebase';
    import { collectionData } from 'rxfire/firestore';
    import { startWith } from 'rxjs/operators';
    import { createEventDispatcher } from 'svelte';
    import { onMount } from 'svelte';
    import User from "./User.svelte"

    import AutoComplete from "simple-svelte-autocomplete";

    export let uid;

    console.log(uid)

    const query = db.collection('profiles').where('uid', '==', uid).orderBy('saved');

    const profiles = collectionData(query, 'id').pipe(startWith([]));

    var subjects = ["English Literature", "English Literature and Language", "Spanish Ab Initio", "Spanish B", "French Ab Initio", "French B", "Hindi Ab Initio", "Hindi B", "Business Management", "Economics", "Geography", "Global Politics", "History", "Information Technology in a Global Society", "Philosophy", "Psychology", "Social and Cultural Anthropology", "World Religions", "Biology", "Chemistry", "Computer Science", "Design Technology", "Environmental Systems and Societies", "Physics", "Sports, Exercise, and Health Science", "Mathematics Analysis and Approaches", "Mathematics Application and Interpretations", "Dance", "Film", "Music", "Theatre", "Visual Arts"]

    let FLAG_newUser = true;

    let data = {
        name: "",
        email: "",
        phone: "",
        subjects: [{name: "", level: "", grade: 1}, {name: "", level: "", grade: 1}, {name: "", level: "", grade: 1}, {name: "", level: "", grade: 1}, {name: "", level: "", grade: 1}, {name: "", level: "", grade: 1}]
    }

    function updateProfile(event) {
        const { id, new_data } = event.detail;
        db.collection('profiles').doc(id).delete();
        db.collection('profiles').add({ uid, data, saved: Date.now() });
        alert("Your profile has been updated.")
    }

    function fillInfo(event) {
        const { id, new_data } = event.detail;
        Object.keys(new_data).forEach(function(key) {
            data[key] = new_data[key]
        })
        FLAG_newUser = false;
        if (Object.keys(new_data).length != Object.keys(data).length) {
            db.collection('profiles').doc(id).delete();
            db.collection('profiles').add({ uid, data, saved: Date.now() });
        }
    }

    function addNewProfile() {
        db.collection('profiles').add({ uid, data, saved: Date.now() })
        alert("Your profile has been added.")
    }

</script>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<body>
<div class="container">
    <div class="row gutters">
        <div class="col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12">
            <div class="card h-100">
                <div class="card-body">
                    <div class="account-settings">
                        <div class="user-profile">
                            <div class="user-avatar">
                                <img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="Maxwell Admin">
                            </div>
                            <h5 class="user-name">{data.name}</h5>
                            <h6 class="user-email">{data.email}</h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
            <div class="card h-100">
                <div class="card-body">
                    <div class="row gutters">
                        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                            <h6 class="mb-3 text-primary">Personal Details</h6>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                            <div class="form-group">
                                <label for="fullName">Full Name</label>
                                <input type="text" class="form-control" id="fullName" placeholder="Enter full name" bind:value={data.name}>
                            </div>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                            <div class="form-group">
                                <label for="eMail">Email</label>
                                <input type="email" class="form-control" id="eMail" placeholder="Enter email ID" bind:value={data.email}>
                            </div>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                            <div class="form-group">
                                <label for="phone">Phone</label>
                                <input type="text" class="form-control" id="phone" placeholder="Enter phone number" bind:value={data.phone}>
                            </div>
                        </div>
                    </div>
                    <div class="row gutters">
                        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                            <h6 class="mb-3 text-primary">IB Subjects</h6>
                        </div>
                        {#each data.subjects as subject}
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <AutoComplete items={subjects} type="name" class="form-control" placeholder="Enter Subject" bind:selectedItem={subject.name}/>
                                    <AutoComplete items={["Higher Level (HL)", "Standard Level (SL)"]} class="form-control" placeholder="Enter Subject Level" bind:selectedItem={subject.level}/>
                                    <AutoComplete items={[1, 2, 3, 4, 5, 6, 7]} class="form-control" placeholder="Enter Current Level (1-7)" bind:selectedItem={subject.grade}/>
                                </div>
                            </div>
                        {/each}
                    </div>
                    {#if FLAG_newUser}
                        <button on:click={addNewProfile}> Add Profile </button>
                    {/if}
                    {#each $profiles as profile}
                        <User {...profile} on:update={updateProfile} on:u_data={fillInfo}/>
                    {/each}
                </div>
            </div>
        </div>
    </div>
    </div>
</body>

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