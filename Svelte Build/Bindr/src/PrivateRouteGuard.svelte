<script>
    import { useNavigate, useLocation } from "svelte-navigator";
    import { userAcc } from "./store";
  
    const navigate = useNavigate();
    const location = useLocation();
  
    $: if (!$userAcc) {
      navigate("/login", {
        state: { from: $location.pathname },
        replace: true,
      });
    }
  </script>
  
  {#if $userAcc}
    <slot />
  {/if}
  