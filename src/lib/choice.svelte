<script>
    import { FireOutline } from 'flowbite-svelte-icons';
    let options = [{name: "option 1", value: false}, 
                    {name: "option 2", value: true}];
    export let multiple_choice;
    export let quiz_question;

    function verify(value){
        if (value){
            alert("yay");
        }
    }
</script>

<div class="card p-4 card-hover post text-left ruounded-lg">
  <header  class="card-header  flex flex-col justify-center items-center">
      <FireOutline size="xl" col/>
  </header>
  <content>
      <p class="p-8">
          {quiz_question}
      </p>
  </content>
  <footer class="">
    {#each multiple_choice as choice}
    <br>
        <button type="button" on:click={()=>{verify(choice.correct)}} class="card p-2 m-2 w-full text-left">- {choice.choice}</button>
    {/each}
</footer>
</div>
<style>
  .post {
      width: 80%;
  }
</style>
