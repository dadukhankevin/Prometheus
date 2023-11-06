<script>
    import { FireOutline } from 'flowbite-svelte-icons';
    export let post;
    export let name;

</script>

<div class="card p-4 card-hover post text-left ruounded-lg">
  <header  class="card-header">
        {name}
  </header>
  <content>
      <p class="p-8">
         {post}
      </p>
  </content>
  <footer class="card-footer">

  </footer>
</div>
<style>
  .post {
      width: 80%;
  }
</style>
