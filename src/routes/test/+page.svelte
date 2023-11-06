<script>
    let message = '';
    let response = '';
  
    async function echo() {
      const res = await fetch(`/api/feed?message=${message}`);
      response = await res.text();
    }
    
  </script>
  
  <h1>Simple Echo Server</h1>
  <input type="text" bind:value={message} />
  <button on:click={echo}>Echo</button>
  <p>{response}</p>
  