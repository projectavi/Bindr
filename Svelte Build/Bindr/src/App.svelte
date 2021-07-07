<script>
	import { auth, googleProvider } from './firebase';
    import { authState } from 'rxfire/auth';

	import Content from './content.svelte';
	import Homescreen from './homescreen.svelte';
	export let name;

	import { Router, Route, Link } from "svelte-navigator";
	import Login from "./Login.svelte";
	import PrivateRoute from "./PrivateRoute.svelte";
	import { user } from "./store";

	function handleLogout() {
		$user = null;
	}

	function login() {
		auth.signInWithPopup(googleProvider);
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<button on:click={login}>Login with Google</button>
	<Content/>
	

	<Router>
		<header>
		  <h1>History</h1>
	  
		  <nav>
			<Link to="/">Home</Link>
			<Link to="about">About</Link>
			<Link to="profile">Profile</Link>
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
			<button on:click={handleLogout}>Logout</button>
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