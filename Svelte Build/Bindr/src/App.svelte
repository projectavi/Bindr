<script>
	import { auth, googleProvider } from './firebase';
    import { authState } from 'rxfire/auth';

	import Content from './content.svelte';
	import Homescreen from './homescreen.svelte';
	let user;

	import { Router, Route, Link } from "svelte-navigator";
	import Login from "./Login.svelte";
	import PrivateRoute from "./PrivateRoute.svelte";
	import { userAcc } from "./store";

	const unsubscribe = authState(auth).subscribe(u => user = u); //This line gives an error but when it is deleted the login stops working so don't delete it

	function signout() {
		// user = null;
		auth.signOut()
		console.log(user)
		$userAcc = user
	}

	function signin() {
		auth.signInWithPopup(googleProvider);
		console.log(user)
		$userAcc = user
	}
</script>

<main>
	<!--<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<button on:click={login}>Login with Google</button>
	<Content/>
	-->

	<Router>
		<header>
		  <h1>History</h1>
	  
		  <nav>
			<Link to="/">Home</Link>
			<Link to="about">About</Link>
			<Link to="profile">Profile</Link>

			<div>
				{#if user}
					<button on:click={signout}>Logout</button>
				{:else}
					<button on:click={signin}>
						Sign In with Google
					</button>
				{/if}
			</div>

			<p>{user}</p>

		  </nav>

		</header>
	  
		<main>
		  <Route path="login">
			<Login />
		  </Route>
	  
		  <Route path="/">
			<Homescreen/>	
		  </Route>
	
	  
		  <PrivateRoute path="profile" let:location>
			<h3>Welcome {$user.username}</h3>
			<button on:click={signout}>Logout</button>
		  </PrivateRoute>
		</main>
	  </Router>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>