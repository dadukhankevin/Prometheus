<script>
    import { FireOutline } from 'flowbite-svelte-icons';
</script>

<div class="card p-4 card-hover post text-left ruounded-lg">
  <header  class="card-header  flex flex-col justify-center items-center">
      <FireOutline size="xl" col/>
  </header>
  <content>
      <p class="p-8">
          When was the Fall of Rome?
      </p>
  </content>
  <footer class="card-footer text-center">
      <input
      class="bg-primary-200 border-0 ring-0 w-96 text-black rounded-xl"
      name="prompt"
      id="prompt"
      placeholder="Answer"
  />    
</footer>
</div>
<style>
  .post {
      width: 80%;
  }
</style>
